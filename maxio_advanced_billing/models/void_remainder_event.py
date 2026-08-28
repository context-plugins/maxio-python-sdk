from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.invoice_event_type import InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict
from .void_remainder_event_data import VoidRemainderEventData, VoidRemainderEventDataDict


class VoidRemainderEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr
    event_data: VoidRemainderEventData
    """Example schema for an ``void_remainder`` event"""


class VoidRemainderEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice | InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: VoidRemainderEventData | VoidRemainderEventDataDict
