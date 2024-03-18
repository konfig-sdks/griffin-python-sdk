# coding: utf-8

"""
    The Griffin API

    ## Introduction  The Griffin API is based on [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). It has resource-oriented URLs, accepts [JSON](https://www.json.org/json-en.html)-encoded request bodies, returns [JSON](https://www.json.org/json-en.html)-encoded responses, and uses standard HTTP response verbs and response codes.  Our API deviates from strict RESTful principles if it makes sense to do so, such as when we enforce tighter access controls around certain operations. For example, when closing a bank account: rather than send a PATCH request to the [bank account](http://docs.griffin.com) resource to update it's status to `\"closed\"`, we provide a dedicated account closure resource.  Anyone can [create an account](https://app.griffin.com/register) with Griffin and try out out API in [sandbox mode](http://docs.griffin.com).  New to Griffin? Check out our [getting started guide](http://docs.griffin.com).  ## Navigation  Our API is designed to be navigated programmatically. When you request any resource, you will find the URLs for related resources in the response body.  The API is structured as a tree with your [organization](http://docs.griffin.com) at the top. Everything that you own will be a sub-resource of your organization.  To bootstrap the navigation process, request the [index](http://docs.griffin.com) endpoint: the response will contain your `organization-url`.  For a walkthrough, see our [getting started guide](http://docs.griffin.com).  ## Pagination  Our list APIs support pagination (e.g. [list bank accounts](http://docs.griffin.com) and [list payments](http://docs.griffin.com)). By default, a list API returns up to 25 results. If there are more results available, the response payload will include links to the previous/next pages.  ### Change page size  You can request a different number of results (between 1 and 200, inclusive) by using the `page[size]` query parameter:  ``` GET /v0/organizations/:id/bank/accounts?page[size]=100 ```  ### Navigating between pages  List responses will include a `links` object with `prev` and `next` attributes, as shown below. Perform a GET request to the value of the attribute to fetch the previous/next page of results.  ``` {   \"accounts\": [     // ...   ],   \"links\": {     \"prev\": \"/v0/organizations/og.IG9yZ2FuaXphdGlvbi1pZA/bank/accounts?page[before]=djE6WxSPxfYUTnCU9XtWzj9gGA\",     \"next\": \"/v0/organizations/og.IG9yZ2FuaXphdGlvbi1pZA/bank/accounts?page[after]=djE6aw79PXZySUOL16LD8HRJ3A\"   } }  ``` If there is no previous or next page available, the value of the attribute will be  null.  Any other query parameters included in the initial request will also be included in the response payload's links. If you want to change parameters (see [filtering and sorting](http://docs.griffin.com)), request the first page and follow the links from there.  ## Filtering and sorting  ### Sort results  By default, resources will be listed in descending order, usually based on the `created-at` attribute. You can change the sorting behaviour of a list of results by using the `sort` query parameter.  For example, to list bank accounts in ascending order (oldest first):  ``` GET /v0/organizations/:id/bank/accounts?sort=created-at ```  To _explicitly_ sort in descending order (newest first), prefix the sort attribute with `-`:  ``` GET /v0/organizations/:id/bank/accounts?sort=-created-at ```  ### Filter results  Some list APIs allow you to filter the results. Filters are expressed as nested data structures encoded into query parameters. For example, you can list bank accounts that are in either the `opening` or `open` state with:  ``` GET /v0/organizations/:id/bank/accounts?filter[account-status][in][]=opening&filter[account-status][in][]=open ```  Similarly, you can list legal persons with a specific `application-status`:  ``` GET /v0/organizations/:id/legal-persons?filter[application-status][eq]=accepted ```  ### Include resources  Some list APIs allow you to include associated resources in the response, reducing the number of requests needed to fetch related data. For instance, when listing bank accounts, you can include each bank account's beneficiary legal person by using the `include` query parameter:  ``` GET /v0/organizations/:id/bank/accounts?include=beneficiary ```  The response returns the usual list of bank accounts, but it will also have an `included` object with a `legal-persons` attribute:  ``` {   \"accounts\": [     // ...   ],   \"links\": {     // ...   }   \"included\": {     \"legal-persons\": [       // ...     ]   } } ```  Check the documentation for each list API to see all options for sorting and filtering  ## Versioning  The Griffin API is versioned via a prefix in the URL. The current version is v0. An example endpoint is: https://api.griffin.com/v0/index.  We will not break your integration with a particular version for as long as we support that version. If we release a new version, you will have 12 months to upgrade to it.

    Generated by: https://konfigthis.com
"""

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


class LegalPersonsCreateNewLegalPersonResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "legal-person-type",
            "display-name",
            "legal-person-verifications-url",
            "legal-person-documents-url",
            "legal-person-url",
            "created-at",
            "legal-person-decisions-url",
        }
        
        class properties:
            
            
            class legal_person_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "individual": "INDIVIDUAL",
                        "corporation": "CORPORATION",
                    }
                
                @schemas.classproperty
                def INDIVIDUAL(cls):
                    return cls("individual")
                
                @schemas.classproperty
                def CORPORATION(cls):
                    return cls("corporation")
            
            
            class display_name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    min_length = 1
            legal_person_url = schemas.StrSchema
            legal_person_decisions_url = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            legal_person_verifications_url = schemas.StrSchema
            legal_person_documents_url = schemas.StrSchema
        
            @staticmethod
            def latest_decision() -> typing.Type['LegalPersonsCreateNewLegalPersonResponseLatestDecision']:
                return LegalPersonsCreateNewLegalPersonResponseLatestDecision
            latest_risk_rating_url = schemas.StrSchema
            
            
            class application_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "referred": "REFERRED",
                        "errored": "ERRORED",
                        "declined": "DECLINED",
                        "submitted": "SUBMITTED",
                        "accepted": "ACCEPTED",
                    }
                
                @schemas.classproperty
                def REFERRED(cls):
                    return cls("referred")
                
                @schemas.classproperty
                def ERRORED(cls):
                    return cls("errored")
                
                @schemas.classproperty
                def DECLINED(cls):
                    return cls("declined")
                
                @schemas.classproperty
                def SUBMITTED(cls):
                    return cls("submitted")
                
                @schemas.classproperty
                def ACCEPTED(cls):
                    return cls("accepted")
            status_changed_at = schemas.DateTimeSchema
            legal_person_claims_url = schemas.StrSchema
            legal_person_bank_payees_url = schemas.StrSchema
            __annotations__ = {
                "legal-person-type": legal_person_type,
                "display-name": display_name,
                "legal-person-url": legal_person_url,
                "legal-person-decisions-url": legal_person_decisions_url,
                "created-at": created_at,
                "legal-person-verifications-url": legal_person_verifications_url,
                "legal-person-documents-url": legal_person_documents_url,
                "latest-decision": latest_decision,
                "latest-risk-rating-url": latest_risk_rating_url,
                "application-status": application_status,
                "status-changed-at": status_changed_at,
                "legal-person-claims-url": legal_person_claims_url,
                "legal-person-bank-payees-url": legal_person_bank_payees_url,
            }
    
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legal-person-type"]) -> MetaOapg.properties.legal_person_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display-name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legal-person-url"]) -> MetaOapg.properties.legal_person_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legal-person-decisions-url"]) -> MetaOapg.properties.legal_person_decisions_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created-at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legal-person-verifications-url"]) -> MetaOapg.properties.legal_person_verifications_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legal-person-documents-url"]) -> MetaOapg.properties.legal_person_documents_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latest-decision"]) -> 'LegalPersonsCreateNewLegalPersonResponseLatestDecision': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latest-risk-rating-url"]) -> MetaOapg.properties.latest_risk_rating_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["application-status"]) -> MetaOapg.properties.application_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status-changed-at"]) -> MetaOapg.properties.status_changed_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legal-person-claims-url"]) -> MetaOapg.properties.legal_person_claims_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legal-person-bank-payees-url"]) -> MetaOapg.properties.legal_person_bank_payees_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["legal-person-type", "display-name", "legal-person-url", "legal-person-decisions-url", "created-at", "legal-person-verifications-url", "legal-person-documents-url", "latest-decision", "latest-risk-rating-url", "application-status", "status-changed-at", "legal-person-claims-url", "legal-person-bank-payees-url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legal-person-type"]) -> MetaOapg.properties.legal_person_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display-name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legal-person-url"]) -> MetaOapg.properties.legal_person_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legal-person-decisions-url"]) -> MetaOapg.properties.legal_person_decisions_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created-at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legal-person-verifications-url"]) -> MetaOapg.properties.legal_person_verifications_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legal-person-documents-url"]) -> MetaOapg.properties.legal_person_documents_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latest-decision"]) -> typing.Union['LegalPersonsCreateNewLegalPersonResponseLatestDecision', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latest-risk-rating-url"]) -> typing.Union[MetaOapg.properties.latest_risk_rating_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["application-status"]) -> typing.Union[MetaOapg.properties.application_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status-changed-at"]) -> typing.Union[MetaOapg.properties.status_changed_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legal-person-claims-url"]) -> typing.Union[MetaOapg.properties.legal_person_claims_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legal-person-bank-payees-url"]) -> typing.Union[MetaOapg.properties.legal_person_bank_payees_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["legal-person-type", "display-name", "legal-person-url", "legal-person-decisions-url", "created-at", "legal-person-verifications-url", "legal-person-documents-url", "latest-decision", "latest-risk-rating-url", "application-status", "status-changed-at", "legal-person-claims-url", "legal-person-bank-payees-url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LegalPersonsCreateNewLegalPersonResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from griffin_python_sdk.model.legal_persons_create_new_legal_person_response_latest_decision import LegalPersonsCreateNewLegalPersonResponseLatestDecision
