from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ListSubscriptionGroupProformaInvoicesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListSubscriptionGroupProformaInvoicesError:
    def map(self, response: HttpResponse) -> ListSubscriptionGroupProformaInvoicesErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


list_subscription_group_proforma_invoices_error_mapper: Final[
    ErrorMapper[ListSubscriptionGroupProformaInvoicesErrorBody]
] = _ListSubscriptionGroupProformaInvoicesError()
