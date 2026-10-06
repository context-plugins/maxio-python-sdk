from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemType1(str, Enum):
    """Item type to add. Either Product or Component."""

    PRODUCT = "Product"

    __str__ = str.__str__


ItemType1OrStr: TypeAlias = Annotated[ItemType1 | str, open_enum_validator(ItemType1)]
