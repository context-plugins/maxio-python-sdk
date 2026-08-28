from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.product_price_point_error_response1 import ProductPricePointErrorResponse1

CreateProductPricePointErrorBody: TypeAlias = ProductPricePointErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateProductPricePointError:
    def map(self, response: HttpResponse) -> CreateProductPricePointErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ProductPricePointErrorResponse1](response)
            case _:
                return RawError(response)


create_product_price_point_error_mapper: Final[
    ErrorMapper[CreateProductPricePointErrorBody]
] = _CreateProductPricePointError()
