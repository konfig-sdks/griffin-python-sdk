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


class LegalPersonHistoryListEventsResponseLegalPersonHistoryItem(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "legal-person-history-event-type",
        }
        
        
        class any_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "risk-rating",
                    "legal-person-history-event-type",
                    "timestamp",
                }
                
                class properties:
                    
                    
                    class legal_person_history_event_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "risk-rating-registered": "RISKRATINGREGISTERED",
                            }
                        
                        @schemas.classproperty
                        def RISKRATINGREGISTERED(cls):
                            return cls("risk-rating-registered")
                    timestamp = schemas.DateTimeSchema
                    
                    
                    class risk_rating(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "high-risk": "HIGHRISK",
                                "prohibited-risk": "PROHIBITEDRISK",
                                "medium-risk": "MEDIUMRISK",
                                "low-risk": "LOWRISK",
                            }
                        
                        @schemas.classproperty
                        def HIGHRISK(cls):
                            return cls("high-risk")
                        
                        @schemas.classproperty
                        def PROHIBITEDRISK(cls):
                            return cls("prohibited-risk")
                        
                        @schemas.classproperty
                        def MEDIUMRISK(cls):
                            return cls("medium-risk")
                        
                        @schemas.classproperty
                        def LOWRISK(cls):
                            return cls("low-risk")
                    
                    
                    class notes(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            min_length = 1
                    
                    
                    class manually_created_by(
                        schemas.ComposedBase,
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "manually-created-by-type",
                            }
                            
                            
                            class any_of_0(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "manually-created-by-type",
                                    }
                                    
                                    class properties:
                                        
                                        
                                        class manually_created_by_type(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                enum_value_to_name = {
                                                    "ops-user": "OPSUSER",
                                                }
                                            
                                            @schemas.classproperty
                                            def OPSUSER(cls):
                                                return cls("ops-user")
                                        __annotations__ = {
                                            "manually-created-by-type": manually_created_by_type,
                                        }
                                
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["manually-created-by-type"]) -> MetaOapg.properties.manually_created_by_type: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["manually-created-by-type", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["manually-created-by-type"]) -> MetaOapg.properties.manually_created_by_type: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["manually-created-by-type", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'any_of_0':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            @classmethod
                            @functools.lru_cache()
                            def any_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    cls.any_of_0,
                                ]
                    
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'manually_created_by':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class previous_risk_rating(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "high-risk": "HIGHRISK",
                                "prohibited-risk": "PROHIBITEDRISK",
                                "medium-risk": "MEDIUMRISK",
                                "low-risk": "LOWRISK",
                            }
                        
                        @schemas.classproperty
                        def HIGHRISK(cls):
                            return cls("high-risk")
                        
                        @schemas.classproperty
                        def PROHIBITEDRISK(cls):
                            return cls("prohibited-risk")
                        
                        @schemas.classproperty
                        def MEDIUMRISK(cls):
                            return cls("medium-risk")
                        
                        @schemas.classproperty
                        def LOWRISK(cls):
                            return cls("low-risk")
                    __annotations__ = {
                        "legal-person-history-event-type": legal_person_history_event_type,
                        "timestamp": timestamp,
                        "risk-rating": risk_rating,
                        "notes": notes,
                        "manually-created-by": manually_created_by,
                        "previous-risk-rating": previous_risk_rating,
                    }
            
            timestamp: MetaOapg.properties.timestamp
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["legal-person-history-event-type"]) -> MetaOapg.properties.legal_person_history_event_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["risk-rating"]) -> MetaOapg.properties.risk_rating: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["manually-created-by"]) -> MetaOapg.properties.manually_created_by: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["previous-risk-rating"]) -> MetaOapg.properties.previous_risk_rating: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["legal-person-history-event-type", "timestamp", "risk-rating", "notes", "manually-created-by", "previous-risk-rating", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["legal-person-history-event-type"]) -> MetaOapg.properties.legal_person_history_event_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["risk-rating"]) -> MetaOapg.properties.risk_rating: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["manually-created-by"]) -> typing.Union[MetaOapg.properties.manually_created_by, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["previous-risk-rating"]) -> typing.Union[MetaOapg.properties.previous_risk_rating, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["legal-person-history-event-type", "timestamp", "risk-rating", "notes", "manually-created-by", "previous-risk-rating", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
                notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_0':
                return super().__new__(
                    cls,
                    *args,
                    timestamp=timestamp,
                    notes=notes,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "decision-notes",
                    "verification-url",
                    "decision-maker",
                    "decision-outcome",
                    "legal-person-history-event-type",
                    "timestamp",
                }
                
                class properties:
                    
                    
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
                    decision_notes = schemas.StrSchema
                    verification_url = schemas.StrSchema
                    
                    
                    class legal_person_history_event_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "risk-rating-registered": "RISKRATINGREGISTERED",
                                "decision-created": "DECISIONCREATED",
                            }
                        
                        @schemas.classproperty
                        def RISKRATINGREGISTERED(cls):
                            return cls("risk-rating-registered")
                        
                        @schemas.classproperty
                        def DECISIONCREATED(cls):
                            return cls("decision-created")
                    timestamp = schemas.DateTimeSchema
                    
                    
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
                    decision_user_url = schemas.StrSchema
                    
                    
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
                    decision_user_username = schemas.StrSchema
                    __annotations__ = {
                        "decision-outcome": decision_outcome,
                        "decision-notes": decision_notes,
                        "verification-url": verification_url,
                        "legal-person-history-event-type": legal_person_history_event_type,
                        "timestamp": timestamp,
                        "decision-maker": decision_maker,
                        "decision-user-url": decision_user_url,
                        "decision-ops-user": decision_ops_user,
                        "decision-user-username": decision_user_username,
                    }
            
            timestamp: MetaOapg.properties.timestamp
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["decision-outcome"]) -> MetaOapg.properties.decision_outcome: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["decision-notes"]) -> MetaOapg.properties.decision_notes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["verification-url"]) -> MetaOapg.properties.verification_url: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["legal-person-history-event-type"]) -> MetaOapg.properties.legal_person_history_event_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["decision-maker"]) -> MetaOapg.properties.decision_maker: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["decision-user-url"]) -> MetaOapg.properties.decision_user_url: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["decision-ops-user"]) -> MetaOapg.properties.decision_ops_user: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["decision-user-username"]) -> MetaOapg.properties.decision_user_username: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["decision-outcome", "decision-notes", "verification-url", "legal-person-history-event-type", "timestamp", "decision-maker", "decision-user-url", "decision-ops-user", "decision-user-username", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["decision-outcome"]) -> MetaOapg.properties.decision_outcome: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["decision-notes"]) -> MetaOapg.properties.decision_notes: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["verification-url"]) -> MetaOapg.properties.verification_url: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["legal-person-history-event-type"]) -> MetaOapg.properties.legal_person_history_event_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["decision-maker"]) -> MetaOapg.properties.decision_maker: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["decision-user-url"]) -> typing.Union[MetaOapg.properties.decision_user_url, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["decision-ops-user"]) -> typing.Union[MetaOapg.properties.decision_ops_user, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["decision-user-username"]) -> typing.Union[MetaOapg.properties.decision_user_username, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["decision-outcome", "decision-notes", "verification-url", "legal-person-history-event-type", "timestamp", "decision-maker", "decision-user-url", "decision-ops-user", "decision-user-username", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_1':
                return super().__new__(
                    cls,
                    *args,
                    timestamp=timestamp,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def any_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.any_of_0,
                cls.any_of_1,
            ]

    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LegalPersonHistoryListEventsResponseLegalPersonHistoryItem':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
