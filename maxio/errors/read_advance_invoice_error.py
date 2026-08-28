from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ReadAdvanceInvoiceErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadAdvanceInvoiceError:
    def map(self, response: HttpResponse) -> ReadAdvanceInvoiceErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


read_advance_invoice_error_mapper: Final[ErrorMapper[ReadAdvanceInvoiceErrorBody]] = _ReadAdvanceInvoiceError()
