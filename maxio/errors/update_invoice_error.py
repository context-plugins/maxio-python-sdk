from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_array_map_response1 import ErrorArrayMapResponse1
from ..models.error_list_response1 import ErrorListResponse1

UpdateInvoiceErrorBody: TypeAlias = ErrorListResponse1 | ErrorArrayMapResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateInvoiceError:
    def map(self, response: HttpResponse) -> UpdateInvoiceErrorBody:
        match response.status_code:
            case 404:
                return decode_json[ErrorListResponse1](response)
            case 422:
                return decode_json[ErrorArrayMapResponse1](response)
            case _:
                return RawError(response)


update_invoice_error_mapper: Final[ErrorMapper[UpdateInvoiceErrorBody]] = _UpdateInvoiceError()
