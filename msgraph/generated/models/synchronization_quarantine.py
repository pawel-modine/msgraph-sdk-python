from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .quarantine_reason import QuarantineReason
    from .synchronization_error import SynchronizationError

@dataclass
class SynchronizationQuarantine(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The currentBegan property
    current_began: Optional[datetime.datetime] = None
    # The error property
    error: Optional[SynchronizationError] = None
    # The nextAttempt property
    next_attempt: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reason property
    reason: Optional[QuarantineReason] = None
    # The seriesBegan property
    series_began: Optional[datetime.datetime] = None
    # The seriesCount property
    series_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationQuarantine:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationQuarantine
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationQuarantine()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .quarantine_reason import QuarantineReason
        from .synchronization_error import SynchronizationError

        from .quarantine_reason import QuarantineReason
        from .synchronization_error import SynchronizationError

        fields: Dict[str, Callable[[Any], None]] = {
            "currentBegan": lambda n : setattr(self, 'current_began', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(SynchronizationError)),
            "nextAttempt": lambda n : setattr(self, 'next_attempt', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_enum_value(QuarantineReason)),
            "seriesBegan": lambda n : setattr(self, 'series_began', n.get_datetime_value()),
            "seriesCount": lambda n : setattr(self, 'series_count', n.get_int_value()),
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
        writer.write_datetime_value()("currentBegan", self.current_began)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value()("nextAttempt", self.next_attempt)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("reason", self.reason)
        writer.write_datetime_value()("seriesBegan", self.series_began)
        writer.write_int_value("seriesCount", self.series_count)
        writer.write_additional_data_value(self.additional_data)
    
