from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_response import SubscriptionResponse

PurgeSubscriptionErrorBody: TypeAlias = SubscriptionResponse | RawError


@dataclass(frozen=True, slots=True)
class _PurgeSubscriptionError:
    def map(self, response: HttpResponse) -> PurgeSubscriptionErrorBody:
        match response.status_code:
            case 400:
                return decode_json[SubscriptionResponse](response)
            case _:
                return RawError(response)


purge_subscription_error_mapper: Final[ErrorMapper[PurgeSubscriptionErrorBody]] = _PurgeSubscriptionError()
