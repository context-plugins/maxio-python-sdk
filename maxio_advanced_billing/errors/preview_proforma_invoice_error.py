from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

PreviewProformaInvoiceErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _PreviewProformaInvoiceError:
    def map(self, response: HttpResponse) -> PreviewProformaInvoiceErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


preview_proforma_invoice_error_mapper: Final[
    ErrorMapper[PreviewProformaInvoiceErrorBody]
] = _PreviewProformaInvoiceError()
