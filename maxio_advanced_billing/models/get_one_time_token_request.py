from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .get_one_time_token_payment_profile import GetOneTimeTokenPaymentProfile, GetOneTimeTokenPaymentProfileDict


class GetOneTimeTokenRequest(SdkBaseModel):
    payment_profile: GetOneTimeTokenPaymentProfile


class GetOneTimeTokenRequestDict(TypedDict):
    payment_profile: GetOneTimeTokenPaymentProfile | GetOneTimeTokenPaymentProfileDict
