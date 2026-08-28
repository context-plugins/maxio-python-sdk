from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_string_map_response1 import ErrorStringMapResponse1

CreateOrUpdateCouponCurrencyPricesErrorBody: TypeAlias = ErrorStringMapResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateOrUpdateCouponCurrencyPricesError:
    def map(self, response: HttpResponse) -> CreateOrUpdateCouponCurrencyPricesErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ErrorStringMapResponse1](response)
            case _:
                return RawError(response)


create_or_update_coupon_currency_prices_error_mapper: Final[
    ErrorMapper[CreateOrUpdateCouponCurrencyPricesErrorBody]
] = _CreateOrUpdateCouponCurrencyPricesError()
