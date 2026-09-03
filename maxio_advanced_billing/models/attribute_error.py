from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AttributeError(SdkBaseModel):
    attribute: list[str]


class AttributeErrorDict(TypedDict):
    attribute: list[str]
