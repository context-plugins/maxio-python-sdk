from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.single_error_response1 import SingleErrorResponse1

UpdateMetafieldErrorBody: TypeAlias = SingleErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateMetafieldError:
    def map(self, response: HttpResponse) -> UpdateMetafieldErrorBody:
        match response.status_code:
            case 422:
                return decode_json[SingleErrorResponse1](response)
            case _:
                return RawError(response)


update_metafield_error_mapper: Final[ErrorMapper[UpdateMetafieldErrorBody]] = _UpdateMetafieldError()
