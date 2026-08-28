from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ReadProformaInvoicesExportErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadProformaInvoicesExportError:
    def map(self, response: HttpResponse) -> ReadProformaInvoicesExportErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


read_proforma_invoices_export_error_mapper: Final[
    ErrorMapper[ReadProformaInvoicesExportErrorBody]
] = _ReadProformaInvoicesExportError()
