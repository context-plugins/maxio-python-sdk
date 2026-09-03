from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

FindSubscriptionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _FindSubscriptionError:
    def map(self, response: HttpResponse) -> FindSubscriptionErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


find_subscription_error_mapper: Final[ErrorMapper[FindSubscriptionErrorBody]] = _FindSubscriptionError()
