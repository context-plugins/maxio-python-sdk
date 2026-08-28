from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

CancelDelayedCancellationErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _CancelDelayedCancellationError:
    def map(self, response: HttpResponse) -> CancelDelayedCancellationErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


cancel_delayed_cancellation_error_mapper: Final[
    ErrorMapper[CancelDelayedCancellationErrorBody]
] = _CancelDelayedCancellationError()
