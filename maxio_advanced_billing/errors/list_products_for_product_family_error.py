from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json

ListProductsForProductFamilyErrorBody: TypeAlias = str | RawError


@dataclass(frozen=True, slots=True)
class _ListProductsForProductFamilyError:
    def map(self, response: HttpResponse) -> ListProductsForProductFamilyErrorBody:
        match response.status_code:
            case 404:
                return decode_json[str](response)
            case _:
                return RawError(response)


list_products_for_product_family_error_mapper: Final[
    ErrorMapper[ListProductsForProductFamilyErrorBody]
] = _ListProductsForProductFamilyError()
