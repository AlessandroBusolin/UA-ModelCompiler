﻿using System.Text;
using System.Reflection;

namespace ModelCompiler
{
    class HeaderUpdateTool
    {
        public enum LicenseType
        {
            MIT,
            MITXML,
            FLC
        }

        static string RemoveXmlHeader(string fileText)
        {
            bool inComment = false;
            bool inDirective = false;

            for (int ii = 0; ii < fileText.Length; ii++)
            {
                if (!inComment && !inDirective)
                {
                    if (fileText[ii] == '<')
                    {
                        if (!inComment)
                        {
                            if (fileText[ii + 1] == '!')
                            {
                                inComment = true;
                                continue;
                            }
                        }

                        if (!inDirective)
                        {
                            if (fileText[ii + 1] == '?')
                            {
                                inDirective = true;
                                continue;
                            }
                        }

                        return fileText.Substring(ii);
                    }
                }
                else
                {
                    if (fileText[ii] == '>')
                    {
                        if (inComment)
                        {
                            if (fileText[ii - 1] == '-')
                            {
                                inComment = false;
                                continue;
                            }
                        }

                        if (inDirective)
                        {
                            if (fileText[ii - 1] == '?')
                            {
                                inDirective = false;
                                continue;
                            }
                        }
                    }
                }
            }

            return fileText;
        }

        static string RemoveCStyleHeader(string fileText)
        {
            bool inComment = false;
            bool newLine = false;

            fileText = fileText.TrimStart();

            if (!fileText.StartsWith("/*"))
            {
                return fileText;
            }

            for (int ii = 0; ii < fileText.Length; ii++)
            {
                if (!inComment)
                {
                    if (fileText[ii] == '/')
                    {
                        if (fileText[ii + 1] == '*')
                        {
                            inComment = true;
                            newLine = false;
                            continue;
                        }
                    }
                }
                else
                {
                    if (fileText[ii] == '\n')
                    {
                        if (inComment)
                        {
                            newLine = true;
                        }
                    }

                    if (fileText[ii] == '/')
                    {
                        if (inComment)
                        {
                            if (fileText[ii - 1] == '*')
                            {
                                if (newLine)
                                {
                                    while (fileText[ii++] != '\n') ;
                                    var text = fileText.Substring(ii).Trim();
                                    text = $"{Environment.NewLine}{text}";
                                    return text;
                                }
                                else
                                {
                                    inComment = false;
                                }
                            }
                        }
                    }
                }
            }

            return fileText;
        }

        public static void ProcessDirectory(string directory, string fileType, LicenseType licenseType, bool silent = false)
        {
            int count = 0;
            ProcessDirectory(new DirectoryInfo(directory), fileType, licenseType, silent, ref count);
            Console.WriteLine("Updating {0} files.", count);
        }

        private static void ProcessDirectory(DirectoryInfo directory, string fileType, LicenseType licenseType, bool silent, ref int count)
        {
            foreach (FileInfo file in directory.GetFiles(fileType))
            {
                if (!silent)
                {
                    Console.WriteLine("Updating file: {0}", file);
                }

                // fetch file text.
                string fileText = null;
                Encoding encoding = Encoding.Default;

                using (StreamReader reader = new StreamReader(file.FullName, true))
                {
                    fileText = reader.ReadToEnd();
                    encoding = reader.CurrentEncoding;
                }

                fileText = fileText.Trim();

                if (licenseType == LicenseType.MITXML)
                {
                    fileText = RemoveXmlHeader(fileText);
                }
                else if (licenseType == LicenseType.MIT)
                {
                    fileText = RemoveCStyleHeader(fileText);
                }
                else if (licenseType == LicenseType.FLC)
                {
                    fileText = RemoveCStyleHeader(fileText);
                }

                // load the selected license.
                string license = null;
                string resourcePath = null;

                switch (licenseType)
                {
                    case LicenseType.FLC: { resourcePath = "ModelCompiler.License.FLC.txt"; break; }
                    case LicenseType.MIT: { resourcePath = "ModelCompiler.License.UA_MIT.txt"; break; }
                    case LicenseType.MITXML: { resourcePath = "ModelCompiler.License.UA_MIT_XML.txt"; break; }
                }

                Stream istrm = Assembly.GetExecutingAssembly().GetManifestResourceStream(resourcePath);

                using (StreamReader reader = new StreamReader(istrm))
                {
                    license = reader.ReadToEnd().Trim();
                }

                // write header and body.
                StreamWriter writer = null;

                if (encoding != Encoding.UTF8)
                {
                    writer = new StreamWriter(file.FullName, false, encoding);
                }
                else
                {
                    writer = new StreamWriter(file.FullName);
                }

                using (writer)
                {
                    if (!String.IsNullOrEmpty(license))
                    {
                        writer.WriteLine(license);

                        if (licenseType == LicenseType.MITXML)
                        {
                            writer.WriteLine();
                        }
                    }

                    writer.WriteLine(fileText);
                    count++;
                }
            }

            // recursively process sub directories.
            foreach (DirectoryInfo subdirectory in directory.GetDirectories())
            {
                ProcessDirectory(subdirectory, fileType, licenseType, silent, ref count);
            }
        }
    }
}
