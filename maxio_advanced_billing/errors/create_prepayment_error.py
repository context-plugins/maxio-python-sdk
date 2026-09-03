from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unions.create_prepayment_error_response import CreatePrepaymentErrorResponse

CreatePrepaymentErrorBody: TypeAlias = CreatePrepaymentErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _CreatePrepaymentError:
    def map(self, response: HttpResponse) -> CreatePrepaymentErrorBody:
        match response.status_code:
            case 422:
                return decode_json[CreatePrepaymentErrorResponse](response)
            case _:
                return RawError(response)


create_prepayment_error_mapper: Final[ErrorMapper[CreatePrepaymentErrorBody]] = _CreatePrepaymentError()
