from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteMetadataErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteMetadataError:
    def map(self, response: HttpResponse) -> DeleteMetadataErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


delete_metadata_error_mapper: Final[ErrorMapper[DeleteMetadataErrorBody]] = _DeleteMetadataError()
