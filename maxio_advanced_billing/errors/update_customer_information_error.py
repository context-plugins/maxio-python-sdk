from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

UpdateCustomerInformationErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateCustomerInformationError:
    def map(self, response: HttpResponse) -> UpdateCustomerInformationErrorBody:
        match response.status_code:
            case 404 | 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


update_customer_information_error_mapper: Final[
    ErrorMapper[UpdateCustomerInformationErrorBody]
] = _UpdateCustomerInformationError()
