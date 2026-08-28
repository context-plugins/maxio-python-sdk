from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GrantType(str, Enum):
    CLIENT_CREDENTIALS = "client_credentials"

    __str__ = str.__str__


GrantTypeOrStr: TypeAlias = Annotated[GrantType | str, open_enum_validator(GrantType)]
