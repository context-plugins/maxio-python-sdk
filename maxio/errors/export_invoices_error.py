from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.single_error_response1 import SingleErrorResponse1

ExportInvoicesErrorBody: TypeAlias = SingleErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ExportInvoicesError:
    def map(self, response: HttpResponse) -> ExportInvoicesErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 409:
                return decode_json[SingleErrorResponse1](response)
            case _:
                return RawError(response)


export_invoices_error_mapper: Final[ErrorMapper[ExportInvoicesErrorBody]] = _ExportInvoicesError()
