from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ReadPaymentProfileErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadPaymentProfileError:
    def map(self, response: HttpResponse) -> ReadPaymentProfileErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


read_payment_profile_error_mapper: Final[ErrorMapper[ReadPaymentProfileErrorBody]] = _ReadPaymentProfileError()
