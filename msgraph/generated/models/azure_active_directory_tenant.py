from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_source import IdentitySource

from .identity_source import IdentitySource

@dataclass
class AzureActiveDirectoryTenant(IdentitySource):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.azureActiveDirectoryTenant"
    # The name of the Azure Active Directory tenant. Read only.
    display_name: Optional[str] = None
    # The ID of the Azure Active Directory tenant. Read only.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureActiveDirectoryTenant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureActiveDirectoryTenant
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AzureActiveDirectoryTenant()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity_source import IdentitySource

        from .identity_source import IdentitySource

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("tenantId", self.tenant_id)
    

