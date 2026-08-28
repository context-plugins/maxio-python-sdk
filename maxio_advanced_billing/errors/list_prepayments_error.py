from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ListPrepaymentsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListPrepaymentsError:
    def map(self, response: HttpResponse) -> ListPrepaymentsErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


list_prepayments_error_mapper: Final[ErrorMapper[ListPrepaymentsErrorBody]] = _ListPrepaymentsError()
