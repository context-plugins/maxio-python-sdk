from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_group_update_error_response1 import SubscriptionGroupUpdateErrorResponse1

UpdateSubscriptionGroupMembersErrorBody: TypeAlias = SubscriptionGroupUpdateErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateSubscriptionGroupMembersError:
    def map(self, response: HttpResponse) -> UpdateSubscriptionGroupMembersErrorBody:
        match response.status_code:
            case 422:
                return decode_json[SubscriptionGroupUpdateErrorResponse1](response)
            case _:
                return RawError(response)


update_subscription_group_members_error_mapper: Final[
    ErrorMapper[UpdateSubscriptionGroupMembersErrorBody]
] = _UpdateSubscriptionGroupMembersError()
