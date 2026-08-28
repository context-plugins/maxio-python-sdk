from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.validate_referral_code_error import ValidateReferralCodeErrorBody, validate_referral_code_error_mapper
from ..models.referral_validation_response import ReferralValidationResponse
from ..server.server import Server


class ReferralCodes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReferralCodesWithRawResponse(client, server, auth)

    def validate_referral_code(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReferralValidationResponse:
        """Validates whether a referral code is valid and applicable within your site. This method is useful for
        validating referral codes that are entered by a customer.

        ## Referrals Documentation

        Full documentation on how to use the referrals feature in the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/sections/24286965611405-Referrals>`__.

        ## Server Response

        If the referral code is valid the status code will be ``200`` and the referral code will be returned. If the
        referral code is invalid, a ``404`` response will be returned.

        Args:
            code: The referral code you are trying to validate
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``SingleStringErrorResponse1 | RawError``."""
        return self._with_raw_response.validate_referral_code(code, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ReferralCodesWithRawResponse:
        return self._with_raw_response


class AsyncReferralCodes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReferralCodesWithRawResponse(client, server, auth)

    async def validate_referral_code(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReferralValidationResponse:
        """Validates whether a referral code is valid and applicable within your site. This method is useful for
        validating referral codes that are entered by a customer.

        ## Referrals Documentation

        Full documentation on how to use the referrals feature in the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/sections/24286965611405-Referrals>`__.

        ## Server Response

        If the referral code is valid the status code will be ``200`` and the referral code will be returned. If the
        referral code is invalid, a ``404`` response will be returned.

        Args:
            code: The referral code you are trying to validate
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``SingleStringErrorResponse1 | RawError``."""
        return (await self._with_raw_response.validate_referral_code(code, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncReferralCodesWithRawResponse:
        return self._with_raw_response


class ReferralCodesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def validate_referral_code(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReferralValidationResponse, ValidateReferralCodeErrorBody]:
        """Validates whether a referral code is valid and applicable within your site. This method is useful for
        validating referral codes that are entered by a customer.

        ## Referrals Documentation

        Full documentation on how to use the referrals feature in the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/sections/24286965611405-Referrals>`__.

        ## Server Response

        If the referral code is valid the status code will be ``200`` and the referral code will be returned. If the
        referral code is invalid, a ``404`` response will be returned.

        Args:
            code: The referral code you are trying to validate
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/referral_codes/validate.json"),
            query_params=[param[str]("code", code)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[ReferralValidationResponse],
            error_mapper=validate_referral_code_error_mapper,
            request_options=request_options,
        )


class AsyncReferralCodesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def validate_referral_code(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReferralValidationResponse, ValidateReferralCodeErrorBody]:
        """Validates whether a referral code is valid and applicable within your site. This method is useful for
        validating referral codes that are entered by a customer.

        ## Referrals Documentation

        Full documentation on how to use the referrals feature in the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/sections/24286965611405-Referrals>`__.

        ## Server Response

        If the referral code is valid the status code will be ``200`` and the referral code will be returned. If the
        referral code is invalid, a ``404`` response will be returned.

        Args:
            code: The referral code you are trying to validate
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/referral_codes/validate.json"),
            query_params=[param[str]("code", code)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[ReferralValidationResponse],
            error_mapper=validate_referral_code_error_mapper,
            request_options=request_options,
        )
