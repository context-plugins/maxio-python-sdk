from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

CancelScheduledRenewalConfigurationErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CancelScheduledRenewalConfigurationError:
    def map(self, response: HttpResponse) -> CancelScheduledRenewalConfigurationErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


cancel_scheduled_renewal_configuration_error_mapper: Final[
    ErrorMapper[CancelScheduledRenewalConfigurationErrorBody]
] = _CancelScheduledRenewalConfigurationError()
