from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.event_based_billing_segment1 import EventBasedBillingSegment1

BulkCreateSegmentsErrorBody: TypeAlias = EventBasedBillingSegment1 | RawError


@dataclass(frozen=True, slots=True)
class _BulkCreateSegmentsError:
    def map(self, response: HttpResponse) -> BulkCreateSegmentsErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[EventBasedBillingSegment1](response)
            case _:
                return RawError(response)


bulk_create_segments_error_mapper: Final[ErrorMapper[BulkCreateSegmentsErrorBody]] = _BulkCreateSegmentsError()
