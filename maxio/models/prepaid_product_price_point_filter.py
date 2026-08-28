from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.include_not_null import IncludeNotNullOrStr


class PrepaidProductPricePointFilter(SdkBaseModel):
    product_price_point_id: IncludeNotNullOrStr
    """Passed as a parameter to list methods to return only non null values."""


class PrepaidProductPricePointFilterDict(TypedDict):
    product_price_point_id: IncludeNotNullOrStr
