from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.single_error_response1 import SingleErrorResponse1

ExportSubscriptionsErrorBody: TypeAlias = SingleErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ExportSubscriptionsError:
    def map(self, response: HttpResponse) -> ExportSubscriptionsErrorBody:
        match response.status_code:
            case 409:
                return decode_json[SingleErrorResponse1](response)
            case _:
                return RawError(response)


export_subscriptions_error_mapper: Final[ErrorMapper[ExportSubscriptionsErrorBody]] = _ExportSubscriptionsError()
