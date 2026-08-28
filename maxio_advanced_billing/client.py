from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.advance_invoice import AdvanceInvoice
from .apis.api_exports import ApiExports
from .apis.billing_portal import BillingPortal
from .apis.component_price_points import ComponentPricePoints
from .apis.components import Components
from .apis.coupons import Coupons
from .apis.custom_fields import CustomFields
from .apis.customers import Customers
from .apis.events import Events
from .apis.events_based_billing_segments import EventsBasedBillingSegments
from .apis.insights import Insights
from .apis.invoices import Invoices
from .apis.maxio_gateway import MaxioGateway
from .apis.offers import Offers
from .apis.payment_profiles import PaymentProfiles
from .apis.product_families import ProductFamilies
from .apis.product_price_points import ProductPricePoints
from .apis.products import Products
from .apis.proforma_invoices import ProformaInvoices
from .apis.reason_codes import ReasonCodes
from .apis.referral_codes import ReferralCodes
from .apis.sales_commissions import SalesCommissions
from .apis.sites import Sites
from .apis.subscription_components import SubscriptionComponents
from .apis.subscription_group_invoice_account import SubscriptionGroupInvoiceAccount
from .apis.subscription_group_status import SubscriptionGroupStatus
from .apis.subscription_groups import SubscriptionGroups
from .apis.subscription_invoice_account import SubscriptionInvoiceAccount
from .apis.subscription_notes import SubscriptionNotes
from .apis.subscription_products import SubscriptionProducts
from .apis.subscription_renewals import SubscriptionRenewals
from .apis.subscription_status import SubscriptionStatus
from .apis.subscriptions import Subscriptions
from .apis.webhooks import Webhooks
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseMaxioAdvancedBillingClient
from .core import (
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    BearerAuthScheme,
    HttpClient,
    HttpxClient,
    RawClient,
    no_auth,
)
from .server.environment import Environment
from .server.server_config import ServerConfigOrDict


class MaxioAdvancedBillingClient(BaseMaxioAdvancedBillingClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "us",
        timeout: float = DEFAULT_TIMEOUT,
        server_config: ServerConfigOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        basic_auth: BasicAuthCredentialsOrDict | None = None,
        bearer_auth: str | None = None,
    ) -> None:
        super().__init__(environment=environment, timeout=timeout, server_config=server_config)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout)
        )
        self._auth = AuthSchemes(
            basic_auth=BasicAuthScheme(BasicAuthCredentials.coerce(basic_auth)) if basic_auth is not None else no_auth,
            bearer_auth=BearerAuthScheme(bearer_auth) if bearer_auth is not None else no_auth,
        )

    @cached_property
    def api_exports(self) -> ApiExports:
        return ApiExports(self._raw_client, self._server, self._auth)

    @cached_property
    def advance_invoice(self) -> AdvanceInvoice:
        return AdvanceInvoice(self._raw_client, self._server, self._auth)

    @cached_property
    def billing_portal(self) -> BillingPortal:
        return BillingPortal(self._raw_client, self._server, self._auth)

    @cached_property
    def component_price_points(self) -> ComponentPricePoints:
        return ComponentPricePoints(self._raw_client, self._server, self._auth)

    @cached_property
    def components(self) -> Components:
        return Components(self._raw_client, self._server, self._auth)

    @cached_property
    def coupons(self) -> Coupons:
        return Coupons(self._raw_client, self._server, self._auth)

    @cached_property
    def custom_fields(self) -> CustomFields:
        return CustomFields(self._raw_client, self._server, self._auth)

    @cached_property
    def customers(self) -> Customers:
        return Customers(self._raw_client, self._server, self._auth)

    @cached_property
    def events(self) -> Events:
        return Events(self._raw_client, self._server, self._auth)

    @cached_property
    def events_based_billing_segments(self) -> EventsBasedBillingSegments:
        return EventsBasedBillingSegments(self._raw_client, self._server, self._auth)

    @cached_property
    def insights(self) -> Insights:
        return Insights(self._raw_client, self._server, self._auth)

    @cached_property
    def invoices(self) -> Invoices:
        return Invoices(self._raw_client, self._server, self._auth)

    @cached_property
    def maxio_gateway(self) -> MaxioGateway:
        return MaxioGateway(self._raw_client, self._server)

    @cached_property
    def offers(self) -> Offers:
        return Offers(self._raw_client, self._server, self._auth)

    @cached_property
    def payment_profiles(self) -> PaymentProfiles:
        return PaymentProfiles(self._raw_client, self._server, self._auth)

    @cached_property
    def product_families(self) -> ProductFamilies:
        return ProductFamilies(self._raw_client, self._server, self._auth)

    @cached_property
    def product_price_points(self) -> ProductPricePoints:
        return ProductPricePoints(self._raw_client, self._server, self._auth)

    @cached_property
    def products(self) -> Products:
        return Products(self._raw_client, self._server, self._auth)

    @cached_property
    def proforma_invoices(self) -> ProformaInvoices:
        return ProformaInvoices(self._raw_client, self._server, self._auth)

    @cached_property
    def reason_codes(self) -> ReasonCodes:
        return ReasonCodes(self._raw_client, self._server, self._auth)

    @cached_property
    def referral_codes(self) -> ReferralCodes:
        return ReferralCodes(self._raw_client, self._server, self._auth)

    @cached_property
    def sales_commissions(self) -> SalesCommissions:
        return SalesCommissions(self._raw_client, self._server, self._auth)

    @cached_property
    def sites(self) -> Sites:
        return Sites(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_components(self) -> SubscriptionComponents:
        return SubscriptionComponents(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_group_invoice_account(self) -> SubscriptionGroupInvoiceAccount:
        return SubscriptionGroupInvoiceAccount(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_group_status(self) -> SubscriptionGroupStatus:
        return SubscriptionGroupStatus(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_groups(self) -> SubscriptionGroups:
        return SubscriptionGroups(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_invoice_account(self) -> SubscriptionInvoiceAccount:
        return SubscriptionInvoiceAccount(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_notes(self) -> SubscriptionNotes:
        return SubscriptionNotes(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_products(self) -> SubscriptionProducts:
        return SubscriptionProducts(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_renewals(self) -> SubscriptionRenewals:
        return SubscriptionRenewals(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_status(self) -> SubscriptionStatus:
        return SubscriptionStatus(self._raw_client, self._server, self._auth)

    @cached_property
    def subscriptions(self) -> Subscriptions:
        return Subscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def webhooks(self) -> Webhooks:
        return Webhooks(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = MaxioAdvancedBillingClient
