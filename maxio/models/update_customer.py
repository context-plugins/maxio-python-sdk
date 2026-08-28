from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class UpdateCustomer(SdkBaseModel):
    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    email: Optional[str] = UNSET
    cc_emails: Optional[str] = UNSET
    organization: Optional[str] = UNSET
    reference: Optional[str] = UNSET
    address: Optional[str] = UNSET
    address_2: Optional[str] = UNSET
    city: Optional[str] = UNSET
    state: Optional[str] = UNSET
    zip: Optional[str] = UNSET
    country: Optional[str] = UNSET
    phone: Optional[str] = UNSET
    locale: Optional[str] = UNSET
    """Set a specific language on a customer record."""

    vat_number: Optional[str] = UNSET
    tax_exempt: Optional[bool] = UNSET
    surcharging: Optional[bool] = UNSET
    """Whether surcharging is enabled for the customer. Only applied on sites where surcharging control is enabled."""

    tax_exempt_reason: Optional[str] = UNSET
    parent_id: OptionalNullable[int] = UNSET
    verified: OptionalNullable[bool] = UNSET
    """Is the customer verified to use ACH as a payment method. Available only on the Authorize.Net gateway."""

    salesforce_id: OptionalNullable[str] = UNSET
    """The Salesforce ID of the customer"""

    branding_theme_id: OptionalNullable[int] = UNSET
    """The ID of the Branding Theme assigned to this customer as the customer's default Branding Theme. This
    customer-level Branding Theme is used when a subscription does not have its own subscription-level Branding Theme.
    Available only when Branding Themes are enabled for the site."""


class UpdateCustomerDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    cc_emails: NotRequired[str]
    organization: NotRequired[str]
    reference: NotRequired[str]
    address: NotRequired[str]
    address_2: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    phone: NotRequired[str]
    locale: NotRequired[str]
    vat_number: NotRequired[str]
    tax_exempt: NotRequired[bool]
    surcharging: NotRequired[bool]
    tax_exempt_reason: NotRequired[str]
    parent_id: NotRequired[int | None]
    verified: NotRequired[bool | None]
    salesforce_id: NotRequired[str | None]
    branding_theme_id: NotRequired[int | None]
