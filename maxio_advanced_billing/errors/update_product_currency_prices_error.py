from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_array_map_response1 import ErrorArrayMapResponse1

UpdateProductCurrencyPricesErrorBody: TypeAlias = ErrorArrayMapResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateProductCurrencyPricesError:
    def map(self, response: HttpResponse) -> UpdateProductCurrencyPricesErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ErrorArrayMapResponse1](response)
            case _:
                return RawError(response)


update_product_currency_prices_error_mapper: Final[
    ErrorMapper[UpdateProductCurrencyPricesErrorBody]
] = _UpdateProductCurrencyPricesError()
