from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    json_body,
    json_decoder,
    param,
)
from ..errors.request_access_token_error import RequestAccessTokenErrorBody, request_access_token_error_mapper
from ..models.maxio_gateway_oauth_access_token import MaxioGatewayOauthAccessToken
from ..models.maxio_gateway_oauth_token_request import MaxioGatewayOauthTokenRequest, MaxioGatewayOauthTokenRequestDict
from ..server.server import Server


class MaxioGateway:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = MaxioGatewayWithRawResponse(client, server)

    def request_access_token(
        self,
        body: MaxioGatewayOauthTokenRequest | MaxioGatewayOauthTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MaxioGatewayOauthAccessToken:
        """Exchanges your connector's OAuth 2.0 client credentials for a bearer access token.

        Authenticate with HTTP Basic auth (``client_id`` as the username, ``client_secret`` as the password) or send
        ``client_id`` and ``client_secret`` in the form body. Then send the returned ``access_token`` as
        ``Authorization: Bearer <access_token>`` on every gateway request.

        The client-credentials grant does not issue a refresh token — when the token expires, request a new one with the
        same credentials.

        This endpoint is available only for connectors configured for OAuth2. It lives at your connector's root host
        (``https://{connector}.api.maxio.com/oauth/token``), not under the ``/api/v1/billing`` base path.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Access token issued.

        Raises:
            ApiError: Malformed request — for example a missing or unsupported grant_type. Client authentication failed
                — unknown or invalid client_id / client_secret. ``error`` is ``MaxioGatewayOauthError | RawError``."""
        return self._with_raw_response.request_access_token(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MaxioGatewayWithRawResponse:
        return self._with_raw_response


class AsyncMaxioGateway:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncMaxioGatewayWithRawResponse(client, server)

    async def request_access_token(
        self,
        body: MaxioGatewayOauthTokenRequest | MaxioGatewayOauthTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MaxioGatewayOauthAccessToken:
        """Exchanges your connector's OAuth 2.0 client credentials for a bearer access token.

        Authenticate with HTTP Basic auth (``client_id`` as the username, ``client_secret`` as the password) or send
        ``client_id`` and ``client_secret`` in the form body. Then send the returned ``access_token`` as
        ``Authorization: Bearer <access_token>`` on every gateway request.

        The client-credentials grant does not issue a refresh token — when the token expires, request a new one with the
        same credentials.

        This endpoint is available only for connectors configured for OAuth2. It lives at your connector's root host
        (``https://{connector}.api.maxio.com/oauth/token``), not under the ``/api/v1/billing`` base path.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Access token issued.

        Raises:
            ApiError: Malformed request — for example a missing or unsupported grant_type. Client authentication failed
                — unknown or invalid client_id / client_secret. ``error`` is ``MaxioGatewayOauthError | RawError``."""
        return (await self._with_raw_response.request_access_token(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncMaxioGatewayWithRawResponse:
        return self._with_raw_response


class MaxioGatewayWithRawResponse(BaseRawResponse[RawClient, Server]):
    def request_access_token(
        self,
        body: MaxioGatewayOauthTokenRequest | MaxioGatewayOauthTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MaxioGatewayOauthAccessToken, RequestAccessTokenErrorBody]:
        """Exchanges your connector's OAuth 2.0 client credentials for a bearer access token.

        Authenticate with HTTP Basic auth (``client_id`` as the username, ``client_secret`` as the password) or send
        ``client_id`` and ``client_secret`` in the form body. Then send the returned ``access_token`` as
        ``Authorization: Bearer <access_token>`` on every gateway request.

        The client-credentials grant does not issue a refresh token — when the token expires, request a new one with the
        same credentials.

        This endpoint is available only for connectors configured for OAuth2. It lives at your connector's root host
        (``https://{connector}.api.maxio.com/oauth/token``), not under the ``/api/v1/billing`` base path.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.oauth("/oauth/token"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MaxioGatewayOauthTokenRequest | MaxioGatewayOauthTokenRequestDict](body),
            decoder=json_decoder[MaxioGatewayOauthAccessToken],
            error_mapper=request_access_token_error_mapper,
            request_options=request_options,
        )


class AsyncMaxioGatewayWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def request_access_token(
        self,
        body: MaxioGatewayOauthTokenRequest | MaxioGatewayOauthTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MaxioGatewayOauthAccessToken, RequestAccessTokenErrorBody]:
        """Exchanges your connector's OAuth 2.0 client credentials for a bearer access token.

        Authenticate with HTTP Basic auth (``client_id`` as the username, ``client_secret`` as the password) or send
        ``client_id`` and ``client_secret`` in the form body. Then send the returned ``access_token`` as
        ``Authorization: Bearer <access_token>`` on every gateway request.

        The client-credentials grant does not issue a refresh token — when the token expires, request a new one with the
        same credentials.

        This endpoint is available only for connectors configured for OAuth2. It lives at your connector's root host
        (``https://{connector}.api.maxio.com/oauth/token``), not under the ``/api/v1/billing`` base path.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.oauth("/oauth/token"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MaxioGatewayOauthTokenRequest | MaxioGatewayOauthTokenRequestDict](body),
            decoder=json_decoder[MaxioGatewayOauthAccessToken],
            error_mapper=request_access_token_error_mapper,
            request_options=request_options,
        )
