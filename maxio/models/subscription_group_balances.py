from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_balance import AccountBalance, AccountBalanceDict


class SubscriptionGroupBalances(SdkBaseModel):
    prepayments: Optional[AccountBalance] = UNSET
    service_credits: Optional[AccountBalance] = UNSET
    open_invoices: Optional[AccountBalance] = UNSET
    pending_discounts: Optional[AccountBalance] = UNSET


class SubscriptionGroupBalancesDict(TypedDict):
    prepayments: NotRequired[AccountBalance | AccountBalanceDict]
    service_credits: NotRequired[AccountBalance | AccountBalanceDict]
    open_invoices: NotRequired[AccountBalance | AccountBalanceDict]
    pending_discounts: NotRequired[AccountBalance | AccountBalanceDict]
