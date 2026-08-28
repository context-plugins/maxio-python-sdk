from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

VoidAdvanceInvoiceErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _VoidAdvanceInvoiceError:
    def map(self, response: HttpResponse) -> VoidAdvanceInvoiceErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


void_advance_invoice_error_mapper: Final[ErrorMapper[VoidAdvanceInvoiceErrorBody]] = _VoidAdvanceInvoiceError()
