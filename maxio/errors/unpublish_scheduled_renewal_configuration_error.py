from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

UnpublishScheduledRenewalConfigurationErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UnpublishScheduledRenewalConfigurationError:
    def map(self, response: HttpResponse) -> UnpublishScheduledRenewalConfigurationErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ErrorListResponse1](response)
            case _:
                return RawError(response)


unpublish_scheduled_renewal_configuration_error_mapper: Final[
    ErrorMapper[UnpublishScheduledRenewalConfigurationErrorBody]
] = _UnpublishScheduledRenewalConfigurationError()
