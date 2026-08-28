from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unions.issue_service_credit_error_response import IssueServiceCreditErrorResponse

IssueServiceCreditErrorBody: TypeAlias = IssueServiceCreditErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _IssueServiceCreditError:
    def map(self, response: HttpResponse) -> IssueServiceCreditErrorBody:
        match response.status_code:
            case 422:
                return decode_json[IssueServiceCreditErrorResponse](response)
            case _:
                return RawError(response)


issue_service_credit_error_mapper: Final[ErrorMapper[IssueServiceCreditErrorBody]] = _IssueServiceCreditError()
