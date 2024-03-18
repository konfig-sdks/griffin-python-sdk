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


class PooledAccountMembershipListLegalPersonsResponseIncludedLegalPersonsItemLatestDecision(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The most recent [decision](http://docs.griffin.com)
    """


    class MetaOapg:
        required = {
            "decision-notes",
            "verification-url",
            "decision-maker",
            "decision-outcome",
            "created-at",
        }
        
        class properties:
            verification_url = schemas.StrSchema
            
            
            class decision_outcome(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "accepted": "ACCEPTED",
                        "declined": "DECLINED",
                    }
                
                @schemas.classproperty
                def ACCEPTED(cls):
                    return cls("accepted")
                
                @schemas.classproperty
                def DECLINED(cls):
                    return cls("declined")
            
            
            class decision_maker(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "system": "SYSTEM",
                        "ops-user": "OPSUSER",
                        "user": "USER",
                    }
                
                @schemas.classproperty
                def SYSTEM(cls):
                    return cls("system")
                
                @schemas.classproperty
                def OPSUSER(cls):
                    return cls("ops-user")
                
                @schemas.classproperty
                def USER(cls):
                    return cls("user")
            decision_notes = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            decision_user_url = schemas.StrSchema
            decision_user_username = schemas.StrSchema
            
            
            class decision_ops_user(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "griffin-ops-user": "GRIFFINOPSUSER",
                    }
                
                @schemas.classproperty
                def GRIFFINOPSUSER(cls):
                    return cls("griffin-ops-user")
            __annotations__ = {
                "verification-url": verification_url,
                "decision-outcome": decision_outcome,
                "decision-maker": decision_maker,
                "decision-notes": decision_notes,
                "created-at": created_at,
                "decision-user-url": decision_user_url,
                "decision-user-username": decision_user_username,
                "decision-ops-user": decision_ops_user,
            }
    
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verification-url"]) -> MetaOapg.properties.verification_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decision-outcome"]) -> MetaOapg.properties.decision_outcome: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decision-maker"]) -> MetaOapg.properties.decision_maker: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decision-notes"]) -> MetaOapg.properties.decision_notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created-at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decision-user-url"]) -> MetaOapg.properties.decision_user_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decision-user-username"]) -> MetaOapg.properties.decision_user_username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decision-ops-user"]) -> MetaOapg.properties.decision_ops_user: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["verification-url", "decision-outcome", "decision-maker", "decision-notes", "created-at", "decision-user-url", "decision-user-username", "decision-ops-user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verification-url"]) -> MetaOapg.properties.verification_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decision-outcome"]) -> MetaOapg.properties.decision_outcome: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decision-maker"]) -> MetaOapg.properties.decision_maker: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decision-notes"]) -> MetaOapg.properties.decision_notes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created-at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decision-user-url"]) -> typing.Union[MetaOapg.properties.decision_user_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decision-user-username"]) -> typing.Union[MetaOapg.properties.decision_user_username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decision-ops-user"]) -> typing.Union[MetaOapg.properties.decision_ops_user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["verification-url", "decision-outcome", "decision-maker", "decision-notes", "created-at", "decision-user-url", "decision-user-username", "decision-ops-user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PooledAccountMembershipListLegalPersonsResponseIncludedLegalPersonsItemLatestDecision':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )