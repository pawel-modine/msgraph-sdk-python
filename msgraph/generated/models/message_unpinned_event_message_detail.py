from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .event_message_detail import EventMessageDetail
    from .identity_set import IdentitySet

from .event_message_detail import EventMessageDetail

@dataclass
class MessageUnpinnedEventMessageDetail(EventMessageDetail):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.messageUnpinnedEventMessageDetail"
    # Date and time when the event occurred.
    event_date_time: Optional[datetime.datetime] = None
    # Initiator of the event.
    initiator: Optional[IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MessageUnpinnedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MessageUnpinnedEventMessageDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MessageUnpinnedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet

        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(IdentitySet)),
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
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_object_value("initiator", self.initiator)
    

