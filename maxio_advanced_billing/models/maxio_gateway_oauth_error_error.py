from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MaxioGatewayOauthErrorError(SdkBaseModel):
    error: str
    error_description: Optional[str] = UNSET


class MaxioGatewayOauthErrorErrorDict(TypedDict):
    error: str
    error_description: NotRequired[str]
