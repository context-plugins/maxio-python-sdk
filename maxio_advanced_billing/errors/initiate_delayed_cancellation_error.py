from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

InitiateDelayedCancellationErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _InitiateDelayedCancellationError:
    def map(self, response: HttpResponse) -> InitiateDelayedCancellationErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


initiate_delayed_cancellation_error_mapper: Final[
    ErrorMapper[InitiateDelayedCancellationErrorBody]
] = _InitiateDelayedCancellationError()
