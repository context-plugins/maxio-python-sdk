from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1
from ..models.too_many_management_link_requests_error1 import TooManyManagementLinkRequestsError1

ReadBillingPortalLinkErrorBody: TypeAlias = ErrorListResponse1 | TooManyManagementLinkRequestsError1 | RawError


@dataclass(frozen=True, slots=True)
class _ReadBillingPortalLinkError:
    def map(self, response: HttpResponse) -> ReadBillingPortalLinkErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ErrorListResponse1](response)
            case 429:
                return decode_json[TooManyManagementLinkRequestsError1](response)
            case _:
                return RawError(response)


read_billing_portal_link_error_mapper: Final[
    ErrorMapper[ReadBillingPortalLinkErrorBody]
] = _ReadBillingPortalLinkError()
