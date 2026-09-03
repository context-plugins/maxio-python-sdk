from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

RecordPaymentForSubscriptionErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _RecordPaymentForSubscriptionError:
    def map(self, response: HttpResponse) -> RecordPaymentForSubscriptionErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


record_payment_for_subscription_error_mapper: Final[
    ErrorMapper[RecordPaymentForSubscriptionErrorBody]
] = _RecordPaymentForSubscriptionError()
