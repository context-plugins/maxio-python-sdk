from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.event_based_billing_segment_errors1 import EventBasedBillingSegmentErrors1

CreateSegmentErrorBody: TypeAlias = EventBasedBillingSegmentErrors1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateSegmentError:
    def map(self, response: HttpResponse) -> CreateSegmentErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[EventBasedBillingSegmentErrors1](response)
            case _:
                return RawError(response)


create_segment_error_mapper: Final[ErrorMapper[CreateSegmentErrorBody]] = _CreateSegmentError()
