/* ========================================================================
 * Copyright (c) 2005-2009 The OPC Foundation, Inc. All rights reserved.
 *
 * OPC Foundation MIT License 1.00
 * 
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following
 * conditions:
 * 
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 *
 * The complete license agreement can be found here:
 * http://opcfoundation.org/License/MIT/1.00/
 * ======================================================================*/

using System.Text;
using System.Xml;
using System.Reflection;
using System.Xml.Schema;

namespace Opc.Ua.Schema.Xml
{
    /// <summary>
    /// Generates files used to describe data types.
    /// </summary>
    public class XmlSchemaValidator : SchemaValidator
    {       
        #region Constructors
		/// <summary>
		/// Intializes the object with default values.
		/// </summary>
		public XmlSchemaValidator()
		{
            SetResourcePaths(WellKnownDictionaries);
		}

		/// <summary>
		/// Intializes the object with a file table.
		/// </summary>
		public XmlSchemaValidator(Dictionary<string,string> fileTable) : base(fileTable)
		{
            SetResourcePaths(WellKnownDictionaries);
		}
        #endregion      
        
        #region Public Members
        /// <summary>
        /// The schema set that was validated.
        /// </summary>
        public XmlSchemaSet SchemaSet
        {
            get { return m_schemaSet; }
        }
        /// <summary>
        /// The schema that was validated.
        /// </summary>
        public XmlSchema TargetSchema
        {
            get { return m_schema; }
        }
        
		/// <summary>
		/// Generates the code from the contents of the address space.
		/// </summary>
		public void Validate(string inputPath)
		{
            Validate(File.OpenRead(inputPath));
        }

		/// <summary>
		/// Generates the code from the contents of the address space.
		/// </summary>
		public void Validate(Stream stream)
		{
            m_schema = XmlSchema.Read(stream, new ValidationEventHandler(OnValidate));

            foreach (XmlSchemaImport import in m_schema.Includes)
            {                    
                if (import.Namespace == Namespaces.OpcUa)
                {
                    StreamReader strm = new StreamReader(Assembly.Load("Opc.Ua.Core").GetManifestResourceStream("Opc.Ua.Model.Opc.Ua.Types.xsd"));
                    import.Schema = XmlSchema.Read(strm, new ValidationEventHandler(OnValidate));
                    continue;
                }

                string location = null;

                if (!KnownFiles.TryGetValue(import.Namespace, out location))
                { 
                    location = import.SchemaLocation;
                }
                
                FileInfo fileInfo = new FileInfo(location);

                if (!fileInfo.Exists)
                {
                    StreamReader strm = new StreamReader(Assembly.GetExecutingAssembly().GetManifestResourceStream(location));
                    import.Schema = XmlSchema.Read(strm, new ValidationEventHandler(OnValidate));
                }
                else
                {
                    Stream strm = File.OpenRead(location);
                    import.Schema = XmlSchema.Read(strm, new ValidationEventHandler(OnValidate));
                }                
            }
 
            m_schemaSet = new XmlSchemaSet();
            m_schemaSet.Add(m_schema);
            m_schemaSet.Compile();                        
		}       

        /// <summary>
        /// Returns the schema for the specified type (returns the entire schema if null).
        /// </summary>
        public override string GetSchema(string typeName)
        {
            XmlWriterSettings settings = new XmlWriterSettings();
            
            settings.Encoding    = Encoding.UTF8;
            settings.Indent      = true;
            settings.IndentChars = "    ";

            MemoryStream ostrm = new MemoryStream();
            XmlWriter writer = XmlWriter.Create(ostrm, settings);
            
            try
            {
                if (typeName == null || m_schema.Elements.Values.Count == 0)
                {
                    m_schema.Write(writer);
                }
                else
                {
                    foreach (XmlSchemaObject current in m_schema.Elements.Values)
                    {       
                        XmlSchemaElement element = current as XmlSchemaElement;

                        if (element != null)
                        {
                            if (element.Name == typeName)
                            {                                
                                XmlSchema schema = new XmlSchema();
                                schema.Items.Add(element.ElementSchemaType);
                                schema.Items.Add(element);
                                schema.Write(writer);
                                break;
                            }
                        }
                    }
                }
            }
            finally
            {
                writer.Close();
            }

            return new UTF8Encoding().GetString(ostrm.ToArray());
        } 
        #endregion      
        
        #region Private Methods
        /// <summary>
        /// Handles a valdiation error.
        /// </summary>
        static void OnValidate(object sender, ValidationEventArgs args)
        {
            throw new InvalidOperationException(args.Message, args.Exception);
        }
        #endregion    

        #region Private Fields
        private readonly string[][] WellKnownDictionaries = new string[][]
        {
            new string[] {  Namespaces.OpcUaBuiltInTypes, "Opc.Ua.Schema.Xml.BuiltInTypes.xsd" }
        };

        private XmlSchema m_schema;
        private XmlSchemaSet m_schemaSet;
        #endregion
    }
}
