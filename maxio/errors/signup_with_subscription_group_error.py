from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_group_signup_error_response1 import SubscriptionGroupSignupErrorResponse1

SignupWithSubscriptionGroupErrorBody: TypeAlias = SubscriptionGroupSignupErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _SignupWithSubscriptionGroupError:
    def map(self, response: HttpResponse) -> SignupWithSubscriptionGroupErrorBody:
        match response.status_code:
            case 422:
                return decode_json[SubscriptionGroupSignupErrorResponse1](response)
            case _:
                return RawError(response)


signup_with_subscription_group_error_mapper: Final[
    ErrorMapper[SignupWithSubscriptionGroupErrorBody]
] = _SignupWithSubscriptionGroupError()
