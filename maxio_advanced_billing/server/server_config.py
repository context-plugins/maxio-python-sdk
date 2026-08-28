from __future__ import annotations

from typing import TypeAlias

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UrlTemplate, param
from .environment import Environment


class ProductionUsConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://{site}.chargify.com"
    site: str = "subdomain"


class ProductionUsConfigDict(TypedDict):
    base_url: NotRequired[str]
    site: NotRequired[str]


class ProductionEuConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://{site}.ebilling.maxio.com"
    site: str = "subdomain"


class ProductionEuConfigDict(TypedDict):
    base_url: NotRequired[str]
    site: NotRequired[str]


class ProductionMaxioApiGatewayConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://{connector}.api.maxio.com/api/v1/billing"
    connector: str = "connector"


class ProductionMaxioApiGatewayConfigDict(TypedDict):
    base_url: NotRequired[str]
    connector: NotRequired[str]


class ProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    us: ProductionUsConfig = Field(default_factory=ProductionUsConfig)
    eu: ProductionEuConfig = Field(default_factory=ProductionEuConfig)
    maxio_api_gateway: ProductionMaxioApiGatewayConfig = Field(default_factory=ProductionMaxioApiGatewayConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "us":
            us = self.us
            return UrlTemplate(base_url=us.base_url, path=path, variables=[param[str]("site", us.site)])
        if environment == "eu":
            eu = self.eu
            return UrlTemplate(base_url=eu.base_url, path=path, variables=[param[str]("site", eu.site)])
        maxio_api_gateway = self.maxio_api_gateway
        return UrlTemplate(
            base_url=maxio_api_gateway.base_url,
            path=path,
            variables=[param[str]("connector", maxio_api_gateway.connector)],
        )


class ProductionConfigDict(TypedDict):
    us: NotRequired[ProductionUsConfigDict]
    eu: NotRequired[ProductionEuConfigDict]
    maxio_api_gateway: NotRequired[ProductionMaxioApiGatewayConfigDict]


class EbbUsConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://events.chargify.com/{site}"
    site: str = "subdomain"


class EbbUsConfigDict(TypedDict):
    base_url: NotRequired[str]
    site: NotRequired[str]


class EbbEuConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://events.chargify.com/{site}"
    site: str = "subdomain"


class EbbEuConfigDict(TypedDict):
    base_url: NotRequired[str]
    site: NotRequired[str]


class EbbMaxioApiGatewayConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://events.chargify.com/{site}"
    site: str = "subdomain"


class EbbMaxioApiGatewayConfigDict(TypedDict):
    base_url: NotRequired[str]
    site: NotRequired[str]


class EbbConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    us: EbbUsConfig = Field(default_factory=EbbUsConfig)
    eu: EbbEuConfig = Field(default_factory=EbbEuConfig)
    maxio_api_gateway: EbbMaxioApiGatewayConfig = Field(default_factory=EbbMaxioApiGatewayConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "us":
            us = self.us
            return UrlTemplate(base_url=us.base_url, path=path, variables=[param[str]("site", us.site)])
        if environment == "eu":
            eu = self.eu
            return UrlTemplate(base_url=eu.base_url, path=path, variables=[param[str]("site", eu.site)])
        maxio_api_gateway = self.maxio_api_gateway
        return UrlTemplate(
            base_url=maxio_api_gateway.base_url, path=path, variables=[param[str]("site", maxio_api_gateway.site)]
        )


class EbbConfigDict(TypedDict):
    us: NotRequired[EbbUsConfigDict]
    eu: NotRequired[EbbEuConfigDict]
    maxio_api_gateway: NotRequired[EbbMaxioApiGatewayConfigDict]


class OauthUsConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://{connector}.api.maxio.com"
    connector: str = "connector"


class OauthUsConfigDict(TypedDict):
    base_url: NotRequired[str]
    connector: NotRequired[str]


class OauthEuConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://{connector}.api.maxio.com"
    connector: str = "connector"


class OauthEuConfigDict(TypedDict):
    base_url: NotRequired[str]
    connector: NotRequired[str]


class OauthMaxioApiGatewayConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://{connector}.api.maxio.com"
    connector: str = "connector"


class OauthMaxioApiGatewayConfigDict(TypedDict):
    base_url: NotRequired[str]
    connector: NotRequired[str]


class OauthConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    us: OauthUsConfig = Field(default_factory=OauthUsConfig)
    eu: OauthEuConfig = Field(default_factory=OauthEuConfig)
    maxio_api_gateway: OauthMaxioApiGatewayConfig = Field(default_factory=OauthMaxioApiGatewayConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "us":
            us = self.us
            return UrlTemplate(base_url=us.base_url, path=path, variables=[param[str]("connector", us.connector)])
        if environment == "eu":
            eu = self.eu
            return UrlTemplate(base_url=eu.base_url, path=path, variables=[param[str]("connector", eu.connector)])
        maxio_api_gateway = self.maxio_api_gateway
        return UrlTemplate(
            base_url=maxio_api_gateway.base_url,
            path=path,
            variables=[param[str]("connector", maxio_api_gateway.connector)],
        )


class OauthConfigDict(TypedDict):
    us: NotRequired[OauthUsConfigDict]
    eu: NotRequired[OauthEuConfigDict]
    maxio_api_gateway: NotRequired[OauthMaxioApiGatewayConfigDict]


class ServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: ProductionConfig = Field(default_factory=ProductionConfig)
    ebb: EbbConfig = Field(default_factory=EbbConfig)
    oauth: OauthConfig = Field(default_factory=OauthConfig)

    @classmethod
    def coerce(cls, value: ServerConfigOrDict | None) -> ServerConfig:
        if isinstance(value, cls):
            return value
        return cls.model_validate(value if value is not None else {})


class ServerConfigDict(TypedDict):
    production: NotRequired[ProductionConfigDict]
    ebb: NotRequired[EbbConfigDict]
    oauth: NotRequired[OauthConfigDict]


ServerConfigOrDict: TypeAlias = ServerConfig | ServerConfigDict
