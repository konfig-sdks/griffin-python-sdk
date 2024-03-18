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

from griffin_python_sdk.model.decisions_list_for_legal_person_response import DecisionsListForLegalPersonResponse as DecisionsListForLegalPersonResponseSchema

from griffin_python_sdk.type.decisions_list_for_legal_person_response import DecisionsListForLegalPersonResponse

from ...api_client import Dictionary
from griffin_python_sdk.pydantic.decisions_list_for_legal_person_response import DecisionsListForLegalPersonResponse as DecisionsListForLegalPersonResponsePydantic

from . import path

# Query params


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "-created-at": "CREATEDAT",
            "created-at": "CREATEDAT",
        }
    
    @schemas.classproperty
    def CREATEDAT(cls):
        return cls("-created-at")
    
    @schemas.classproperty
    def CREATEDAT(cls):
        return cls("created-at")


class PageSizeSchema(
    schemas.Int64Schema
):


    class MetaOapg:
        format = 'int64'
        inclusive_maximum = 200
        inclusive_minimum = 1
PageAfterSchema = schemas.StrSchema
PageBeforeSchema = schemas.StrSchema
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
        'page[after]': typing.Union[PageAfterSchema, str, ],
        'page[before]': typing.Union[PageBeforeSchema, str, ],
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
request_query_page_after = api_client.QueryParameter(
    name="page[after]",
    style=api_client.ParameterStyle.FORM,
    schema=PageAfterSchema,
    explode=True,
)
request_query_page_before = api_client.QueryParameter(
    name="page[before]",
    style=api_client.ParameterStyle.FORM,
    schema=PageBeforeSchema,
    explode=True,
)
# Path params
LegalPersonIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'legal-person-id': typing.Union[LegalPersonIdSchema, str, ],
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


request_path_legal_person_id = api_client.PathParameter(
    name="legal-person-id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LegalPersonIdSchema,
    required=True,
)
_auth = [
    'api-key-auth',
]
SchemaFor200ResponseBodyApplicationJson = DecisionsListForLegalPersonResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: DecisionsListForLegalPersonResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: DecisionsListForLegalPersonResponse


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
www_authenticate_parameter = api_client.HeaderParameter(
    name="www-authenticate",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WwwAuthenticateSchema,
)
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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_for_legal_person_mapped_args(
        self,
        legal_person_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_after: typing.Optional[str] = None,
        page_before: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if sort is not None:
            _query_params["sort"] = sort
        if page_size is not None:
            _query_params["page[size]"] = page_size
        if page_after is not None:
            _query_params["page[after]"] = page_after
        if page_before is not None:
            _query_params["page[before]"] = page_before
        if legal_person_id is not None:
            _path_params["legal-person-id"] = legal_person_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _alist_for_legal_person_oapg(
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
        List decisions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_legal_person_id,
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
            request_query_page_after,
            request_query_page_before,
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
            path_template='/v0/legal-persons/{legal-person-id}/decisions',
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


    def _list_for_legal_person_oapg(
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
        List decisions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_legal_person_id,
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
            request_query_page_after,
            request_query_page_before,
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
            path_template='/v0/legal-persons/{legal-person-id}/decisions',
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


class ListForLegalPersonRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_for_legal_person(
        self,
        legal_person_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_after: typing.Optional[str] = None,
        page_before: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_for_legal_person_mapped_args(
            legal_person_id=legal_person_id,
            sort=sort,
            page_size=page_size,
            page_after=page_after,
            page_before=page_before,
        )
        return await self._alist_for_legal_person_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def list_for_legal_person(
        self,
        legal_person_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_after: typing.Optional[str] = None,
        page_before: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_for_legal_person_mapped_args(
            legal_person_id=legal_person_id,
            sort=sort,
            page_size=page_size,
            page_after=page_after,
            page_before=page_before,
        )
        return self._list_for_legal_person_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class ListForLegalPerson(BaseApi):

    async def alist_for_legal_person(
        self,
        legal_person_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_after: typing.Optional[str] = None,
        page_before: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> DecisionsListForLegalPersonResponsePydantic:
        raw_response = await self.raw.alist_for_legal_person(
            legal_person_id=legal_person_id,
            sort=sort,
            page_size=page_size,
            page_after=page_after,
            page_before=page_before,
            **kwargs,
        )
        if validate:
            return DecisionsListForLegalPersonResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DecisionsListForLegalPersonResponsePydantic, raw_response.body)
    
    
    def list_for_legal_person(
        self,
        legal_person_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_after: typing.Optional[str] = None,
        page_before: typing.Optional[str] = None,
        validate: bool = False,
    ) -> DecisionsListForLegalPersonResponsePydantic:
        raw_response = self.raw.list_for_legal_person(
            legal_person_id=legal_person_id,
            sort=sort,
            page_size=page_size,
            page_after=page_after,
            page_before=page_before,
        )
        if validate:
            return DecisionsListForLegalPersonResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DecisionsListForLegalPersonResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        legal_person_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_after: typing.Optional[str] = None,
        page_before: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_for_legal_person_mapped_args(
            legal_person_id=legal_person_id,
            sort=sort,
            page_size=page_size,
            page_after=page_after,
            page_before=page_before,
        )
        return await self._alist_for_legal_person_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        legal_person_id: str,
        sort: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_after: typing.Optional[str] = None,
        page_before: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_for_legal_person_mapped_args(
            legal_person_id=legal_person_id,
            sort=sort,
            page_size=page_size,
            page_after=page_after,
            page_before=page_before,
        )
        return self._list_for_legal_person_oapg(
            query_params=args.query,
            path_params=args.path,
        )
