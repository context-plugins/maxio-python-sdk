from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteMetafieldErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteMetafieldError:
    def map(self, response: HttpResponse) -> DeleteMetafieldErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


delete_metafield_error_mapper: Final[ErrorMapper[DeleteMetafieldErrorBody]] = _DeleteMetafieldError()
