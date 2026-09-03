from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_component_allocation_error1 import SubscriptionComponentAllocationError1

UpdatePrepaidUsageAllocationExpirationDateErrorBody: TypeAlias = SubscriptionComponentAllocationError1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdatePrepaidUsageAllocationExpirationDateError:
    def map(self, response: HttpResponse) -> UpdatePrepaidUsageAllocationExpirationDateErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case 422:
                return decode_json[SubscriptionComponentAllocationError1](response)
            case _:
                return RawError(response)


update_prepaid_usage_allocation_expiration_date_error_mapper: Final[
    ErrorMapper[UpdatePrepaidUsageAllocationExpirationDateErrorBody]
] = _UpdatePrepaidUsageAllocationExpirationDateError()
