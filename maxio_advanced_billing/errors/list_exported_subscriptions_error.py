from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ListExportedSubscriptionsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListExportedSubscriptionsError:
    def map(self, response: HttpResponse) -> ListExportedSubscriptionsErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


list_exported_subscriptions_error_mapper: Final[
    ErrorMapper[ListExportedSubscriptionsErrorBody]
] = _ListExportedSubscriptionsError()
