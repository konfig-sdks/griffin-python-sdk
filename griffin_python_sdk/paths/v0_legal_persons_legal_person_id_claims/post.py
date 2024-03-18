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

from griffin_python_sdk.model.claims_create_new_claim_request import ClaimsCreateNewClaimRequest as ClaimsCreateNewClaimRequestSchema
from griffin_python_sdk.model.claims_create_new_claim_response import ClaimsCreateNewClaimResponse as ClaimsCreateNewClaimResponseSchema

from griffin_python_sdk.type.claims_create_new_claim_request import ClaimsCreateNewClaimRequest
from griffin_python_sdk.type.claims_create_new_claim_response import ClaimsCreateNewClaimResponse

from ...api_client import Dictionary
from griffin_python_sdk.pydantic.claims_create_new_claim_response import ClaimsCreateNewClaimResponse as ClaimsCreateNewClaimResponsePydantic
from griffin_python_sdk.pydantic.claims_create_new_claim_request import ClaimsCreateNewClaimRequest as ClaimsCreateNewClaimRequestPydantic

from . import path

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
# body param
SchemaForRequestBodyApplicationJson = ClaimsCreateNewClaimRequestSchema


request_body_claims_create_new_claim_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'api-key-auth',
]
SchemaFor201ResponseBodyApplicationJson = ClaimsCreateNewClaimResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: ClaimsCreateNewClaimResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: ClaimsCreateNewClaimResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '401': _response_for_401,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_claim_mapped_args(
        self,
        claim_type: str,
        legal_person_id: str,
        mobile_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_birth: typing.Optional[date] = None,
        given_name: typing.Optional[str] = None,
        surname: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        trading_name: typing.Optional[str] = None,
        trading_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        email_address: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        city: typing.Optional[str] = None,
        building_name: typing.Optional[str] = None,
        street_name: typing.Optional[str] = None,
        entity_name: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        corporation_type: typing.Optional[str] = None,
        telephone_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        building_number: typing.Optional[str] = None,
        country_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_incorporation: typing.Optional[date] = None,
        entity_registration_number: typing.Optional[str] = None,
        income: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        initial_deposit: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        international_payments_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        legal_person_url: typing.Optional[str] = None,
        ownership_percent: typing.Optional[str] = None,
        companies_house_url: typing.Optional[str] = None,
        senior_manager: typing.Optional[bool] = None,
        tax_residency: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        uk_regulatory_permissions: typing.Optional[typing.List[str]] = None,
        business_description: typing.Optional[str] = None,
        individual_sources_of_funds: typing.Optional[typing.List[str]] = None,
        business_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        occupation: typing.Optional[str] = None,
        industry_of_occupation: typing.Optional[str] = None,
        employment_status: typing.Optional[str] = None,
        annual_turnover: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        purposes_of_account: typing.Optional[typing.List[str]] = None,
        sic_codes: typing.Optional[typing.List[str]] = None,
        international_operations_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sources_of_funds: typing.Optional[typing.List[str]] = None,
        reliance_verification_methods: typing.Optional[typing.List[str]] = None,
        reliance_verification_standard: typing.Optional[str] = None,
        business_name: typing.Optional[str] = None,
        individual_purposes_of_account: typing.Optional[typing.List[str]] = None,
        nationality: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        social_media: typing.Optional[str] = None,
        website_url: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if mobile_number is not None:
            _body["mobile-number"] = mobile_number
        if claim_type is not None:
            _body["claim-type"] = claim_type
        if date_of_birth is not None:
            _body["date-of-birth"] = date_of_birth
        if given_name is not None:
            _body["given-name"] = given_name
        if surname is not None:
            _body["surname"] = surname
        if middle_name is not None:
            _body["middle-name"] = middle_name
        if trading_name is not None:
            _body["trading-name"] = trading_name
        if trading_address is not None:
            _body["trading-address"] = trading_address
        if email_address is not None:
            _body["email-address"] = email_address
        if city is not None:
            _body["city"] = city
        if building_name is not None:
            _body["building-name"] = building_name
        if street_name is not None:
            _body["street-name"] = street_name
        if entity_name is not None:
            _body["entity-name"] = entity_name
        if postal_code is not None:
            _body["postal-code"] = postal_code
        if corporation_type is not None:
            _body["corporation-type"] = corporation_type
        if telephone_number is not None:
            _body["telephone-number"] = telephone_number
        if building_number is not None:
            _body["building-number"] = building_number
        if country_code is not None:
            _body["country-code"] = country_code
        if date_of_incorporation is not None:
            _body["date-of-incorporation"] = date_of_incorporation
        if entity_registration_number is not None:
            _body["entity-registration-number"] = entity_registration_number
        if income is not None:
            _body["income"] = income
        if initial_deposit is not None:
            _body["initial-deposit"] = initial_deposit
        if international_payments_countries is not None:
            _body["international-payments-countries"] = international_payments_countries
        if legal_person_url is not None:
            _body["legal-person-url"] = legal_person_url
        if ownership_percent is not None:
            _body["ownership-percent"] = ownership_percent
        if companies_house_url is not None:
            _body["companies-house-url"] = companies_house_url
        if senior_manager is not None:
            _body["senior-manager?"] = senior_manager
        if tax_residency is not None:
            _body["tax-residency"] = tax_residency
        if uk_regulatory_permissions is not None:
            _body["uk-regulatory-permissions"] = uk_regulatory_permissions
        if business_description is not None:
            _body["business-description"] = business_description
        if individual_sources_of_funds is not None:
            _body["individual-sources-of-funds"] = individual_sources_of_funds
        if business_address is not None:
            _body["business-address"] = business_address
        if occupation is not None:
            _body["occupation"] = occupation
        if industry_of_occupation is not None:
            _body["industry-of-occupation"] = industry_of_occupation
        if employment_status is not None:
            _body["employment-status"] = employment_status
        if annual_turnover is not None:
            _body["annual-turnover"] = annual_turnover
        if purposes_of_account is not None:
            _body["purposes-of-account"] = purposes_of_account
        if sic_codes is not None:
            _body["sic-codes"] = sic_codes
        if international_operations_countries is not None:
            _body["international-operations-countries"] = international_operations_countries
        if sources_of_funds is not None:
            _body["sources-of-funds"] = sources_of_funds
        if reliance_verification_methods is not None:
            _body["reliance-verification-methods"] = reliance_verification_methods
        if reliance_verification_standard is not None:
            _body["reliance-verification-standard"] = reliance_verification_standard
        if business_name is not None:
            _body["business-name"] = business_name
        if individual_purposes_of_account is not None:
            _body["individual-purposes-of-account"] = individual_purposes_of_account
        if nationality is not None:
            _body["nationality"] = nationality
        if social_media is not None:
            _body["social-media"] = social_media
        if website_url is not None:
            _body["website-url"] = website_url
        if tax_identification_number is not None:
            _body["tax-identification-number"] = tax_identification_number
        args.body = _body
        if legal_person_id is not None:
            _path_params["legal-person-id"] = legal_person_id
        args.path = _path_params
        return args

    async def _acreate_new_claim_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create claim
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v0/legal-persons/{legal-person-id}/claims',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_claims_create_new_claim_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _create_new_claim_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create claim
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v0/legal-persons/{legal-person-id}/claims',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_claims_create_new_claim_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class CreateNewClaimRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_claim(
        self,
        claim_type: str,
        legal_person_id: str,
        mobile_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_birth: typing.Optional[date] = None,
        given_name: typing.Optional[str] = None,
        surname: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        trading_name: typing.Optional[str] = None,
        trading_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        email_address: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        city: typing.Optional[str] = None,
        building_name: typing.Optional[str] = None,
        street_name: typing.Optional[str] = None,
        entity_name: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        corporation_type: typing.Optional[str] = None,
        telephone_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        building_number: typing.Optional[str] = None,
        country_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_incorporation: typing.Optional[date] = None,
        entity_registration_number: typing.Optional[str] = None,
        income: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        initial_deposit: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        international_payments_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        legal_person_url: typing.Optional[str] = None,
        ownership_percent: typing.Optional[str] = None,
        companies_house_url: typing.Optional[str] = None,
        senior_manager: typing.Optional[bool] = None,
        tax_residency: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        uk_regulatory_permissions: typing.Optional[typing.List[str]] = None,
        business_description: typing.Optional[str] = None,
        individual_sources_of_funds: typing.Optional[typing.List[str]] = None,
        business_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        occupation: typing.Optional[str] = None,
        industry_of_occupation: typing.Optional[str] = None,
        employment_status: typing.Optional[str] = None,
        annual_turnover: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        purposes_of_account: typing.Optional[typing.List[str]] = None,
        sic_codes: typing.Optional[typing.List[str]] = None,
        international_operations_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sources_of_funds: typing.Optional[typing.List[str]] = None,
        reliance_verification_methods: typing.Optional[typing.List[str]] = None,
        reliance_verification_standard: typing.Optional[str] = None,
        business_name: typing.Optional[str] = None,
        individual_purposes_of_account: typing.Optional[typing.List[str]] = None,
        nationality: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        social_media: typing.Optional[str] = None,
        website_url: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_claim_mapped_args(
            claim_type=claim_type,
            legal_person_id=legal_person_id,
            mobile_number=mobile_number,
            date_of_birth=date_of_birth,
            given_name=given_name,
            surname=surname,
            middle_name=middle_name,
            trading_name=trading_name,
            trading_address=trading_address,
            email_address=email_address,
            city=city,
            building_name=building_name,
            street_name=street_name,
            entity_name=entity_name,
            postal_code=postal_code,
            corporation_type=corporation_type,
            telephone_number=telephone_number,
            building_number=building_number,
            country_code=country_code,
            date_of_incorporation=date_of_incorporation,
            entity_registration_number=entity_registration_number,
            income=income,
            initial_deposit=initial_deposit,
            international_payments_countries=international_payments_countries,
            legal_person_url=legal_person_url,
            ownership_percent=ownership_percent,
            companies_house_url=companies_house_url,
            senior_manager=senior_manager,
            tax_residency=tax_residency,
            uk_regulatory_permissions=uk_regulatory_permissions,
            business_description=business_description,
            individual_sources_of_funds=individual_sources_of_funds,
            business_address=business_address,
            occupation=occupation,
            industry_of_occupation=industry_of_occupation,
            employment_status=employment_status,
            annual_turnover=annual_turnover,
            purposes_of_account=purposes_of_account,
            sic_codes=sic_codes,
            international_operations_countries=international_operations_countries,
            sources_of_funds=sources_of_funds,
            reliance_verification_methods=reliance_verification_methods,
            reliance_verification_standard=reliance_verification_standard,
            business_name=business_name,
            individual_purposes_of_account=individual_purposes_of_account,
            nationality=nationality,
            social_media=social_media,
            website_url=website_url,
            tax_identification_number=tax_identification_number,
        )
        return await self._acreate_new_claim_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_new_claim(
        self,
        claim_type: str,
        legal_person_id: str,
        mobile_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_birth: typing.Optional[date] = None,
        given_name: typing.Optional[str] = None,
        surname: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        trading_name: typing.Optional[str] = None,
        trading_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        email_address: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        city: typing.Optional[str] = None,
        building_name: typing.Optional[str] = None,
        street_name: typing.Optional[str] = None,
        entity_name: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        corporation_type: typing.Optional[str] = None,
        telephone_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        building_number: typing.Optional[str] = None,
        country_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_incorporation: typing.Optional[date] = None,
        entity_registration_number: typing.Optional[str] = None,
        income: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        initial_deposit: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        international_payments_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        legal_person_url: typing.Optional[str] = None,
        ownership_percent: typing.Optional[str] = None,
        companies_house_url: typing.Optional[str] = None,
        senior_manager: typing.Optional[bool] = None,
        tax_residency: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        uk_regulatory_permissions: typing.Optional[typing.List[str]] = None,
        business_description: typing.Optional[str] = None,
        individual_sources_of_funds: typing.Optional[typing.List[str]] = None,
        business_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        occupation: typing.Optional[str] = None,
        industry_of_occupation: typing.Optional[str] = None,
        employment_status: typing.Optional[str] = None,
        annual_turnover: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        purposes_of_account: typing.Optional[typing.List[str]] = None,
        sic_codes: typing.Optional[typing.List[str]] = None,
        international_operations_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sources_of_funds: typing.Optional[typing.List[str]] = None,
        reliance_verification_methods: typing.Optional[typing.List[str]] = None,
        reliance_verification_standard: typing.Optional[str] = None,
        business_name: typing.Optional[str] = None,
        individual_purposes_of_account: typing.Optional[typing.List[str]] = None,
        nationality: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        social_media: typing.Optional[str] = None,
        website_url: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_claim_mapped_args(
            claim_type=claim_type,
            legal_person_id=legal_person_id,
            mobile_number=mobile_number,
            date_of_birth=date_of_birth,
            given_name=given_name,
            surname=surname,
            middle_name=middle_name,
            trading_name=trading_name,
            trading_address=trading_address,
            email_address=email_address,
            city=city,
            building_name=building_name,
            street_name=street_name,
            entity_name=entity_name,
            postal_code=postal_code,
            corporation_type=corporation_type,
            telephone_number=telephone_number,
            building_number=building_number,
            country_code=country_code,
            date_of_incorporation=date_of_incorporation,
            entity_registration_number=entity_registration_number,
            income=income,
            initial_deposit=initial_deposit,
            international_payments_countries=international_payments_countries,
            legal_person_url=legal_person_url,
            ownership_percent=ownership_percent,
            companies_house_url=companies_house_url,
            senior_manager=senior_manager,
            tax_residency=tax_residency,
            uk_regulatory_permissions=uk_regulatory_permissions,
            business_description=business_description,
            individual_sources_of_funds=individual_sources_of_funds,
            business_address=business_address,
            occupation=occupation,
            industry_of_occupation=industry_of_occupation,
            employment_status=employment_status,
            annual_turnover=annual_turnover,
            purposes_of_account=purposes_of_account,
            sic_codes=sic_codes,
            international_operations_countries=international_operations_countries,
            sources_of_funds=sources_of_funds,
            reliance_verification_methods=reliance_verification_methods,
            reliance_verification_standard=reliance_verification_standard,
            business_name=business_name,
            individual_purposes_of_account=individual_purposes_of_account,
            nationality=nationality,
            social_media=social_media,
            website_url=website_url,
            tax_identification_number=tax_identification_number,
        )
        return self._create_new_claim_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateNewClaim(BaseApi):

    async def acreate_new_claim(
        self,
        claim_type: str,
        legal_person_id: str,
        mobile_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_birth: typing.Optional[date] = None,
        given_name: typing.Optional[str] = None,
        surname: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        trading_name: typing.Optional[str] = None,
        trading_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        email_address: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        city: typing.Optional[str] = None,
        building_name: typing.Optional[str] = None,
        street_name: typing.Optional[str] = None,
        entity_name: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        corporation_type: typing.Optional[str] = None,
        telephone_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        building_number: typing.Optional[str] = None,
        country_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_incorporation: typing.Optional[date] = None,
        entity_registration_number: typing.Optional[str] = None,
        income: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        initial_deposit: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        international_payments_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        legal_person_url: typing.Optional[str] = None,
        ownership_percent: typing.Optional[str] = None,
        companies_house_url: typing.Optional[str] = None,
        senior_manager: typing.Optional[bool] = None,
        tax_residency: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        uk_regulatory_permissions: typing.Optional[typing.List[str]] = None,
        business_description: typing.Optional[str] = None,
        individual_sources_of_funds: typing.Optional[typing.List[str]] = None,
        business_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        occupation: typing.Optional[str] = None,
        industry_of_occupation: typing.Optional[str] = None,
        employment_status: typing.Optional[str] = None,
        annual_turnover: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        purposes_of_account: typing.Optional[typing.List[str]] = None,
        sic_codes: typing.Optional[typing.List[str]] = None,
        international_operations_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sources_of_funds: typing.Optional[typing.List[str]] = None,
        reliance_verification_methods: typing.Optional[typing.List[str]] = None,
        reliance_verification_standard: typing.Optional[str] = None,
        business_name: typing.Optional[str] = None,
        individual_purposes_of_account: typing.Optional[typing.List[str]] = None,
        nationality: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        social_media: typing.Optional[str] = None,
        website_url: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ClaimsCreateNewClaimResponsePydantic:
        raw_response = await self.raw.acreate_new_claim(
            claim_type=claim_type,
            legal_person_id=legal_person_id,
            mobile_number=mobile_number,
            date_of_birth=date_of_birth,
            given_name=given_name,
            surname=surname,
            middle_name=middle_name,
            trading_name=trading_name,
            trading_address=trading_address,
            email_address=email_address,
            city=city,
            building_name=building_name,
            street_name=street_name,
            entity_name=entity_name,
            postal_code=postal_code,
            corporation_type=corporation_type,
            telephone_number=telephone_number,
            building_number=building_number,
            country_code=country_code,
            date_of_incorporation=date_of_incorporation,
            entity_registration_number=entity_registration_number,
            income=income,
            initial_deposit=initial_deposit,
            international_payments_countries=international_payments_countries,
            legal_person_url=legal_person_url,
            ownership_percent=ownership_percent,
            companies_house_url=companies_house_url,
            senior_manager=senior_manager,
            tax_residency=tax_residency,
            uk_regulatory_permissions=uk_regulatory_permissions,
            business_description=business_description,
            individual_sources_of_funds=individual_sources_of_funds,
            business_address=business_address,
            occupation=occupation,
            industry_of_occupation=industry_of_occupation,
            employment_status=employment_status,
            annual_turnover=annual_turnover,
            purposes_of_account=purposes_of_account,
            sic_codes=sic_codes,
            international_operations_countries=international_operations_countries,
            sources_of_funds=sources_of_funds,
            reliance_verification_methods=reliance_verification_methods,
            reliance_verification_standard=reliance_verification_standard,
            business_name=business_name,
            individual_purposes_of_account=individual_purposes_of_account,
            nationality=nationality,
            social_media=social_media,
            website_url=website_url,
            tax_identification_number=tax_identification_number,
            **kwargs,
        )
        if validate:
            return RootModel[ClaimsCreateNewClaimResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(ClaimsCreateNewClaimResponsePydantic, raw_response.body)
    
    
    def create_new_claim(
        self,
        claim_type: str,
        legal_person_id: str,
        mobile_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_birth: typing.Optional[date] = None,
        given_name: typing.Optional[str] = None,
        surname: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        trading_name: typing.Optional[str] = None,
        trading_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        email_address: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        city: typing.Optional[str] = None,
        building_name: typing.Optional[str] = None,
        street_name: typing.Optional[str] = None,
        entity_name: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        corporation_type: typing.Optional[str] = None,
        telephone_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        building_number: typing.Optional[str] = None,
        country_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_incorporation: typing.Optional[date] = None,
        entity_registration_number: typing.Optional[str] = None,
        income: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        initial_deposit: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        international_payments_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        legal_person_url: typing.Optional[str] = None,
        ownership_percent: typing.Optional[str] = None,
        companies_house_url: typing.Optional[str] = None,
        senior_manager: typing.Optional[bool] = None,
        tax_residency: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        uk_regulatory_permissions: typing.Optional[typing.List[str]] = None,
        business_description: typing.Optional[str] = None,
        individual_sources_of_funds: typing.Optional[typing.List[str]] = None,
        business_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        occupation: typing.Optional[str] = None,
        industry_of_occupation: typing.Optional[str] = None,
        employment_status: typing.Optional[str] = None,
        annual_turnover: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        purposes_of_account: typing.Optional[typing.List[str]] = None,
        sic_codes: typing.Optional[typing.List[str]] = None,
        international_operations_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sources_of_funds: typing.Optional[typing.List[str]] = None,
        reliance_verification_methods: typing.Optional[typing.List[str]] = None,
        reliance_verification_standard: typing.Optional[str] = None,
        business_name: typing.Optional[str] = None,
        individual_purposes_of_account: typing.Optional[typing.List[str]] = None,
        nationality: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        social_media: typing.Optional[str] = None,
        website_url: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ClaimsCreateNewClaimResponsePydantic:
        raw_response = self.raw.create_new_claim(
            claim_type=claim_type,
            legal_person_id=legal_person_id,
            mobile_number=mobile_number,
            date_of_birth=date_of_birth,
            given_name=given_name,
            surname=surname,
            middle_name=middle_name,
            trading_name=trading_name,
            trading_address=trading_address,
            email_address=email_address,
            city=city,
            building_name=building_name,
            street_name=street_name,
            entity_name=entity_name,
            postal_code=postal_code,
            corporation_type=corporation_type,
            telephone_number=telephone_number,
            building_number=building_number,
            country_code=country_code,
            date_of_incorporation=date_of_incorporation,
            entity_registration_number=entity_registration_number,
            income=income,
            initial_deposit=initial_deposit,
            international_payments_countries=international_payments_countries,
            legal_person_url=legal_person_url,
            ownership_percent=ownership_percent,
            companies_house_url=companies_house_url,
            senior_manager=senior_manager,
            tax_residency=tax_residency,
            uk_regulatory_permissions=uk_regulatory_permissions,
            business_description=business_description,
            individual_sources_of_funds=individual_sources_of_funds,
            business_address=business_address,
            occupation=occupation,
            industry_of_occupation=industry_of_occupation,
            employment_status=employment_status,
            annual_turnover=annual_turnover,
            purposes_of_account=purposes_of_account,
            sic_codes=sic_codes,
            international_operations_countries=international_operations_countries,
            sources_of_funds=sources_of_funds,
            reliance_verification_methods=reliance_verification_methods,
            reliance_verification_standard=reliance_verification_standard,
            business_name=business_name,
            individual_purposes_of_account=individual_purposes_of_account,
            nationality=nationality,
            social_media=social_media,
            website_url=website_url,
            tax_identification_number=tax_identification_number,
        )
        if validate:
            return RootModel[ClaimsCreateNewClaimResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(ClaimsCreateNewClaimResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        claim_type: str,
        legal_person_id: str,
        mobile_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_birth: typing.Optional[date] = None,
        given_name: typing.Optional[str] = None,
        surname: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        trading_name: typing.Optional[str] = None,
        trading_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        email_address: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        city: typing.Optional[str] = None,
        building_name: typing.Optional[str] = None,
        street_name: typing.Optional[str] = None,
        entity_name: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        corporation_type: typing.Optional[str] = None,
        telephone_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        building_number: typing.Optional[str] = None,
        country_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_incorporation: typing.Optional[date] = None,
        entity_registration_number: typing.Optional[str] = None,
        income: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        initial_deposit: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        international_payments_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        legal_person_url: typing.Optional[str] = None,
        ownership_percent: typing.Optional[str] = None,
        companies_house_url: typing.Optional[str] = None,
        senior_manager: typing.Optional[bool] = None,
        tax_residency: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        uk_regulatory_permissions: typing.Optional[typing.List[str]] = None,
        business_description: typing.Optional[str] = None,
        individual_sources_of_funds: typing.Optional[typing.List[str]] = None,
        business_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        occupation: typing.Optional[str] = None,
        industry_of_occupation: typing.Optional[str] = None,
        employment_status: typing.Optional[str] = None,
        annual_turnover: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        purposes_of_account: typing.Optional[typing.List[str]] = None,
        sic_codes: typing.Optional[typing.List[str]] = None,
        international_operations_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sources_of_funds: typing.Optional[typing.List[str]] = None,
        reliance_verification_methods: typing.Optional[typing.List[str]] = None,
        reliance_verification_standard: typing.Optional[str] = None,
        business_name: typing.Optional[str] = None,
        individual_purposes_of_account: typing.Optional[typing.List[str]] = None,
        nationality: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        social_media: typing.Optional[str] = None,
        website_url: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_claim_mapped_args(
            claim_type=claim_type,
            legal_person_id=legal_person_id,
            mobile_number=mobile_number,
            date_of_birth=date_of_birth,
            given_name=given_name,
            surname=surname,
            middle_name=middle_name,
            trading_name=trading_name,
            trading_address=trading_address,
            email_address=email_address,
            city=city,
            building_name=building_name,
            street_name=street_name,
            entity_name=entity_name,
            postal_code=postal_code,
            corporation_type=corporation_type,
            telephone_number=telephone_number,
            building_number=building_number,
            country_code=country_code,
            date_of_incorporation=date_of_incorporation,
            entity_registration_number=entity_registration_number,
            income=income,
            initial_deposit=initial_deposit,
            international_payments_countries=international_payments_countries,
            legal_person_url=legal_person_url,
            ownership_percent=ownership_percent,
            companies_house_url=companies_house_url,
            senior_manager=senior_manager,
            tax_residency=tax_residency,
            uk_regulatory_permissions=uk_regulatory_permissions,
            business_description=business_description,
            individual_sources_of_funds=individual_sources_of_funds,
            business_address=business_address,
            occupation=occupation,
            industry_of_occupation=industry_of_occupation,
            employment_status=employment_status,
            annual_turnover=annual_turnover,
            purposes_of_account=purposes_of_account,
            sic_codes=sic_codes,
            international_operations_countries=international_operations_countries,
            sources_of_funds=sources_of_funds,
            reliance_verification_methods=reliance_verification_methods,
            reliance_verification_standard=reliance_verification_standard,
            business_name=business_name,
            individual_purposes_of_account=individual_purposes_of_account,
            nationality=nationality,
            social_media=social_media,
            website_url=website_url,
            tax_identification_number=tax_identification_number,
        )
        return await self._acreate_new_claim_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        claim_type: str,
        legal_person_id: str,
        mobile_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_birth: typing.Optional[date] = None,
        given_name: typing.Optional[str] = None,
        surname: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        trading_name: typing.Optional[str] = None,
        trading_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        email_address: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        city: typing.Optional[str] = None,
        building_name: typing.Optional[str] = None,
        street_name: typing.Optional[str] = None,
        entity_name: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        corporation_type: typing.Optional[str] = None,
        telephone_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        building_number: typing.Optional[str] = None,
        country_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        date_of_incorporation: typing.Optional[date] = None,
        entity_registration_number: typing.Optional[str] = None,
        income: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        initial_deposit: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        international_payments_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        legal_person_url: typing.Optional[str] = None,
        ownership_percent: typing.Optional[str] = None,
        companies_house_url: typing.Optional[str] = None,
        senior_manager: typing.Optional[bool] = None,
        tax_residency: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        uk_regulatory_permissions: typing.Optional[typing.List[str]] = None,
        business_description: typing.Optional[str] = None,
        individual_sources_of_funds: typing.Optional[typing.List[str]] = None,
        business_address: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        occupation: typing.Optional[str] = None,
        industry_of_occupation: typing.Optional[str] = None,
        employment_status: typing.Optional[str] = None,
        annual_turnover: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        purposes_of_account: typing.Optional[typing.List[str]] = None,
        sic_codes: typing.Optional[typing.List[str]] = None,
        international_operations_countries: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sources_of_funds: typing.Optional[typing.List[str]] = None,
        reliance_verification_methods: typing.Optional[typing.List[str]] = None,
        reliance_verification_standard: typing.Optional[str] = None,
        business_name: typing.Optional[str] = None,
        individual_purposes_of_account: typing.Optional[typing.List[str]] = None,
        nationality: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        social_media: typing.Optional[str] = None,
        website_url: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_claim_mapped_args(
            claim_type=claim_type,
            legal_person_id=legal_person_id,
            mobile_number=mobile_number,
            date_of_birth=date_of_birth,
            given_name=given_name,
            surname=surname,
            middle_name=middle_name,
            trading_name=trading_name,
            trading_address=trading_address,
            email_address=email_address,
            city=city,
            building_name=building_name,
            street_name=street_name,
            entity_name=entity_name,
            postal_code=postal_code,
            corporation_type=corporation_type,
            telephone_number=telephone_number,
            building_number=building_number,
            country_code=country_code,
            date_of_incorporation=date_of_incorporation,
            entity_registration_number=entity_registration_number,
            income=income,
            initial_deposit=initial_deposit,
            international_payments_countries=international_payments_countries,
            legal_person_url=legal_person_url,
            ownership_percent=ownership_percent,
            companies_house_url=companies_house_url,
            senior_manager=senior_manager,
            tax_residency=tax_residency,
            uk_regulatory_permissions=uk_regulatory_permissions,
            business_description=business_description,
            individual_sources_of_funds=individual_sources_of_funds,
            business_address=business_address,
            occupation=occupation,
            industry_of_occupation=industry_of_occupation,
            employment_status=employment_status,
            annual_turnover=annual_turnover,
            purposes_of_account=purposes_of_account,
            sic_codes=sic_codes,
            international_operations_countries=international_operations_countries,
            sources_of_funds=sources_of_funds,
            reliance_verification_methods=reliance_verification_methods,
            reliance_verification_standard=reliance_verification_standard,
            business_name=business_name,
            individual_purposes_of_account=individual_purposes_of_account,
            nationality=nationality,
            social_media=social_media,
            website_url=website_url,
            tax_identification_number=tax_identification_number,
        )
        return self._create_new_claim_oapg(
            body=args.body,
            path_params=args.path,
        )

