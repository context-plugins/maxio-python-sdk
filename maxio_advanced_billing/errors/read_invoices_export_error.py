from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ReadInvoicesExportErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadInvoicesExportError:
    def map(self, response: HttpResponse) -> ReadInvoicesExportErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


read_invoices_export_error_mapper: Final[ErrorMapper[ReadInvoicesExportErrorBody]] = _ReadInvoicesExportError()
