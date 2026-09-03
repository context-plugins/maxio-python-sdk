from __future__ import annotations

from typing import TypeAlias

from ..scheduled_renewal_item_request_body_component import (
    ScheduledRenewalItemRequestBodyComponent,
    ScheduledRenewalItemRequestBodyComponentDict,
)
from ..scheduled_renewal_item_request_body_product import (
    ScheduledRenewalItemRequestBodyProduct,
    ScheduledRenewalItemRequestBodyProductDict,
)

RenewalConfigurationItem: TypeAlias = ScheduledRenewalItemRequestBodyComponent | ScheduledRenewalItemRequestBodyProduct

RenewalConfigurationItemDict: TypeAlias = (
    ScheduledRenewalItemRequestBodyComponentDict | ScheduledRenewalItemRequestBodyProductDict
)
