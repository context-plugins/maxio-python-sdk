from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteReasonCodeErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteReasonCodeError:
    def map(self, response: HttpResponse) -> DeleteReasonCodeErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


delete_reason_code_error_mapper: Final[ErrorMapper[DeleteReasonCodeErrorBody]] = _DeleteReasonCodeError()
