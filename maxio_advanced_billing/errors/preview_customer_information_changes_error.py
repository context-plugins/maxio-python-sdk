from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

PreviewCustomerInformationChangesErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _PreviewCustomerInformationChangesError:
    def map(self, response: HttpResponse) -> PreviewCustomerInformationChangesErrorBody:
        match response.status_code:
            case 404 | 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


preview_customer_information_changes_error_mapper: Final[
    ErrorMapper[PreviewCustomerInformationChangesErrorBody]
] = _PreviewCustomerInformationChangesError()
