from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MaxioGatewayOauthTokenRequest(SdkBaseModel):
    grant_type: Literal["client_credentials"] = "client_credentials"
    client_id: Optional[str] = UNSET
    """OAuth client identifier. Omit when authenticating with HTTP Basic."""

    client_secret: Optional[str] = UNSET
    """OAuth client secret. Omit when authenticating with HTTP Basic."""


class MaxioGatewayOauthTokenRequestDict(TypedDict):
    grant_type: NotRequired[Literal["client_credentials"]]
    client_id: NotRequired[str]
    client_secret: NotRequired[str]
