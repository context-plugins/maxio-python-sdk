from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reactivation_charge import ReactivationChargeOrStr


class ReactivationBilling(SdkBaseModel):
    """These values are only applicable to subscriptions using calendar billing."""

    reactivation_charge: Optional[ReactivationChargeOrStr] = UNSET
    """You may choose how to handle the reactivation charge for that subscription: 1) ``prorated`` A prorated charge for
    the product price will be attempted to complete the period 2) ``immediate`` A full-price charge for the product
    price will be attempted immediately 3) ``delayed`` A full-price charge for the product price will be attempted at
    the next renewal."""


class ReactivationBillingDict(TypedDict):
    reactivation_charge: NotRequired[ReactivationChargeOrStr]
