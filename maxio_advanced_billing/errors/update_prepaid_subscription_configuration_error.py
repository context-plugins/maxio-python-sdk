from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unions.prepaid_configuration_error_response import PrepaidConfigurationErrorResponse

UpdatePrepaidSubscriptionConfigurationErrorBody: TypeAlias = PrepaidConfigurationErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _UpdatePrepaidSubscriptionConfigurationError:
    def map(self, response: HttpResponse) -> UpdatePrepaidSubscriptionConfigurationErrorBody:
        match response.status_code:
            case 422:
                return decode_json[PrepaidConfigurationErrorResponse](response)
            case _:
                return RawError(response)


update_prepaid_subscription_configuration_error_mapper: Final[
    ErrorMapper[UpdatePrepaidSubscriptionConfigurationErrorBody]
] = _UpdatePrepaidSubscriptionConfigurationError()
