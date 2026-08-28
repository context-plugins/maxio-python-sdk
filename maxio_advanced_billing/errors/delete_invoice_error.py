from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

DeleteInvoiceErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _DeleteInvoiceError:
    def map(self, response: HttpResponse) -> DeleteInvoiceErrorBody:
        match response.status_code:
            case 404 | 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


delete_invoice_error_mapper: Final[ErrorMapper[DeleteInvoiceErrorBody]] = _DeleteInvoiceError()
