from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ListExportedProformaInvoicesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListExportedProformaInvoicesError:
    def map(self, response: HttpResponse) -> ListExportedProformaInvoicesErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


list_exported_proforma_invoices_error_mapper: Final[
    ErrorMapper[ListExportedProformaInvoicesErrorBody]
] = _ListExportedProformaInvoicesError()
