from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..apply_credit_note_event import ApplyCreditNoteEvent, ApplyCreditNoteEventDict
from ..apply_debit_note_event import ApplyDebitNoteEvent, ApplyDebitNoteEventDict
from ..apply_payment_event import ApplyPaymentEvent, ApplyPaymentEventDict
from ..backport_invoice_event import BackportInvoiceEvent, BackportInvoiceEventDict
from ..change_chargeback_status_event import ChangeChargebackStatusEvent, ChangeChargebackStatusEventDict
from ..change_invoice_collection_method_event import (
    ChangeInvoiceCollectionMethodEvent,
    ChangeInvoiceCollectionMethodEventDict,
)
from ..change_invoice_status_event import ChangeInvoiceStatusEvent, ChangeInvoiceStatusEventDict
from ..create_credit_note_event import CreateCreditNoteEvent, CreateCreditNoteEventDict
from ..create_debit_note_event import CreateDebitNoteEvent, CreateDebitNoteEventDict
from ..failed_payment_event import FailedPaymentEvent, FailedPaymentEventDict
from ..issue_invoice_event import IssueInvoiceEvent, IssueInvoiceEventDict
from ..refund_invoice_event import RefundInvoiceEvent, RefundInvoiceEventDict
from ..remove_payment_event import RemovePaymentEvent, RemovePaymentEventDict
from ..void_invoice_event import VoidInvoiceEvent, VoidInvoiceEventDict
from ..void_remainder_event import VoidRemainderEvent, VoidRemainderEventDict

InvoiceEvent1: TypeAlias = Annotated[
    (
        ApplyCreditNoteEvent
        | ApplyDebitNoteEvent
        | ApplyPaymentEvent
        | BackportInvoiceEvent
        | ChangeChargebackStatusEvent
        | ChangeInvoiceCollectionMethodEvent
        | ChangeInvoiceStatusEvent
        | CreateCreditNoteEvent
        | CreateDebitNoteEvent
        | FailedPaymentEvent
        | IssueInvoiceEvent
        | RefundInvoiceEvent
        | RemovePaymentEvent
        | VoidInvoiceEvent
        | VoidRemainderEvent
    ),
    Field(discriminator="event_type"),
]

InvoiceEvent1Dict: TypeAlias = (
    ApplyCreditNoteEventDict
    | ApplyDebitNoteEventDict
    | ApplyPaymentEventDict
    | BackportInvoiceEventDict
    | ChangeChargebackStatusEventDict
    | ChangeInvoiceCollectionMethodEventDict
    | ChangeInvoiceStatusEventDict
    | CreateCreditNoteEventDict
    | CreateDebitNoteEventDict
    | FailedPaymentEventDict
    | IssueInvoiceEventDict
    | RefundInvoiceEventDict
    | RemovePaymentEventDict
    | VoidInvoiceEventDict
    | VoidRemainderEventDict
)
