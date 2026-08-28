from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.item_type1 import ItemType1OrStr
from .scheduled_renewal_product_price_point import (
    ScheduledRenewalProductPricePoint,
    ScheduledRenewalProductPricePointDict,
)


class ScheduledRenewalItemRequestBodyProduct(SdkBaseModel):
    item_type: ItemType1OrStr
    """Item type to add. Either Product or Component."""

    item_id: int
    """Product or component identifier."""

    price_point_id: Optional[int] = UNSET
    """Price point identifier."""

    quantity: Optional[int] = UNSET
    """(Optional) Quantity for the item."""

    custom_price: Optional[ScheduledRenewalProductPricePoint] = UNSET
    """Custom pricing for a product within a scheduled renewal."""


class ScheduledRenewalItemRequestBodyProductDict(TypedDict):
    item_type: ItemType1OrStr
    item_id: int
    price_point_id: NotRequired[int]
    quantity: NotRequired[int]
    custom_price: NotRequired[ScheduledRenewalProductPricePoint | ScheduledRenewalProductPricePointDict]
