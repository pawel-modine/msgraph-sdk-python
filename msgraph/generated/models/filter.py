from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_group import FilterGroup

@dataclass
class Filter(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The categoryFilterGroups property
    category_filter_groups: Optional[List[FilterGroup]] = None
    # The groups property
    groups: Optional[List[FilterGroup]] = None
    # The inputFilterGroups property
    input_filter_groups: Optional[List[FilterGroup]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Filter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Filter
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Filter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .filter_group import FilterGroup

        from .filter_group import FilterGroup

        fields: Dict[str, Callable[[Any], None]] = {
            "categoryFilterGroups": lambda n : setattr(self, 'category_filter_groups', n.get_collection_of_object_values(FilterGroup)),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(FilterGroup)),
            "inputFilterGroups": lambda n : setattr(self, 'input_filter_groups', n.get_collection_of_object_values(FilterGroup)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("categoryFilterGroups", self.category_filter_groups)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_collection_of_object_values("inputFilterGroups", self.input_filter_groups)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    
