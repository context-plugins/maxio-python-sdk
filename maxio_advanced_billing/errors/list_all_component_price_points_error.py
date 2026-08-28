from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

ListAllComponentPricePointsErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ListAllComponentPricePointsError:
    def map(self, response: HttpResponse) -> ListAllComponentPricePointsErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


list_all_component_price_points_error_mapper: Final[
    ErrorMapper[ListAllComponentPricePointsErrorBody]
] = _ListAllComponentPricePointsError()
