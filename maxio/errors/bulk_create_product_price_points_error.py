from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json

BulkCreateProductPricePointsErrorBody: TypeAlias = dict[str, Any] | RawError


@dataclass(frozen=True, slots=True)
class _BulkCreateProductPricePointsError:
    def map(self, response: HttpResponse) -> BulkCreateProductPricePointsErrorBody:
        match response.status_code:
            case 422:
                return decode_json[dict[str, Any]](response)
            case _:
                return RawError(response)


bulk_create_product_price_points_error_mapper: Final[
    ErrorMapper[BulkCreateProductPricePointsErrorBody]
] = _BulkCreateProductPricePointsError()
