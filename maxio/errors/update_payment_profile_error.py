from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_string_map_response1 import ErrorStringMapResponse1

UpdatePaymentProfileErrorBody: TypeAlias = ErrorStringMapResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdatePaymentProfileError:
    def map(self, response: HttpResponse) -> UpdatePaymentProfileErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[ErrorStringMapResponse1](response)
            case _:
                return RawError(response)


update_payment_profile_error_mapper: Final[ErrorMapper[UpdatePaymentProfileErrorBody]] = _UpdatePaymentProfileError()
