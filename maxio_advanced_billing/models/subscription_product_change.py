from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubscriptionProductChange(SdkBaseModel):
    previous_product_id: int
    new_product_id: int


class SubscriptionProductChangeDict(TypedDict):
    previous_product_id: int
    new_product_id: int
