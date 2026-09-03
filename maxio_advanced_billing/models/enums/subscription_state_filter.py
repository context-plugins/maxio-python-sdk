from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionStateFilter(str, Enum):
    """Allowed values for filtering by the current state of the subscription."""

    ACTIVE = "active"
    CANCELED = "canceled"
    EXPIRED = "expired"
    EXPIRED_CARDS = "expired_cards"
    ON_HOLD = "on_hold"
    PAST_DUE = "past_due"
    PENDING_CANCELLATION = "pending_cancellation"
    PENDING_RENEWAL = "pending_renewal"
    SUSPENDED = "suspended"
    TRIAL_ENDED = "trial_ended"
    TRIALING = "trialing"
    UNPAID = "unpaid"

    __str__ = str.__str__


SubscriptionStateFilterOrStr: TypeAlias = Annotated[
    SubscriptionStateFilter | str, open_enum_validator(SubscriptionStateFilter)
]
