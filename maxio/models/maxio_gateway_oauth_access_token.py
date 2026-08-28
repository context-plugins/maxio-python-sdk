from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MaxioGatewayOauthAccessToken(SdkBaseModel):
    access_token: str
    token_type: str
    expires_in: int
    """Token lifetime in seconds."""

    created_at: int
    """Unix timestamp when the token was issued."""


class MaxioGatewayOauthAccessTokenDict(TypedDict):
    access_token: str
    token_type: str
    expires_in: int
    created_at: int
