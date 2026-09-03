from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.create_customer_error import CreateCustomerErrorBody, create_customer_error_mapper
from ..errors.update_customer_error import UpdateCustomerErrorBody, update_customer_error_mapper
from ..models.create_customer_request import CreateCustomerRequest, CreateCustomerRequestDict
from ..models.customer_response import CustomerResponse
from ..models.enums.basic_date_field import BasicDateFieldOrStr
from ..models.enums.sorting_direction import SortingDirectionOrStr
from ..models.subscription_response import SubscriptionResponse
from ..models.update_customer_request import UpdateCustomerRequest, UpdateCustomerRequestDict
from ..server.server import Server


class Customers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CustomersWithRawResponse(client, server, auth)

    def create_customer(
        self,
        *,
        body: CreateCustomerRequest | CreateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomerResponse:
        """Creates a new customer; can also be created alongside a new subscription. The only validation restriction is
        that you may only create one customer for a given reference value.

        If provided, the ``reference`` value must be unique. It represents a unique identifier for the customer from
        your own app, i.e. the customer’s ID. This allows you to retrieve a given customer via a piece of shared
        information. Alternatively, you may choose to leave ``reference`` blank, and store Advanced Billing’s unique ID
        for the customer, which is in the ``id`` attribute.

        Full documentation on how to locate, create and edit Customers in the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/articles/24252190590093-Customer-Details>`__.

        ## Required Country Format

        Advanced Billing requires that you use the ISO Standard Country codes when formatting country attribute of the
        customer.

        Countries should be formatted as 2 characters. For more information, see the following wikipedia article on
        `ISO_3166-1. <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__

        ## Required State Format

        Advanced Billing requires that you use the ISO Standard State codes when formatting state attribute of the
        customer.

        + US States (2 characters): `ISO_3166-2 <https://en.wikipedia.org/wiki/ISO_3166-2:US>`__

        + States Outside the US (2-3 characters): To find the correct state codes outside of the US, go to `ISO_3166-1
            <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ and click on the link in the “ISO 3166-2 codes”
            column next to country you wish to populate.

        ## Locale

        Advanced Billing allows you to attribute a language/region to your customer to deliver invoices in any required
        language. For more: `Customer Locale
        <https://maxio.zendesk.com/hc/en-us/articles/24286672013709-Customer-Locale>`__

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``CustomerErrorResponse1 | RawError``."""
        return self._with_raw_response.create_customer(body=body, request_options=request_options).unwrap()

    def delete_customer(self, id: int, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes the customer.

        Args:
            id: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_customer(id, request_options=request_options).unwrap()

    def list_customer_subscriptions(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SubscriptionResponse]:
        """Lists all subscriptions that belong to a customer.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, subscriptions no
        longer require an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_customer_subscriptions(
            customer_id, request_options=request_options
        ).unwrap()

    def list_customers(
        self,
        *,
        direction: SortingDirectionOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 50,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        q: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CustomerResponse]:
        """Lists all customers associated with your site, or filters results using the search parameter.

        ## Find Customer

        Use the search feature with the ``q`` query parameter to retrieve an array of customers that matches the search
        query.

        Common use cases are:

        + Search by an email
        + Search by an Advanced Billing ID
        + Search by an organization
        + Search by a reference value from your application
        + Search by a first or last name

        To retrieve a single, exact match by reference, use the `lookup endpoint
        <https://developers.chargify.com/docs/api-docs/b710d8fbef104-read-customer-by-reference>`__.

        Args:
            direction: Direction to sort customers by time of creation
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 50. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of end_date.
            q: A search query by which to filter customers (can be an email, an ID, a reference, organization)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_customers(
            direction=direction,
            page=page,
            per_page=per_page,
            date_field=date_field,
            start_date=start_date,
            end_date=end_date,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            q=q,
            request_options=request_options,
        ).unwrap()

    def read_customer(self, id: int, *, request_options: RequestOptionsOrDict | None = None) -> CustomerResponse:
        """Retrieves the Customer properties by Advanced Billing-generated Customer ID.

        Args:
            id: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.read_customer(id, request_options=request_options).unwrap()

    def read_customer_by_reference(
        self, reference: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CustomerResponse:
        """Returns a customer by their unique reference ID. It will return a single match.

        Args:
            reference: Customer reference
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.read_customer_by_reference(reference, request_options=request_options).unwrap()

    def update_customer(
        self,
        id: int,
        *,
        body: UpdateCustomerRequest | UpdateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomerResponse:
        """Updates the customer.

        Args:
            id: The Advanced Billing id of the customer
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``CustomerErrorResponse1 | RawError``."""
        return self._with_raw_response.update_customer(id, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CustomersWithRawResponse:
        return self._with_raw_response


class AsyncCustomers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCustomersWithRawResponse(client, server, auth)

    async def create_customer(
        self,
        *,
        body: CreateCustomerRequest | CreateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomerResponse:
        """Creates a new customer; can also be created alongside a new subscription. The only validation restriction is
        that you may only create one customer for a given reference value.

        If provided, the ``reference`` value must be unique. It represents a unique identifier for the customer from
        your own app, i.e. the customer’s ID. This allows you to retrieve a given customer via a piece of shared
        information. Alternatively, you may choose to leave ``reference`` blank, and store Advanced Billing’s unique ID
        for the customer, which is in the ``id`` attribute.

        Full documentation on how to locate, create and edit Customers in the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/articles/24252190590093-Customer-Details>`__.

        ## Required Country Format

        Advanced Billing requires that you use the ISO Standard Country codes when formatting country attribute of the
        customer.

        Countries should be formatted as 2 characters. For more information, see the following wikipedia article on
        `ISO_3166-1. <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__

        ## Required State Format

        Advanced Billing requires that you use the ISO Standard State codes when formatting state attribute of the
        customer.

        + US States (2 characters): `ISO_3166-2 <https://en.wikipedia.org/wiki/ISO_3166-2:US>`__

        + States Outside the US (2-3 characters): To find the correct state codes outside of the US, go to `ISO_3166-1
            <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ and click on the link in the “ISO 3166-2 codes”
            column next to country you wish to populate.

        ## Locale

        Advanced Billing allows you to attribute a language/region to your customer to deliver invoices in any required
        language. For more: `Customer Locale
        <https://maxio.zendesk.com/hc/en-us/articles/24286672013709-Customer-Locale>`__

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``CustomerErrorResponse1 | RawError``."""
        return (await self._with_raw_response.create_customer(body=body, request_options=request_options)).unwrap()

    async def delete_customer(self, id: int, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes the customer.

        Args:
            id: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_customer(id, request_options=request_options)).unwrap()

    async def list_customer_subscriptions(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SubscriptionResponse]:
        """Lists all subscriptions that belong to a customer.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, subscriptions no
        longer require an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_customer_subscriptions(customer_id, request_options=request_options)
        ).unwrap()

    async def list_customers(
        self,
        *,
        direction: SortingDirectionOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 50,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        q: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CustomerResponse]:
        """Lists all customers associated with your site, or filters results using the search parameter.

        ## Find Customer

        Use the search feature with the ``q`` query parameter to retrieve an array of customers that matches the search
        query.

        Common use cases are:

        + Search by an email
        + Search by an Advanced Billing ID
        + Search by an organization
        + Search by a reference value from your application
        + Search by a first or last name

        To retrieve a single, exact match by reference, use the `lookup endpoint
        <https://developers.chargify.com/docs/api-docs/b710d8fbef104-read-customer-by-reference>`__.

        Args:
            direction: Direction to sort customers by time of creation
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 50. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of end_date.
            q: A search query by which to filter customers (can be an email, an ID, a reference, organization)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_customers(
                direction=direction,
                page=page,
                per_page=per_page,
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                q=q,
                request_options=request_options,
            )
        ).unwrap()

    async def read_customer(self, id: int, *, request_options: RequestOptionsOrDict | None = None) -> CustomerResponse:
        """Retrieves the Customer properties by Advanced Billing-generated Customer ID.

        Args:
            id: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.read_customer(id, request_options=request_options)).unwrap()

    async def read_customer_by_reference(
        self, reference: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CustomerResponse:
        """Returns a customer by their unique reference ID. It will return a single match.

        Args:
            reference: Customer reference
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.read_customer_by_reference(reference, request_options=request_options)
        ).unwrap()

    async def update_customer(
        self,
        id: int,
        *,
        body: UpdateCustomerRequest | UpdateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomerResponse:
        """Updates the customer.

        Args:
            id: The Advanced Billing id of the customer
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``CustomerErrorResponse1 | RawError``."""
        return (await self._with_raw_response.update_customer(id, body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncCustomersWithRawResponse:
        return self._with_raw_response


class CustomersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_customer(
        self,
        *,
        body: CreateCustomerRequest | CreateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomerResponse, CreateCustomerErrorBody]:
        """Creates a new customer; can also be created alongside a new subscription. The only validation restriction is
        that you may only create one customer for a given reference value.

        If provided, the ``reference`` value must be unique. It represents a unique identifier for the customer from
        your own app, i.e. the customer’s ID. This allows you to retrieve a given customer via a piece of shared
        information. Alternatively, you may choose to leave ``reference`` blank, and store Advanced Billing’s unique ID
        for the customer, which is in the ``id`` attribute.

        Full documentation on how to locate, create and edit Customers in the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/articles/24252190590093-Customer-Details>`__.

        ## Required Country Format

        Advanced Billing requires that you use the ISO Standard Country codes when formatting country attribute of the
        customer.

        Countries should be formatted as 2 characters. For more information, see the following wikipedia article on
        `ISO_3166-1. <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__

        ## Required State Format

        Advanced Billing requires that you use the ISO Standard State codes when formatting state attribute of the
        customer.

        + US States (2 characters): `ISO_3166-2 <https://en.wikipedia.org/wiki/ISO_3166-2:US>`__

        + States Outside the US (2-3 characters): To find the correct state codes outside of the US, go to `ISO_3166-1
            <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ and click on the link in the “ISO 3166-2 codes”
            column next to country you wish to populate.

        ## Locale

        Advanced Billing allows you to attribute a language/region to your customer to deliver invoices in any required
        language. For more: `Customer Locale
        <https://maxio.zendesk.com/hc/en-us/articles/24286672013709-Customer-Locale>`__

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/customers.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCustomerRequest | CreateCustomerRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[CustomerResponse],
            error_mapper=create_customer_error_mapper,
            request_options=request_options,
        )

    def delete_customer(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes the customer.

        Args:
            id: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/customers/{id}.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_customer_subscriptions(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SubscriptionResponse], RawError]:
        """Lists all subscriptions that belong to a customer.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, subscriptions no
        longer require an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers/{customer_id}/subscriptions.json"),
            path_params=[param[int]("customer_id", customer_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[list[SubscriptionResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_customers(
        self,
        *,
        direction: SortingDirectionOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 50,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        q: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CustomerResponse], RawError]:
        """Lists all customers associated with your site, or filters results using the search parameter.

        ## Find Customer

        Use the search feature with the ``q`` query parameter to retrieve an array of customers that matches the search
        query.

        Common use cases are:

        + Search by an email
        + Search by an Advanced Billing ID
        + Search by an organization
        + Search by a reference value from your application
        + Search by a first or last name

        To retrieve a single, exact match by reference, use the `lookup endpoint
        <https://developers.chargify.com/docs/api-docs/b710d8fbef104-read-customer-by-reference>`__.

        Args:
            direction: Direction to sort customers by time of creation
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 50. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of end_date.
            q: A search query by which to filter customers (can be an email, an ID, a reference, organization)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers.json"),
            query_params=[
                param[SortingDirectionOrStr | None]("direction", direction),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_datetime", end_datetime),
                param[str | None]("q", q),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[list[CustomerResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_customer(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CustomerResponse, RawError]:
        """Retrieves the Customer properties by Advanced Billing-generated Customer ID.

        Args:
            id: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers/{id}.json"),
            path_params=[param[int]("id", id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[CustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_customer_by_reference(
        self, reference: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CustomerResponse, RawError]:
        """Returns a customer by their unique reference ID. It will return a single match.

        Args:
            reference: Customer reference
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers/lookup.json"),
            query_params=[param[str]("reference", reference)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[CustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_customer(
        self,
        id: int,
        *,
        body: UpdateCustomerRequest | UpdateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomerResponse, UpdateCustomerErrorBody]:
        """Updates the customer.

        Args:
            id: The Advanced Billing id of the customer
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/customers/{id}.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCustomerRequest | UpdateCustomerRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[CustomerResponse],
            error_mapper=update_customer_error_mapper,
            request_options=request_options,
        )


class AsyncCustomersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_customer(
        self,
        *,
        body: CreateCustomerRequest | CreateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomerResponse, CreateCustomerErrorBody]:
        """Creates a new customer; can also be created alongside a new subscription. The only validation restriction is
        that you may only create one customer for a given reference value.

        If provided, the ``reference`` value must be unique. It represents a unique identifier for the customer from
        your own app, i.e. the customer’s ID. This allows you to retrieve a given customer via a piece of shared
        information. Alternatively, you may choose to leave ``reference`` blank, and store Advanced Billing’s unique ID
        for the customer, which is in the ``id`` attribute.

        Full documentation on how to locate, create and edit Customers in the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/articles/24252190590093-Customer-Details>`__.

        ## Required Country Format

        Advanced Billing requires that you use the ISO Standard Country codes when formatting country attribute of the
        customer.

        Countries should be formatted as 2 characters. For more information, see the following wikipedia article on
        `ISO_3166-1. <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__

        ## Required State Format

        Advanced Billing requires that you use the ISO Standard State codes when formatting state attribute of the
        customer.

        + US States (2 characters): `ISO_3166-2 <https://en.wikipedia.org/wiki/ISO_3166-2:US>`__

        + States Outside the US (2-3 characters): To find the correct state codes outside of the US, go to `ISO_3166-1
            <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ and click on the link in the “ISO 3166-2 codes”
            column next to country you wish to populate.

        ## Locale

        Advanced Billing allows you to attribute a language/region to your customer to deliver invoices in any required
        language. For more: `Customer Locale
        <https://maxio.zendesk.com/hc/en-us/articles/24286672013709-Customer-Locale>`__

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/customers.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCustomerRequest | CreateCustomerRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[CustomerResponse],
            error_mapper=create_customer_error_mapper,
            request_options=request_options,
        )

    async def delete_customer(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes the customer.

        Args:
            id: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/customers/{id}.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_customer_subscriptions(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SubscriptionResponse], RawError]:
        """Lists all subscriptions that belong to a customer.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, subscriptions no
        longer require an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers/{customer_id}/subscriptions.json"),
            path_params=[param[int]("customer_id", customer_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[list[SubscriptionResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_customers(
        self,
        *,
        direction: SortingDirectionOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 50,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        q: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CustomerResponse], RawError]:
        """Lists all customers associated with your site, or filters results using the search parameter.

        ## Find Customer

        Use the search feature with the ``q`` query parameter to retrieve an array of customers that matches the search
        query.

        Common use cases are:

        + Search by an email
        + Search by an Advanced Billing ID
        + Search by an organization
        + Search by a reference value from your application
        + Search by a first or last name

        To retrieve a single, exact match by reference, use the `lookup endpoint
        <https://developers.chargify.com/docs/api-docs/b710d8fbef104-read-customer-by-reference>`__.

        Args:
            direction: Direction to sort customers by time of creation
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 50. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of end_date.
            q: A search query by which to filter customers (can be an email, an ID, a reference, organization)
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers.json"),
            query_params=[
                param[SortingDirectionOrStr | None]("direction", direction),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_datetime", end_datetime),
                param[str | None]("q", q),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[list[CustomerResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_customer(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CustomerResponse, RawError]:
        """Retrieves the Customer properties by Advanced Billing-generated Customer ID.

        Args:
            id: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers/{id}.json"),
            path_params=[param[int]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[CustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_customer_by_reference(
        self, reference: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CustomerResponse, RawError]:
        """Returns a customer by their unique reference ID. It will return a single match.

        Args:
            reference: Customer reference
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers/lookup.json"),
            query_params=[param[str]("reference", reference)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[CustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_customer(
        self,
        id: int,
        *,
        body: UpdateCustomerRequest | UpdateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomerResponse, UpdateCustomerErrorBody]:
        """Updates the customer.

        Args:
            id: The Advanced Billing id of the customer
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/customers/{id}.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCustomerRequest | UpdateCustomerRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.bearer_auth),
            decoder=json_decoder[CustomerResponse],
            error_mapper=update_customer_error_mapper,
            request_options=request_options,
        )
