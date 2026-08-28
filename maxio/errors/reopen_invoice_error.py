from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

ReopenInvoiceErrorBody: TypeAlias = Any | None | ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ReopenInvoiceError:
    def map(self, response: HttpResponse) -> ReopenInvoiceErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Any | None](response)
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


reopen_invoice_error_mapper: Final[ErrorMapper[ReopenInvoiceErrorBody]] = _ReopenInvoiceError()
