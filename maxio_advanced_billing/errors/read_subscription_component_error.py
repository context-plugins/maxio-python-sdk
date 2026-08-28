from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ReadSubscriptionComponentErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadSubscriptionComponentError:
    def map(self, response: HttpResponse) -> ReadSubscriptionComponentErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


read_subscription_component_error_mapper: Final[
    ErrorMapper[ReadSubscriptionComponentErrorBody]
] = _ReadSubscriptionComponentError()
