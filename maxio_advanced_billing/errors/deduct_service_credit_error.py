from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unions.deduct_service_credit_error_response import DeductServiceCreditErrorResponse

DeductServiceCreditErrorBody: TypeAlias = DeductServiceCreditErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _DeductServiceCreditError:
    def map(self, response: HttpResponse) -> DeductServiceCreditErrorBody:
        match response.status_code:
            case 422:
                return decode_json[DeductServiceCreditErrorResponse](response)
            case _:
                return RawError(response)


deduct_service_credit_error_mapper: Final[ErrorMapper[DeductServiceCreditErrorBody]] = _DeductServiceCreditError()
