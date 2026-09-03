from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteSegmentErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteSegmentError:
    def map(self, response: HttpResponse) -> DeleteSegmentErrorBody:
        match response.status_code:
            case 404 | 422:
                return RawError(response)
            case _:
                return RawError(response)


delete_segment_error_mapper: Final[ErrorMapper[DeleteSegmentErrorBody]] = _DeleteSegmentError()
