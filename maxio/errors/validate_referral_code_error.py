from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.single_string_error_response1 import SingleStringErrorResponse1

ValidateReferralCodeErrorBody: TypeAlias = SingleStringErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ValidateReferralCodeError:
    def map(self, response: HttpResponse) -> ValidateReferralCodeErrorBody:
        match response.status_code:
            case 404:
                return decode_json[SingleStringErrorResponse1](response)
            case _:
                return RawError(response)


validate_referral_code_error_mapper: Final[ErrorMapper[ValidateReferralCodeErrorBody]] = _ValidateReferralCodeError()
