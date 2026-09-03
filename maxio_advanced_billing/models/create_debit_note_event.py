from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .debit_note import DebitNote, DebitNoteDict
from .enums.invoice_event_type import InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict


class CreateDebitNoteEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr
    event_data: DebitNote
    """Example schema for an ``create_debit_note`` event"""


class CreateDebitNoteEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice | InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: DebitNote | DebitNoteDict
