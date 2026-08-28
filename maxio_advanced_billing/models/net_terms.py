from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NetTerms(SdkBaseModel):
    default_net_terms: Optional[int] = UNSET
    automatic_net_terms: Optional[int] = UNSET
    remittance_net_terms: Optional[int] = UNSET
    net_terms_on_remittance_signups_enabled: Optional[bool] = UNSET
    custom_net_terms_enabled: Optional[bool] = UNSET


class NetTermsDict(TypedDict):
    default_net_terms: NotRequired[int]
    automatic_net_terms: NotRequired[int]
    remittance_net_terms: NotRequired[int]
    net_terms_on_remittance_signups_enabled: NotRequired[bool]
    custom_net_terms_enabled: NotRequired[bool]
