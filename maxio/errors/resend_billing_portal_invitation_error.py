from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

ResendBillingPortalInvitationErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ResendBillingPortalInvitationError:
    def map(self, response: HttpResponse) -> ResendBillingPortalInvitationErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


resend_billing_portal_invitation_error_mapper: Final[
    ErrorMapper[ResendBillingPortalInvitationErrorBody]
] = _ResendBillingPortalInvitationError()
