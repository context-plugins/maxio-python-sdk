from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

RecordPaymentForMultipleInvoicesErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _RecordPaymentForMultipleInvoicesError:
    def map(self, response: HttpResponse) -> RecordPaymentForMultipleInvoicesErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


record_payment_for_multiple_invoices_error_mapper: Final[
    ErrorMapper[RecordPaymentForMultipleInvoicesErrorBody]
] = _RecordPaymentForMultipleInvoicesError()
