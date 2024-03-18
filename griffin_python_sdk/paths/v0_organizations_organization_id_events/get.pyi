# coding: utf-8

"""
    The Griffin API

    ## Introduction  The Griffin API is based on [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). It has resource-oriented URLs, accepts [JSON](https://www.json.org/json-en.html)-encoded request bodies, returns [JSON](https://www.json.org/json-en.html)-encoded responses, and uses standard HTTP response verbs and response codes.  Our API deviates from strict RESTful principles if it makes sense to do so, such as when we enforce tighter access controls around certain operations. For example, when closing a bank account: rather than send a PATCH request to the [bank account](http://docs.griffin.com) resource to update it's status to `\"closed\"`, we provide a dedicated account closure resource.  Anyone can [create an account](https://app.griffin.com/register) with Griffin and try out out API in [sandbox mode](http://docs.griffin.com).  New to Griffin? Check out our [getting started guide](http://docs.griffin.com).  ## Navigation  Our API is designed to be navigated programmatically. When you request any resource, you will find the URLs for related resources in the response body.  The API is structured as a tree with your [organization](http://docs.griffin.com) at the top. Everything that you own will be a sub-resource of your organization.  To bootstrap the navigation process, request the [index](http://docs.griffin.com) endpoint: the response will contain your `organization-url`.  For a walkthrough, see our [getting started guide](http://docs.griffin.com).  ## Pagination  Our list APIs support pagination (e.g. [list bank accounts](http://docs.griffin.com) and [list payments](http://docs.griffin.com)). By default, a list API returns up to 25 results. If there are more results available, the response payload will include links to the previous/next pages.  ### Change page size  You can request a different number of results (between 1 and 200, inclusive) by using the `page[size]` query parameter:  ``` GET /v0/organizations/:id/bank/accounts?page[size]=100 ```  ### Navigating between pages  List responses will include a `links` object with `prev` and `next` attributes, as shown below. Perform a GET request to the value of the attribute to fetch the previous/next page of results.  ``` {   \"accounts\": [     // ...   ],   \"links\": {     \"prev\": \"/v0/organizations/og.IG9yZ2FuaXphdGlvbi1pZA/bank/accounts?page[before]=djE6WxSPxfYUTnCU9XtWzj9gGA\",     \"next\": \"/v0/organizations/og.IG9yZ2FuaXphdGlvbi1pZA/bank/accounts?page[after]=djE6aw79PXZySUOL16LD8HRJ3A\"   } }  ``` If there is no previous or next page available, the value of the attribute will be  null.  Any other query parameters included in the initial request will also be included in the response payload's links. If you want to change parameters (see [filtering and sorting](http://docs.griffin.com)), request the first page and follow the links from there.  ## Filtering and sorting  ### Sort results  By default, resources will be listed in descending order, usually based on the `created-at` attribute. You can change the sorting behaviour of a list of results by using the `sort` query parameter.  For example, to list bank accounts in ascending order (oldest first):  ``` GET /v0/organizations/:id/bank/accounts?sort=created-at ```  To _explicitly_ sort in descending order (newest first), prefix the sort attribute with `-`:  ``` GET /v0/organizations/:id/bank/accounts?sort=-created-at ```  ### Filter results  Some list APIs allow you to filter the results. Filters are expressed as nested data structures encoded into query parameters. For example, you can list bank accounts that are in either the `opening` or `open` state with:  ``` GET /v0/organizations/:id/bank/accounts?filter[account-status][in][]=opening&filter[account-status][in][]=open ```  Similarly, you can list legal persons with a specific `application-status`:  ``` GET /v0/organizations/:id/legal-persons?filter[application-status][eq]=accepted ```  ### Include resources  Some list APIs allow you to include associated resources in the response, reducing the number of requests needed to fetch related data. For instance, when listing bank accounts, you can include each bank account's beneficiary legal person by using the `include` query parameter:  ``` GET /v0/organizations/:id/bank/accounts?include=beneficiary ```  The response returns the usual list of bank accounts, but it will also have an `included` object with a `legal-persons` attribute:  ``` {   \"accounts\": [     // ...   ],   \"links\": {     // ...   }   \"included\": {     \"legal-persons\": [       // ...     ]   } } ```  Check the documentation for each list API to see all options for sorting and filtering  ## Versioning  The Griffin API is versioned via a prefix in the URL. The current version is v0. An example endpoint is: https://api.griffin.com/v0/index.  We will not break your integration with a particular version for as long as we support that version. If we release a new version, you will have 12 months to upgrade to it.

    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from griffin_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from griffin_python_sdk.api_response import AsyncGeneratorResponse
from griffin_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from griffin_python_sdk import schemas  # noqa: F401

from griffin_python_sdk.model.events_get_all_organization_events_response import EventsGetAllOrganizationEventsResponse as EventsGetAllOrganizationEventsResponseSchema

from griffin_python_sdk.type.events_get_all_organization_events_response import EventsGetAllOrganizationEventsResponse

from ...api_client import Dictionary
from griffin_python_sdk.pydantic.events_get_all_organization_events_response import EventsGetAllOrganizationEventsResponse as EventsGetAllOrganizationEventsResponsePydantic

# Query params


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def CREATEDAT(cls):
        return cls("-created-at")
    
    @schemas.classproperty
    def CREATEDAT(cls):
        return cls("created-at")


class PageSizeSchema(
    schemas.Int64Schema
):
    pass
PageBeforeSchema = schemas.StrSchema
PageAfterSchema = schemas.StrSchema


class FilterEventTypeEqSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DECISIONCREATED(cls):
        return cls("decision-created")
    
    @schemas.classproperty
    def PAYMENTCREATED(cls):
        return cls("payment-created")
    
    @schemas.classproperty
    def TRANSACTIONCREATED(cls):
        return cls("transaction-created")
    
    @schemas.classproperty
    def VERIFICATIONUPDATED(cls):
        return cls("verification-updated")
    
    @schemas.classproperty
    def ADMISSIONUPDATED(cls):
        return cls("admission-updated")
    
    @schemas.classproperty
    def VERIFICATIONCREATED(cls):
        return cls("verification-created")
    
    @schemas.classproperty
    def ACCOUNTSTATUSUPDATED(cls):
        return cls("account-status-updated")
    
    @schemas.classproperty
    def SUBMISSIONCREATED(cls):
        return cls("submission-created")
    
    @schemas.classproperty
    def TESTEVENT(cls):
        return cls("test-event")
    
    @schemas.classproperty
    def ADMISSIONCREATED(cls):
        return cls("admission-created")
    
    @schemas.classproperty
    def ACCOUNTSTATUSCREATED(cls):
        return cls("account-status-created")
    
    @schemas.classproperty
    def SUBMISSIONUPDATED(cls):
        return cls("submission-updated")
FilterCreatedAtLteSchema = schemas.DateTimeSchema
FilterCreatedAtLtSchema = schemas.DateTimeSchema
FilterCreatedAtGteSchema = schemas.DateTimeSchema
FilterCreatedAtGtSchema = schemas.DateTimeSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'sort': typing.Union[SortSchema, str, ],
        'page[size]': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
        'page[before]': typing.Union[PageBeforeSchema, str, ],
        'page[after]': typing.Union[PageAfterSchema, str, ],
        'filter[event-type][eq]': typing.Union[FilterEventTypeEqSchema, str, ],
        'filter[created-at][lte]': typing.Union[FilterCreatedAtLteSchema, str, datetime, ],
        'filter[created-at][lt]': typing.Union[FilterCreatedAtLtSchema, str, datetime, ],
        'filter[created-at][gte]': typing.Union[FilterCreatedAtGteSchema, str, datetime, ],
        'filter[created-at][gt]': typing.Union[FilterCreatedAtGtSchema, str, datetime, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="page[size]",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
request_query_page_before = api_client.QueryParameter(
    name="page[before]",
    style=api_client.ParameterStyle.FORM,
    schema=PageBeforeSchema,
    explode=True,
)
request_query_page_after = api_client.QueryParameter(
    name="page[after]",
    style=api_client.ParameterStyle.FORM,
    schema=PageAfterSchema,
    explode=True,
)
request_query_filter_event_type_eq = api_client.QueryParameter(
    name="filter[event-type][eq]",
    style=api_client.ParameterStyle.FORM,
    schema=FilterEventTypeEqSchema,
    explode=True,
)
request_query_filter_created_at_lte = api_client.QueryParameter(
    name="filter[created-at][lte]",
    style=api_client.ParameterStyle.FORM,
    schema=FilterCreatedAtLteSchema,
    explode=True,
)
request_query_filter_created_at_lt = api_client.QueryParameter(
    name="filter[created-at][lt]",
    style=api_client.ParameterStyle.FORM,
    schema=FilterCreatedAtLtSchema,
    explode=True,
)
request_query_filter_created_at_gte = api_client.QueryParameter(
    name="filter[created-at][gte]",
    style=api_client.ParameterStyle.FORM,
    schema=FilterCreatedAtGteSchema,
    explode=True,
)
request_query_filter_created_at_gt = api_client.QueryParameter(
    name="filter[created-at][gt]",
    style=api_client.ParameterStyle.FORM,
    schema=FilterCreatedAtGtSchema,
    explode=True,
)
# Path params
OrganizationIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'organization-id': typing.Union[OrganizationIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_organization_id = api_client.PathParameter(
    name="organization-id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OrganizationIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = EventsGetAllOrganizationEventsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EventsGetAllOrganizationEventsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EventsGetAllOrganizationEventsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)
WwwAuthenticateSchema = schemas.StrSchema
ResponseHeadersFor401 = typing_extensions.TypedDict(
    'ResponseHeadersFor401',
    {
        'www-authenticate': WwwAuthenticateSchema,
    }
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    headers: ResponseHeadersFor401
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    headers: ResponseHeadersFor401
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    headers=[
        www_authenticate_parameter,
    ]
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_all_organization_events_mapped_args(
        self,
        organization_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_before: typing.Optional[str] = None,
        page_after: typing.Optional[str] = None,
        filter_event_type_eq: typing.Optional[str] = None,
        filter_created_at_lte: typing.Optional[datetime] = None,
        filter_created_at_lt: typing.Optional[datetime] = None,
        filter_created_at_gte: typing.Optional[datetime] = None,
        filter_created_at_gt: typing.Optional[datetime] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if sort is not None:
            _query_params["sort"] = sort
        if page_size is not None:
            _query_params["page[size]"] = page_size
        if page_before is not None:
            _query_params["page[before]"] = page_before
        if page_after is not None:
            _query_params["page[after]"] = page_after
        if filter_event_type_eq is not None:
            _query_params["filter[event-type][eq]"] = filter_event_type_eq
        if filter_created_at_lte is not None:
            _query_params["filter[created-at][lte]"] = filter_created_at_lte
        if filter_created_at_lt is not None:
            _query_params["filter[created-at][lt]"] = filter_created_at_lt
        if filter_created_at_gte is not None:
            _query_params["filter[created-at][gte]"] = filter_created_at_gte
        if filter_created_at_gt is not None:
            _query_params["filter[created-at][gt]"] = filter_created_at_gt
        if organization_id is not None:
            _path_params["organization-id"] = organization_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_all_organization_events_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_organization_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_sort,
            request_query_page_size,
            request_query_page_before,
            request_query_page_after,
            request_query_filter_event_type_eq,
            request_query_filter_created_at_lte,
            request_query_filter_created_at_lt,
            request_query_filter_created_at_gte,
            request_query_filter_created_at_gt,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v0/organizations/{organization-id}/events',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_all_organization_events_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_organization_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_sort,
            request_query_page_size,
            request_query_page_before,
            request_query_page_after,
            request_query_filter_event_type_eq,
            request_query_filter_created_at_lte,
            request_query_filter_created_at_lt,
            request_query_filter_created_at_gte,
            request_query_filter_created_at_gt,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v0/organizations/{organization-id}/events',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetAllOrganizationEventsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_all_organization_events(
        self,
        organization_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_before: typing.Optional[str] = None,
        page_after: typing.Optional[str] = None,
        filter_event_type_eq: typing.Optional[str] = None,
        filter_created_at_lte: typing.Optional[datetime] = None,
        filter_created_at_lt: typing.Optional[datetime] = None,
        filter_created_at_gte: typing.Optional[datetime] = None,
        filter_created_at_gt: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_organization_events_mapped_args(
            organization_id=organization_id,
            sort=sort,
            page_size=page_size,
            page_before=page_before,
            page_after=page_after,
            filter_event_type_eq=filter_event_type_eq,
            filter_created_at_lte=filter_created_at_lte,
            filter_created_at_lt=filter_created_at_lt,
            filter_created_at_gte=filter_created_at_gte,
            filter_created_at_gt=filter_created_at_gt,
        )
        return await self._aget_all_organization_events_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_all_organization_events(
        self,
        organization_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_before: typing.Optional[str] = None,
        page_after: typing.Optional[str] = None,
        filter_event_type_eq: typing.Optional[str] = None,
        filter_created_at_lte: typing.Optional[datetime] = None,
        filter_created_at_lt: typing.Optional[datetime] = None,
        filter_created_at_gte: typing.Optional[datetime] = None,
        filter_created_at_gt: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_organization_events_mapped_args(
            organization_id=organization_id,
            sort=sort,
            page_size=page_size,
            page_before=page_before,
            page_after=page_after,
            filter_event_type_eq=filter_event_type_eq,
            filter_created_at_lte=filter_created_at_lte,
            filter_created_at_lt=filter_created_at_lt,
            filter_created_at_gte=filter_created_at_gte,
            filter_created_at_gt=filter_created_at_gt,
        )
        return self._get_all_organization_events_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetAllOrganizationEvents(BaseApi):

    async def aget_all_organization_events(
        self,
        organization_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_before: typing.Optional[str] = None,
        page_after: typing.Optional[str] = None,
        filter_event_type_eq: typing.Optional[str] = None,
        filter_created_at_lte: typing.Optional[datetime] = None,
        filter_created_at_lt: typing.Optional[datetime] = None,
        filter_created_at_gte: typing.Optional[datetime] = None,
        filter_created_at_gt: typing.Optional[datetime] = None,
        validate: bool = False,
        **kwargs,
    ) -> EventsGetAllOrganizationEventsResponsePydantic:
        raw_response = await self.raw.aget_all_organization_events(
            organization_id=organization_id,
            sort=sort,
            page_size=page_size,
            page_before=page_before,
            page_after=page_after,
            filter_event_type_eq=filter_event_type_eq,
            filter_created_at_lte=filter_created_at_lte,
            filter_created_at_lt=filter_created_at_lt,
            filter_created_at_gte=filter_created_at_gte,
            filter_created_at_gt=filter_created_at_gt,
            **kwargs,
        )
        if validate:
            return EventsGetAllOrganizationEventsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EventsGetAllOrganizationEventsResponsePydantic, raw_response.body)
    
    
    def get_all_organization_events(
        self,
        organization_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_before: typing.Optional[str] = None,
        page_after: typing.Optional[str] = None,
        filter_event_type_eq: typing.Optional[str] = None,
        filter_created_at_lte: typing.Optional[datetime] = None,
        filter_created_at_lt: typing.Optional[datetime] = None,
        filter_created_at_gte: typing.Optional[datetime] = None,
        filter_created_at_gt: typing.Optional[datetime] = None,
        validate: bool = False,
    ) -> EventsGetAllOrganizationEventsResponsePydantic:
        raw_response = self.raw.get_all_organization_events(
            organization_id=organization_id,
            sort=sort,
            page_size=page_size,
            page_before=page_before,
            page_after=page_after,
            filter_event_type_eq=filter_event_type_eq,
            filter_created_at_lte=filter_created_at_lte,
            filter_created_at_lt=filter_created_at_lt,
            filter_created_at_gte=filter_created_at_gte,
            filter_created_at_gt=filter_created_at_gt,
        )
        if validate:
            return EventsGetAllOrganizationEventsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EventsGetAllOrganizationEventsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        organization_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_before: typing.Optional[str] = None,
        page_after: typing.Optional[str] = None,
        filter_event_type_eq: typing.Optional[str] = None,
        filter_created_at_lte: typing.Optional[datetime] = None,
        filter_created_at_lt: typing.Optional[datetime] = None,
        filter_created_at_gte: typing.Optional[datetime] = None,
        filter_created_at_gt: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_organization_events_mapped_args(
            organization_id=organization_id,
            sort=sort,
            page_size=page_size,
            page_before=page_before,
            page_after=page_after,
            filter_event_type_eq=filter_event_type_eq,
            filter_created_at_lte=filter_created_at_lte,
            filter_created_at_lt=filter_created_at_lt,
            filter_created_at_gte=filter_created_at_gte,
            filter_created_at_gt=filter_created_at_gt,
        )
        return await self._aget_all_organization_events_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        organization_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_before: typing.Optional[str] = None,
        page_after: typing.Optional[str] = None,
        filter_event_type_eq: typing.Optional[str] = None,
        filter_created_at_lte: typing.Optional[datetime] = None,
        filter_created_at_lt: typing.Optional[datetime] = None,
        filter_created_at_gte: typing.Optional[datetime] = None,
        filter_created_at_gt: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_organization_events_mapped_args(
            organization_id=organization_id,
            sort=sort,
            page_size=page_size,
            page_before=page_before,
            page_after=page_after,
            filter_event_type_eq=filter_event_type_eq,
            filter_created_at_lte=filter_created_at_lte,
            filter_created_at_lt=filter_created_at_lt,
            filter_created_at_gte=filter_created_at_gte,
            filter_created_at_gt=filter_created_at_gt,
        )
        return self._get_all_organization_events_oapg(
            query_params=args.query,
            path_params=args.path,
        )

