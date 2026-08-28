from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ReadProformaInvoiceErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadProformaInvoiceError:
    def map(self, response: HttpResponse) -> ReadProformaInvoiceErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


read_proforma_invoice_error_mapper: Final[ErrorMapper[ReadProformaInvoiceErrorBody]] = _ReadProformaInvoiceError()
