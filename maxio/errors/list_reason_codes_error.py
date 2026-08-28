from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

ListReasonCodesErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ListReasonCodesError:
    def map(self, response: HttpResponse) -> ListReasonCodesErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


list_reason_codes_error_mapper: Final[ErrorMapper[ListReasonCodesErrorBody]] = _ListReasonCodesError()
