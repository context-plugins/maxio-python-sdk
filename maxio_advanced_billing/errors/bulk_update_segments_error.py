from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.event_based_billing_segment1 import EventBasedBillingSegment1

BulkUpdateSegmentsErrorBody: TypeAlias = EventBasedBillingSegment1 | RawError


@dataclass(frozen=True, slots=True)
class _BulkUpdateSegmentsError:
    def map(self, response: HttpResponse) -> BulkUpdateSegmentsErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[EventBasedBillingSegment1](response)
            case _:
                return RawError(response)


bulk_update_segments_error_mapper: Final[ErrorMapper[BulkUpdateSegmentsErrorBody]] = _BulkUpdateSegmentsError()
