from enum import Enum

class Namespaces(Enum):
     Uri = "urn:opcfoundation.org:2024-01:DemoModel"

class BrowseNames(Enum):
    Blue = "Blue"
    DemoModel_BinarySchema = "DemoModel"
    DemoModel_XmlSchema = "DemoModel"
    EnumUnderscoreTest = "EnumUnderscoreTest"
    HeaterStatus = "HeaterStatus"
    Person = "Person"
    Pink_Placeholder = "<Pink>"
    Red = "Red"
    RestrictedObjectType = "RestrictedObjectType"
    RestrictedVariableType = "RestrictedVariableType"
    SampleStructureAllowSubtypes = "SampleStructureAllowSubtypes"
    SampleStructureWithOptionalFields = "SampleStructureWithOptionalFields"
    SampleUnion = "SampleUnion"
    SampleUnionAllowSubtypes = "SampleUnionAllowSubtypes"
    Seeker = "Seeker"
    Student = "Student"
    Test_Error = "Test_Error"
    Test_ErrorComponent = "Test_ErrorComponent"
    TestObject = "TestObject"
    Vector = "Vector"
    WithTwoDimensionalVariableType = "WithTwoDimensionalVariableType"
    WorkOrderStatusType = "WorkOrderStatusType"
    WorkOrderType = "WorkOrderType"
    X = "X"
    Y = "Y"
    Yellow = "Yellow"
    Z = "Z"

class DataTypeIds(Enum):
    EnumUnderscoreTest = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=68"
    HeaterStatus = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=1"
    Vector = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=3"
    WorkOrderStatusType = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=4"
    WorkOrderType = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=5"
    SampleUnion = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=41"
    SampleStructureWithOptionalFields = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=42"
    SampleUnionAllowSubtypes = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=43"
    SampleStructureAllowSubtypes = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=44"
    Person = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=222"
    Student = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=223"

def get_DataTypeIds_name(value: str) -> str:
    try:
        return DataTypeIds(value).name
    except ValueError:
        return None


class MethodIds(Enum):
    RestrictedObjectType_Blue = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=127"
    TestObject_Blue = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=71"

def get_MethodIds_name(value: str) -> str:
    try:
        return MethodIds(value).name
    except ValueError:
        return None


class ObjectIds(Enum):
    Seeker = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=95"
    TestObject = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=128"
    Test_Error = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=93"
    Test_ErrorComponent = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=94"
    Vector_Encoding_DefaultBinary = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=21"
    WorkOrderStatusType_Encoding_DefaultBinary = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=22"
    WorkOrderType_Encoding_DefaultBinary = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=23"
    SampleUnion_Encoding_DefaultBinary = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=45"
    SampleStructureWithOptionalFields_Encoding_DefaultBinary = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=46"
    SampleUnionAllowSubtypes_Encoding_DefaultBinary = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=47"
    SampleStructureAllowSubtypes_Encoding_DefaultBinary = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=48"
    Person_Encoding_DefaultBinary = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=224"
    Student_Encoding_DefaultBinary = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=225"
    Vector_Encoding_DefaultXml = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=6"
    WorkOrderStatusType_Encoding_DefaultXml = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=7"
    WorkOrderType_Encoding_DefaultXml = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=8"
    SampleUnion_Encoding_DefaultXml = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=62"
    SampleStructureWithOptionalFields_Encoding_DefaultXml = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=63"
    SampleUnionAllowSubtypes_Encoding_DefaultXml = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=64"
    SampleStructureAllowSubtypes_Encoding_DefaultXml = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=65"
    Person_Encoding_DefaultXml = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=232"
    Student_Encoding_DefaultXml = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=233"
    Vector_Encoding_DefaultJson = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=79"
    WorkOrderStatusType_Encoding_DefaultJson = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=80"
    WorkOrderType_Encoding_DefaultJson = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=81"
    SampleUnion_Encoding_DefaultJson = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=82"
    SampleStructureWithOptionalFields_Encoding_DefaultJson = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=83"
    SampleUnionAllowSubtypes_Encoding_DefaultJson = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=84"
    SampleStructureAllowSubtypes_Encoding_DefaultJson = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=85"
    Person_Encoding_DefaultJson = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=240"
    Student_Encoding_DefaultJson = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=241"

def get_ObjectIds_name(value: str) -> str:
    try:
        return ObjectIds(value).name
    except ValueError:
        return None


class ObjectTypeIds(Enum):
    RestrictedObjectType = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=124"
    WithTwoDimensionalVariableType = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=120"

def get_ObjectTypeIds_name(value: str) -> str:
    try:
        return ObjectTypeIds(value).name
    except ValueError:
        return None


class VariableIds(Enum):
    Seeker_Identities = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=10"
    Seeker_AddIdentity_InputArguments = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=25"
    Seeker_RemoveIdentity_InputArguments = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=29"
    Seeker_AddApplication_InputArguments = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=32"
    Seeker_RemoveApplication_InputArguments = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=35"
    Seeker_AddEndpoint_InputArguments = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=52"
    Seeker_RemoveEndpoint_InputArguments = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=55"
    EnumUnderscoreTest_EnumValues = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=69"
    RestrictedVariableType_Yellow = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=123"
    RestrictedVariableType_X = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=210"
    RestrictedVariableType_Y = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=211"
    RestrictedVariableType_Z = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=212"
    RestrictedObjectType_Red = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=125"
    RestrictedObjectType_Red_Yellow = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=57"
    RestrictedObjectType_Red_X = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=213"
    RestrictedObjectType_Red_Y = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=214"
    RestrictedObjectType_Red_Z = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=215"
    RestrictedObjectType_Pink_Placeholder = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=132"
    RestrictedObjectType_Pink_Placeholder_Yellow = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=58"
    RestrictedObjectType_Pink_Placeholder_X = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=216"
    RestrictedObjectType_Pink_Placeholder_Y = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=217"
    RestrictedObjectType_Pink_Placeholder_Z = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=218"
    TestObject_Red = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=60"
    TestObject_Red_Yellow = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=61"
    TestObject_Red_X = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=219"
    TestObject_Red_Y = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=220"
    TestObject_Red_Z = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=221"
    HeaterStatus_EnumStrings = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=2"
    WithTwoDimensionalVariableType_X = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=121"
    DemoModel_BinarySchema = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=24"
    DemoModel_BinarySchema_NamespaceUri = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=26"
    DemoModel_BinarySchema_Deprecated = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=49"
    DemoModel_BinarySchema_Vector = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=27"
    DemoModel_BinarySchema_WorkOrderStatusType = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=30"
    DemoModel_BinarySchema_WorkOrderType = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=33"
    DemoModel_BinarySchema_SampleUnion = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=50"
    DemoModel_BinarySchema_SampleStructureWithOptionalFields = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=53"
    DemoModel_BinarySchema_SampleUnionAllowSubtypes = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=56"
    DemoModel_BinarySchema_SampleStructureAllowSubtypes = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=59"
    DemoModel_BinarySchema_Person = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=226"
    DemoModel_BinarySchema_Student = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=229"
    DemoModel_XmlSchema = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=9"
    DemoModel_XmlSchema_NamespaceUri = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=11"
    DemoModel_XmlSchema_Deprecated = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=66"
    DemoModel_XmlSchema_Vector = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=12"
    DemoModel_XmlSchema_WorkOrderStatusType = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=15"
    DemoModel_XmlSchema_WorkOrderType = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=18"
    DemoModel_XmlSchema_SampleUnion = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=67"
    DemoModel_XmlSchema_SampleStructureWithOptionalFields = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=70"
    DemoModel_XmlSchema_SampleUnionAllowSubtypes = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=73"
    DemoModel_XmlSchema_SampleStructureAllowSubtypes = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=76"
    DemoModel_XmlSchema_Person = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=234"
    DemoModel_XmlSchema_Student = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=237"

def get_VariableIds_name(value: str) -> str:
    try:
        return VariableIds(value).name
    except ValueError:
        return None


class VariableTypeIds(Enum):
    RestrictedVariableType = "nsu=urn:opcfoundation.org:2024-01:DemoModel;i=122"

def get_VariableTypeIds_name(value: str) -> str:
    try:
        return VariableTypeIds(value).name
    except ValueError:
        return None

