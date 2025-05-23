const string NS = 'tag:opc-foundation.org,2024-01:DemoModel';

export class BrowseNames {
   static readonly Blue: string = 'nsu=' + NS + ';Blue';
   static readonly DemoModel_BinarySchema: string = 'nsu=' + NS + ';DemoModel';
   static readonly DemoModel_XmlSchema: string = 'nsu=' + NS + ';DemoModel';
   static readonly EnumUnderscoreTest: string = 'nsu=' + NS + ';EnumUnderscoreTest';
   static readonly HeaterStatus: string = 'nsu=' + NS + ';HeaterStatus';
   static readonly Pink_Placeholder: string = 'nsu=' + NS + ';<Pink>';
   static readonly Red: string = 'nsu=' + NS + ';Red';
   static readonly RestrictedObjectType: string = 'nsu=' + NS + ';RestrictedObjectType';
   static readonly RestrictedVariableType: string = 'nsu=' + NS + ';RestrictedVariableType';
   static readonly SampleStructureAllowSubtypes: string = 'nsu=' + NS + ';SampleStructureAllowSubtypes';
   static readonly SampleStructureWithOptionalFields: string = 'nsu=' + NS + ';SampleStructureWithOptionalFields';
   static readonly SampleUnion: string = 'nsu=' + NS + ';SampleUnion';
   static readonly SampleUnionAllowSubtypes: string = 'nsu=' + NS + ';SampleUnionAllowSubtypes';
   static readonly Seeker: string = 'nsu=' + NS + ';Seeker';
   static readonly Test_Error: string = 'nsu=' + NS + ';Test_Error';
   static readonly Test_ErrorComponent: string = 'nsu=' + NS + ';Test_ErrorComponent';
   static readonly TestObject: string = 'nsu=' + NS + ';TestObject';
   static readonly Vector: string = 'nsu=' + NS + ';Vector';
   static readonly WithTwoDimensionalVariableType: string = 'nsu=' + NS + ';WithTwoDimensionalVariableType';
   static readonly WorkOrderStatusType: string = 'nsu=' + NS + ';WorkOrderStatusType';
   static readonly WorkOrderType: string = 'nsu=' + NS + ';WorkOrderType';
   static readonly X: string = 'nsu=' + NS + ';X';
   static readonly Yellow: string = 'nsu=' + NS + ';Yellow';
}

class DataTypeIds {
   static readonly EnumUnderscoreTest: string = 'nsu=' + NS + ';i=68';
   static readonly HeaterStatus: string = 'nsu=' + NS + ';i=1';
   static readonly Vector: string = 'nsu=' + NS + ';i=3';
   static readonly WorkOrderStatusType: string = 'nsu=' + NS + ';i=4';
   static readonly WorkOrderType: string = 'nsu=' + NS + ';i=5';
   static readonly SampleUnion: string = 'nsu=' + NS + ';i=41';
   static readonly SampleStructureWithOptionalFields: string = 'nsu=' + NS + ';i=42';
   static readonly SampleUnionAllowSubtypes: string = 'nsu=' + NS + ';i=43';
   static readonly SampleStructureAllowSubtypes: string = 'nsu=' + NS + ';i=44';
}

class MethodIds {
   static readonly RestrictedObjectType_Blue: string = 'nsu=' + NS + ';i=127';
   static readonly TestObject_Blue: string = 'nsu=' + NS + ';i=71';
}

class ObjectIds {
   static readonly Seeker: string = 'nsu=' + NS + ';i=95';
   static readonly TestObject: string = 'nsu=' + NS + ';i=128';
   static readonly Test_Error: string = 'nsu=' + NS + ';i=93';
   static readonly Test_ErrorComponent: string = 'nsu=' + NS + ';i=94';
   static readonly Vector_Encoding_DefaultBinary: string = 'nsu=' + NS + ';i=21';
   static readonly WorkOrderStatusType_Encoding_DefaultBinary: string = 'nsu=' + NS + ';i=22';
   static readonly WorkOrderType_Encoding_DefaultBinary: string = 'nsu=' + NS + ';i=23';
   static readonly SampleUnion_Encoding_DefaultBinary: string = 'nsu=' + NS + ';i=45';
   static readonly SampleStructureWithOptionalFields_Encoding_DefaultBinary: string = 'nsu=' + NS + ';i=46';
   static readonly SampleUnionAllowSubtypes_Encoding_DefaultBinary: string = 'nsu=' + NS + ';i=47';
   static readonly SampleStructureAllowSubtypes_Encoding_DefaultBinary: string = 'nsu=' + NS + ';i=48';
   static readonly Vector_Encoding_DefaultXml: string = 'nsu=' + NS + ';i=6';
   static readonly WorkOrderStatusType_Encoding_DefaultXml: string = 'nsu=' + NS + ';i=7';
   static readonly WorkOrderType_Encoding_DefaultXml: string = 'nsu=' + NS + ';i=8';
   static readonly SampleUnion_Encoding_DefaultXml: string = 'nsu=' + NS + ';i=62';
   static readonly SampleStructureWithOptionalFields_Encoding_DefaultXml: string = 'nsu=' + NS + ';i=63';
   static readonly SampleUnionAllowSubtypes_Encoding_DefaultXml: string = 'nsu=' + NS + ';i=64';
   static readonly SampleStructureAllowSubtypes_Encoding_DefaultXml: string = 'nsu=' + NS + ';i=65';
   static readonly Vector_Encoding_DefaultJson: string = 'nsu=' + NS + ';i=79';
   static readonly WorkOrderStatusType_Encoding_DefaultJson: string = 'nsu=' + NS + ';i=80';
   static readonly WorkOrderType_Encoding_DefaultJson: string = 'nsu=' + NS + ';i=81';
   static readonly SampleUnion_Encoding_DefaultJson: string = 'nsu=' + NS + ';i=82';
   static readonly SampleStructureWithOptionalFields_Encoding_DefaultJson: string = 'nsu=' + NS + ';i=83';
   static readonly SampleUnionAllowSubtypes_Encoding_DefaultJson: string = 'nsu=' + NS + ';i=84';
   static readonly SampleStructureAllowSubtypes_Encoding_DefaultJson: string = 'nsu=' + NS + ';i=85';
}

class ObjectTypeIds {
   static readonly RestrictedObjectType: string = 'nsu=' + NS + ';i=124';
   static readonly WithTwoDimensionalVariableType: string = 'nsu=' + NS + ';i=120';
}

class VariableIds {
   static readonly Seeker_Identities: string = 'nsu=' + NS + ';i=10';
   static readonly Seeker_AddIdentity_InputArguments: string = 'nsu=' + NS + ';i=25';
   static readonly Seeker_RemoveIdentity_InputArguments: string = 'nsu=' + NS + ';i=29';
   static readonly Seeker_AddApplication_InputArguments: string = 'nsu=' + NS + ';i=32';
   static readonly Seeker_RemoveApplication_InputArguments: string = 'nsu=' + NS + ';i=35';
   static readonly Seeker_AddEndpoint_InputArguments: string = 'nsu=' + NS + ';i=52';
   static readonly Seeker_RemoveEndpoint_InputArguments: string = 'nsu=' + NS + ';i=55';
   static readonly EnumUnderscoreTest_EnumValues: string = 'nsu=' + NS + ';i=69';
   static readonly RestrictedVariableType_Yellow: string = 'nsu=' + NS + ';i=123';
   static readonly RestrictedObjectType_Red: string = 'nsu=' + NS + ';i=125';
   static readonly RestrictedObjectType_Red_Yellow: string = 'nsu=' + NS + ';i=57';
   static readonly RestrictedObjectType_Pink_Placeholder: string = 'nsu=' + NS + ';i=132';
   static readonly RestrictedObjectType_Pink_Placeholder_Yellow: string = 'nsu=' + NS + ';i=58';
   static readonly TestObject_Red: string = 'nsu=' + NS + ';i=60';
   static readonly TestObject_Red_Yellow: string = 'nsu=' + NS + ';i=61';
   static readonly HeaterStatus_EnumStrings: string = 'nsu=' + NS + ';i=2';
   static readonly WithTwoDimensionalVariableType_X: string = 'nsu=' + NS + ';i=121';
   static readonly DemoModel_BinarySchema: string = 'nsu=' + NS + ';i=24';
   static readonly DemoModel_BinarySchema_NamespaceUri: string = 'nsu=' + NS + ';i=26';
   static readonly DemoModel_BinarySchema_Deprecated: string = 'nsu=' + NS + ';i=49';
   static readonly DemoModel_BinarySchema_Vector: string = 'nsu=' + NS + ';i=27';
   static readonly DemoModel_BinarySchema_WorkOrderStatusType: string = 'nsu=' + NS + ';i=30';
   static readonly DemoModel_BinarySchema_WorkOrderType: string = 'nsu=' + NS + ';i=33';
   static readonly DemoModel_BinarySchema_SampleUnion: string = 'nsu=' + NS + ';i=50';
   static readonly DemoModel_BinarySchema_SampleStructureWithOptionalFields: string = 'nsu=' + NS + ';i=53';
   static readonly DemoModel_BinarySchema_SampleUnionAllowSubtypes: string = 'nsu=' + NS + ';i=56';
   static readonly DemoModel_BinarySchema_SampleStructureAllowSubtypes: string = 'nsu=' + NS + ';i=59';
   static readonly DemoModel_XmlSchema: string = 'nsu=' + NS + ';i=9';
   static readonly DemoModel_XmlSchema_NamespaceUri: string = 'nsu=' + NS + ';i=11';
   static readonly DemoModel_XmlSchema_Deprecated: string = 'nsu=' + NS + ';i=66';
   static readonly DemoModel_XmlSchema_Vector: string = 'nsu=' + NS + ';i=12';
   static readonly DemoModel_XmlSchema_WorkOrderStatusType: string = 'nsu=' + NS + ';i=15';
   static readonly DemoModel_XmlSchema_WorkOrderType: string = 'nsu=' + NS + ';i=18';
   static readonly DemoModel_XmlSchema_SampleUnion: string = 'nsu=' + NS + ';i=67';
   static readonly DemoModel_XmlSchema_SampleStructureWithOptionalFields: string = 'nsu=' + NS + ';i=70';
   static readonly DemoModel_XmlSchema_SampleUnionAllowSubtypes: string = 'nsu=' + NS + ';i=73';
   static readonly DemoModel_XmlSchema_SampleStructureAllowSubtypes: string = 'nsu=' + NS + ';i=76';
}

class VariableTypeIds {
   static readonly RestrictedVariableType: string = 'nsu=' + NS + ';i=122';
}
