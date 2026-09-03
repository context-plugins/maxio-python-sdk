from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ListExportedInvoicesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListExportedInvoicesError:
    def map(self, response: HttpResponse) -> ListExportedInvoicesErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


list_exported_invoices_error_mapper: Final[ErrorMapper[ListExportedInvoicesErrorBody]] = _ListExportedInvoicesError()
