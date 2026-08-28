from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteCouponSubcodeErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteCouponSubcodeError:
    def map(self, response: HttpResponse) -> DeleteCouponSubcodeErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


delete_coupon_subcode_error_mapper: Final[ErrorMapper[DeleteCouponSubcodeErrorBody]] = _DeleteCouponSubcodeError()
