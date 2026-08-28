from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MeteredUsage(SdkBaseModel):
    previous_unit_balance: str
    new_unit_balance: int
    usage_quantity: int
    component_id: int
    component_handle: str
    memo: str


class MeteredUsageDict(TypedDict):
    previous_unit_balance: str
    new_unit_balance: int
    usage_quantity: int
    component_id: int
    component_handle: str
    memo: str
