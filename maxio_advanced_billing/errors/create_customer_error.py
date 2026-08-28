from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.customer_error_response1 import CustomerErrorResponse1

CreateCustomerErrorBody: TypeAlias = CustomerErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateCustomerError:
    def map(self, response: HttpResponse) -> CreateCustomerErrorBody:
        match response.status_code:
            case 422:
                return decode_json[CustomerErrorResponse1](response)
            case _:
                return RawError(response)


create_customer_error_mapper: Final[ErrorMapper[CreateCustomerErrorBody]] = _CreateCustomerError()
