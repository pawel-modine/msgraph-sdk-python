from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class GetAvailableExtensionPropertiesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the getAvailableExtensionProperties method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value

    def __init__(self,) -> None:
        """
        Instantiates a new getAvailableExtensionPropertiesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The isSyncedFromOnPremises property
        self._is_synced_from_on_premises: Optional[bool] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetAvailableExtensionPropertiesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetAvailableExtensionPropertiesPostRequestBody
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return GetAvailableExtensionPropertiesPostRequestBody()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_synced_from_on_premises": lambda n : setattr(self, 'is_synced_from_on_premises', n.get_bool_value()),
        }
        return fields

    @property
    def is_synced_from_on_premises(self,) -> Optional[bool]:
        """
        Gets the isSyncedFromOnPremises property value. The isSyncedFromOnPremises property
        Returns: Optional[bool]
        """
        return self._is_synced_from_on_premises

    @is_synced_from_on_premises.setter
    def is_synced_from_on_premises(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSyncedFromOnPremises property value. The isSyncedFromOnPremises property
        Args:
            value: Value to set for the isSyncedFromOnPremises property.
        """
        self._is_synced_from_on_premises = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isSyncedFromOnPremises", self.is_synced_from_on_premises)
        writer.write_additional_data_value(self.additional_data)

