from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteSubscriptionGroupErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteSubscriptionGroupError:
    def map(self, response: HttpResponse) -> DeleteSubscriptionGroupErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


delete_subscription_group_error_mapper: Final[
    ErrorMapper[DeleteSubscriptionGroupErrorBody]
] = _DeleteSubscriptionGroupError()
