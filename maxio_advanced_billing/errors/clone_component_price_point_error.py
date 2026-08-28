from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

CloneComponentPricePointErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CloneComponentPricePointError:
    def map(self, response: HttpResponse) -> CloneComponentPricePointErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


clone_component_price_point_error_mapper: Final[
    ErrorMapper[CloneComponentPricePointErrorBody]
] = _CloneComponentPricePointError()
