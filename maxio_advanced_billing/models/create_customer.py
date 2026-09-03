from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CreateCustomer(SdkBaseModel):
    first_name: str
    last_name: str
    email: str
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
    """Whether surcharging is enabled for the customer. Defaults to ``true`` when omitted. Only applied on sites where
    surcharging control is enabled."""

    tax_exempt_reason: Optional[str] = UNSET
    parent_id: OptionalNullable[int] = UNSET
    """The parent ID in Chargify if applicable. Parent is another Customer object."""

    salesforce_id: OptionalNullable[str] = UNSET
    """The Salesforce ID of the customer"""

    branding_theme_id: OptionalNullable[int] = UNSET
    """The ID of the Branding Theme assigned to this customer as the customer's default Branding Theme. This
    customer-level Branding Theme is used when a subscription does not have its own subscription-level Branding Theme.
    Available only when Branding Themes are enabled for the site."""


class CreateCustomerDict(TypedDict):
    first_name: str
    last_name: str
    email: str
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
    salesforce_id: NotRequired[str | None]
    branding_theme_id: NotRequired[int | None]
