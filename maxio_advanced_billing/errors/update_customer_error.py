from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.customer_error_response1 import CustomerErrorResponse1

UpdateCustomerErrorBody: TypeAlias = CustomerErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateCustomerError:
    def map(self, response: HttpResponse) -> UpdateCustomerErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[CustomerErrorResponse1](response)
            case _:
                return RawError(response)


update_customer_error_mapper: Final[ErrorMapper[UpdateCustomerErrorBody]] = _UpdateCustomerError()
