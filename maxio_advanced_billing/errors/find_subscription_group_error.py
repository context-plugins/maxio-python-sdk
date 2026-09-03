from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

FindSubscriptionGroupErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _FindSubscriptionGroupError:
    def map(self, response: HttpResponse) -> FindSubscriptionGroupErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


find_subscription_group_error_mapper: Final[ErrorMapper[FindSubscriptionGroupErrorBody]] = _FindSubscriptionGroupError()
