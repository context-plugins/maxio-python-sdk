from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.event_based_billing_segment_errors1 import EventBasedBillingSegmentErrors1

UpdateSegmentErrorBody: TypeAlias = EventBasedBillingSegmentErrors1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateSegmentError:
    def map(self, response: HttpResponse) -> UpdateSegmentErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[EventBasedBillingSegmentErrors1](response)
            case _:
                return RawError(response)


update_segment_error_mapper: Final[ErrorMapper[UpdateSegmentErrorBody]] = _UpdateSegmentError()
