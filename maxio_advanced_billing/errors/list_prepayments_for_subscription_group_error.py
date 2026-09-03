from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ListPrepaymentsForSubscriptionGroupErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListPrepaymentsForSubscriptionGroupError:
    def map(self, response: HttpResponse) -> ListPrepaymentsForSubscriptionGroupErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


list_prepayments_for_subscription_group_error_mapper: Final[
    ErrorMapper[ListPrepaymentsForSubscriptionGroupErrorBody]
] = _ListPrepaymentsForSubscriptionGroupError()
