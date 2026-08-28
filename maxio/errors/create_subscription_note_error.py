from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

CreateSubscriptionNoteErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateSubscriptionNoteError:
    def map(self, response: HttpResponse) -> CreateSubscriptionNoteErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


create_subscription_note_error_mapper: Final[
    ErrorMapper[CreateSubscriptionNoteErrorBody]
] = _CreateSubscriptionNoteError()
