from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.component_allocation_error1 import ComponentAllocationError1

PreviewAllocationsErrorBody: TypeAlias = ComponentAllocationError1 | RawError


@dataclass(frozen=True, slots=True)
class _PreviewAllocationsError:
    def map(self, response: HttpResponse) -> PreviewAllocationsErrorBody:
        match response.status_code:
            case 422:
                return decode_json[ComponentAllocationError1](response)
            case _:
                return RawError(response)


preview_allocations_error_mapper: Final[ErrorMapper[PreviewAllocationsErrorBody]] = _PreviewAllocationsError()
