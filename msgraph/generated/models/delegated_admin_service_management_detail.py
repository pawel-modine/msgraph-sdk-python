from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class DelegatedAdminServiceManagementDetail(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new delegatedAdminServiceManagementDetail and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The serviceManagementUrl property
        self._service_management_url: Optional[str] = None
        # The serviceName property
        self._service_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DelegatedAdminServiceManagementDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminServiceManagementDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DelegatedAdminServiceManagementDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "service_management_url": lambda n : setattr(self, 'service_management_url', n.get_str_value()),
            "service_name": lambda n : setattr(self, 'service_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("serviceManagementUrl", self.service_management_url)
        writer.write_str_value("serviceName", self.service_name)
    
    @property
    def service_management_url(self,) -> Optional[str]:
        """
        Gets the serviceManagementUrl property value. The serviceManagementUrl property
        Returns: Optional[str]
        """
        return self._service_management_url
    
    @service_management_url.setter
    def service_management_url(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceManagementUrl property value. The serviceManagementUrl property
        Args:
            value: Value to set for the serviceManagementUrl property.
        """
        self._service_management_url = value
    
    @property
    def service_name(self,) -> Optional[str]:
        """
        Gets the serviceName property value. The serviceName property
        Returns: Optional[str]
        """
        return self._service_name
    
    @service_name.setter
    def service_name(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceName property value. The serviceName property
        Args:
            value: Value to set for the serviceName property.
        """
        self._service_name = value
    

