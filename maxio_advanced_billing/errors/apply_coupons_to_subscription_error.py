from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_add_coupon_error1 import SubscriptionAddCouponError1

ApplyCouponsToSubscriptionErrorBody: TypeAlias = SubscriptionAddCouponError1 | RawError


@dataclass(frozen=True, slots=True)
class _ApplyCouponsToSubscriptionError:
    def map(self, response: HttpResponse) -> ApplyCouponsToSubscriptionErrorBody:
        match response.status_code:
            case 422:
                return decode_json[SubscriptionAddCouponError1](response)
            case _:
                return RawError(response)


apply_coupons_to_subscription_error_mapper: Final[
    ErrorMapper[ApplyCouponsToSubscriptionErrorBody]
] = _ApplyCouponsToSubscriptionError()
