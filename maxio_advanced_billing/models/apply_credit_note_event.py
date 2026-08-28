from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .apply_credit_note_event_data import ApplyCreditNoteEventData, ApplyCreditNoteEventDataDict
from .enums.invoice_event_type import InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict


class ApplyCreditNoteEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr
    event_data: ApplyCreditNoteEventData
    """Example schema for an ``apply_credit_note`` event"""


class ApplyCreditNoteEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice | InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: ApplyCreditNoteEventData | ApplyCreditNoteEventDataDict
