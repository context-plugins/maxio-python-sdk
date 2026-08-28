from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionListInclude(str, Enum):
    SELF_SERVICE_PAGE_TOKEN = "self_service_page_token"

    __str__ = str.__str__


SubscriptionListIncludeOrStr: TypeAlias = Annotated[
    SubscriptionListInclude | str, open_enum_validator(SubscriptionListInclude)
]
