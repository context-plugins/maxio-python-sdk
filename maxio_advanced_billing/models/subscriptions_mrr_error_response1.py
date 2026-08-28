from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attribute_error import AttributeError, AttributeErrorDict


class SubscriptionsMrrErrorResponse1(SdkBaseModel):
    errors: AttributeError


class SubscriptionsMrrErrorResponse1Dict(TypedDict):
    errors: AttributeError | AttributeErrorDict
