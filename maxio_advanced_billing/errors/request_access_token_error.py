from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.maxio_gateway_oauth_error import MaxioGatewayOauthError

RequestAccessTokenErrorBody: TypeAlias = MaxioGatewayOauthError | RawError


@dataclass(frozen=True, slots=True)
class _RequestAccessTokenError:
    def map(self, response: HttpResponse) -> RequestAccessTokenErrorBody:
        match response.status_code:
            case 400 | 401:
                return decode_json[MaxioGatewayOauthError](response)
            case _:
                return RawError(response)


request_access_token_error_mapper: Final[ErrorMapper[RequestAccessTokenErrorBody]] = _RequestAccessTokenError()
