from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_remove_coupon_errors1 import SubscriptionRemoveCouponErrors1

RemoveCouponFromSubscriptionErrorBody: TypeAlias = SubscriptionRemoveCouponErrors1 | RawError


@dataclass(frozen=True, slots=True)
class _RemoveCouponFromSubscriptionError:
    def map(self, response: HttpResponse) -> RemoveCouponFromSubscriptionErrorBody:
        match response.status_code:
            case 422:
                return decode_json[SubscriptionRemoveCouponErrors1](response)
            case _:
                return RawError(response)


remove_coupon_from_subscription_error_mapper: Final[
    ErrorMapper[RemoveCouponFromSubscriptionErrorBody]
] = _RemoveCouponFromSubscriptionError()
