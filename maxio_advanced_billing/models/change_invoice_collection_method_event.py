from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .change_invoice_collection_method_event_data import (
    ChangeInvoiceCollectionMethodEventData,
    ChangeInvoiceCollectionMethodEventDataDict,
)
from .enums.invoice_event_type import InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict


class ChangeInvoiceCollectionMethodEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr
    event_data: ChangeInvoiceCollectionMethodEventData
    """Example schema for an ``change_invoice_collection_method`` event"""


class ChangeInvoiceCollectionMethodEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice | InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: ChangeInvoiceCollectionMethodEventData | ChangeInvoiceCollectionMethodEventDataDict
