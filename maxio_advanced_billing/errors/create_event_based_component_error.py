from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

CreateEventBasedComponentErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateEventBasedComponentError:
    def map(self, response: HttpResponse) -> CreateEventBasedComponentErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


create_event_based_component_error_mapper: Final[
    ErrorMapper[CreateEventBasedComponentErrorBody]
] = _CreateEventBasedComponentError()
