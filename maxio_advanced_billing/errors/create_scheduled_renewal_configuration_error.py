from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

CreateScheduledRenewalConfigurationErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateScheduledRenewalConfigurationError:
    def map(self, response: HttpResponse) -> CreateScheduledRenewalConfigurationErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


create_scheduled_renewal_configuration_error_mapper: Final[
    ErrorMapper[CreateScheduledRenewalConfigurationErrorBody]
] = _CreateScheduledRenewalConfigurationError()
