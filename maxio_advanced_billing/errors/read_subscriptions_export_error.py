from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ReadSubscriptionsExportErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadSubscriptionsExportError:
    def map(self, response: HttpResponse) -> ReadSubscriptionsExportErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


read_subscriptions_export_error_mapper: Final[
    ErrorMapper[ReadSubscriptionsExportErrorBody]
] = _ReadSubscriptionsExportError()
