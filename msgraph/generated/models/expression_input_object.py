from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .object_definition import ObjectDefinition
    from .string_key_object_value_pair import StringKeyObjectValuePair

@dataclass
class ExpressionInputObject(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The definition property
    definition: Optional[ObjectDefinition] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The properties property
    properties: Optional[List[StringKeyObjectValuePair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExpressionInputObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExpressionInputObject
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ExpressionInputObject()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .object_definition import ObjectDefinition
        from .string_key_object_value_pair import StringKeyObjectValuePair

        from .object_definition import ObjectDefinition
        from .string_key_object_value_pair import StringKeyObjectValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(ObjectDefinition)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(StringKeyObjectValuePair)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("definition", self.definition)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("properties", self.properties)
        writer.write_additional_data_value(self.additional_data)
    
