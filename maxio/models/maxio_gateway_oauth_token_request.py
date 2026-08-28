from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.grant_type import GrantTypeOrStr


class MaxioGatewayOauthTokenRequest(SdkBaseModel):
    grant_type: GrantTypeOrStr
    client_id: Optional[str] = UNSET
    """OAuth client identifier. Omit when authenticating with HTTP Basic."""

    client_secret: Optional[str] = UNSET
    """OAuth client secret. Omit when authenticating with HTTP Basic."""


class MaxioGatewayOauthTokenRequestDict(TypedDict):
    grant_type: GrantTypeOrStr
    client_id: NotRequired[str]
    client_secret: NotRequired[str]
