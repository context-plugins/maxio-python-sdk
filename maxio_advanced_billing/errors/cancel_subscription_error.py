from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unions.cancel_subscription_error_response import CancelSubscriptionErrorResponse

CancelSubscriptionErrorBody: TypeAlias = CancelSubscriptionErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _CancelSubscriptionError:
    def map(self, response: HttpResponse) -> CancelSubscriptionErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[CancelSubscriptionErrorResponse](response)
            case _:
                return RawError(response)


cancel_subscription_error_mapper: Final[ErrorMapper[CancelSubscriptionErrorBody]] = _CancelSubscriptionError()
