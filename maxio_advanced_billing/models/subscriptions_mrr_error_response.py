from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attribute_error import AttributeError, AttributeErrorDict


class SubscriptionsMrrErrorResponse(SdkBaseModel):
    errors: AttributeError


class SubscriptionsMrrErrorResponseDict(TypedDict):
    errors: AttributeError | AttributeErrorDict
