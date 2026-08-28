from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_array_map_response1 import ErrorArrayMapResponse1

ActivateSubscriptionErrorBody: TypeAlias = ErrorArrayMapResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ActivateSubscriptionError:
    def map(self, response: HttpResponse) -> ActivateSubscriptionErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ErrorArrayMapResponse1](response)
            case _:
                return RawError(response)


activate_subscription_error_mapper: Final[ErrorMapper[ActivateSubscriptionErrorBody]] = _ActivateSubscriptionError()
