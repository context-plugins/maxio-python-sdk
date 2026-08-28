from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ReadReasonCodeErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadReasonCodeError:
    def map(self, response: HttpResponse) -> ReadReasonCodeErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


read_reason_code_error_mapper: Final[ErrorMapper[ReadReasonCodeErrorBody]] = _ReadReasonCodeError()
