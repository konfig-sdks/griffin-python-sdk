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


class ClaimsCreateNewClaimResponse(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "claim-type",
        }
        
        
        class any_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "mobile-number",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class mobile_number(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'(\+[1-9])?\d{1,14}',
                            }]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'mobile_number':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "mobile-number": "MOBILENUMBER",
                            }
                        
                        @schemas.classproperty
                        def MOBILENUMBER(cls):
                            return cls("mobile-number")
                    __annotations__ = {
                        "mobile-number": mobile_number,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["mobile-number"]) -> MetaOapg.properties.mobile_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["mobile-number", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["mobile-number"]) -> MetaOapg.properties.mobile_number: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mobile-number", "claim-type", ], str]):
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
        
        
        class any_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "date-of-birth",
                    "surname",
                    "given-name",
                    "claim-type",
                }
                
                class properties:
                    date_of_birth = schemas.DateSchema
                    given_name = schemas.StrSchema
                    surname = schemas.StrSchema
                    middle_name = schemas.StrSchema
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "individual-identity": "INDIVIDUALIDENTITY",
                            }
                        
                        @schemas.classproperty
                        def INDIVIDUALIDENTITY(cls):
                            return cls("individual-identity")
                    __annotations__ = {
                        "date-of-birth": date_of_birth,
                        "given-name": given_name,
                        "surname": surname,
                        "middle-name": middle_name,
                        "claim-type": claim_type,
                    }
            
            surname: MetaOapg.properties.surname
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["date-of-birth"]) -> MetaOapg.properties.date_of_birth: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["given-name"]) -> MetaOapg.properties.given_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["surname"]) -> MetaOapg.properties.surname: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["middle-name"]) -> MetaOapg.properties.middle_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["date-of-birth", "given-name", "surname", "middle-name", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["date-of-birth"]) -> MetaOapg.properties.date_of_birth: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["given-name"]) -> MetaOapg.properties.given_name: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["surname"]) -> MetaOapg.properties.surname: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["middle-name"]) -> typing.Union[MetaOapg.properties.middle_name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date-of-birth", "given-name", "surname", "middle-name", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                surname: typing.Union[MetaOapg.properties.surname, str, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_1':
                return super().__new__(
                    cls,
                    *args,
                    surname=surname,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_2(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "trading-address",
                    "trading-name",
                    "claim-type",
                }
                
                class properties:
                    trading_name = schemas.StrSchema
                    
                    
                    class trading_address(
                        schemas.ComposedBase,
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "country-code",
                                "postal-code",
                                "city",
                                "street-name",
                            }
                            
                            class properties:
                                street_name = schemas.StrSchema
                                city = schemas.StrSchema
                                
                                
                                class postal_code(
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        max_length = 10
                                        min_length = 0
                                
                                
                                class country_code(
                                    schemas.AnyTypeSchema,
                                ):
                                
                                
                                    class MetaOapg:
                                        max_length = 2
                                        min_length = 2
                                
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'country_code':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                __annotations__ = {
                                    "street-name": street_name,
                                    "city": city,
                                    "postal-code": postal_code,
                                    "country-code": country_code,
                                }
                            
                            
                            class any_of_0(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "building-number",
                                        "building-name",
                                    }
                                    
                                    class properties:
                                        building_name = schemas.StrSchema
                                        building_number = schemas.StrSchema
                                        __annotations__ = {
                                            "building-name": building_name,
                                            "building-number": building_number,
                                        }
                                
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["building-name", "building-number", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building-name", "building-number", ], str]):
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
                            
                            
                            class any_of_1(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "building-name",
                                    }
                                    
                                    class properties:
                                        building_name = schemas.StrSchema
                                        __annotations__ = {
                                            "building-name": building_name,
                                        }
                                
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["building-name", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building-name", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'any_of_1':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            
                            class any_of_2(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "building-number",
                                    }
                                    
                                    class properties:
                                        building_number = schemas.StrSchema
                                        __annotations__ = {
                                            "building-number": building_number,
                                        }
                                
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["building-number", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building-number", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'any_of_2':
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
                                    cls.any_of_1,
                                    cls.any_of_2,
                                ]
                    
                        
                        city: MetaOapg.properties.city
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["street-name"]) -> MetaOapg.properties.street_name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["postal-code"]) -> MetaOapg.properties.postal_code: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["country-code"]) -> MetaOapg.properties.country_code: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["street-name", "city", "postal-code", "country-code", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["street-name"]) -> MetaOapg.properties.street_name: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["postal-code"]) -> MetaOapg.properties.postal_code: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["country-code"]) -> MetaOapg.properties.country_code: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["street-name", "city", "postal-code", "country-code", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            city: typing.Union[MetaOapg.properties.city, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'trading_address':
                            return super().__new__(
                                cls,
                                *args,
                                city=city,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "sole-trader": "SOLETRADER",
                            }
                        
                        @schemas.classproperty
                        def SOLETRADER(cls):
                            return cls("sole-trader")
                    __annotations__ = {
                        "trading-name": trading_name,
                        "trading-address": trading_address,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["trading-name"]) -> MetaOapg.properties.trading_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["trading-address"]) -> MetaOapg.properties.trading_address: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["trading-name", "trading-address", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["trading-name"]) -> MetaOapg.properties.trading_name: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["trading-address"]) -> MetaOapg.properties.trading_address: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["trading-name", "trading-address", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_2':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_3(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "country-code",
                    "postal-code",
                    "corporation-type",
                    "entity-name",
                    "city",
                    "entity-registration-number",
                    "claim-type",
                    "street-name",
                }
                
                class properties:
                    
                    
                    class email_address(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'.+\@.+\..+',
                            }]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'email_address':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "uk-company-register": "UKCOMPANYREGISTER",
                            }
                        
                        @schemas.classproperty
                        def UKCOMPANYREGISTER(cls):
                            return cls("uk-company-register")
                    city = schemas.StrSchema
                    building_name = schemas.StrSchema
                    street_name = schemas.StrSchema
                    entity_name = schemas.StrSchema
                    
                    
                    class postal_code(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 10
                            min_length = 0
                    
                    
                    class corporation_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "private-limited-guarant-nsc-limited-exemption": "PRIVATELIMITEDGUARANTNSCLIMITEDEXEMPTION",
                                "eeig": "EEIG",
                                "private-limited-shares-section-30-exemption": "PRIVATELIMITEDSHARESSECTION30EXEMPTION",
                                "limited-partnership": "LIMITEDPARTNERSHIP",
                                "royal-charter": "ROYALCHARTER",
                                "private-unlimited-nsc": "PRIVATEUNLIMITEDNSC",
                                "old-public-company": "OLDPUBLICCOMPANY",
                                "investment-company-with-variable-capital": "INVESTMENTCOMPANYWITHVARIABLECAPITAL",
                                "other-company-type": "OTHERCOMPANYTYPE",
                                "converted-or-closed": "CONVERTEDORCLOSED",
                                "protected-cell-company": "PROTECTEDCELLCOMPANY",
                                "private-limited-guarant-nsc": "PRIVATELIMITEDGUARANTNSC",
                                "scottish-charitable-incorporated-organisation": "SCOTTISHCHARITABLEINCORPORATEDORGANISATION",
                                "industrial-and-provident-society": "INDUSTRIALANDPROVIDENTSOCIETY",
                                "registered-society-non-jurisdictional": "REGISTEREDSOCIETYNONJURISDICTIONAL",
                                "private-unlimited": "PRIVATEUNLIMITED",
                                "further-education-or-sixth-form-college-corporation": "FURTHEREDUCATIONORSIXTHFORMCOLLEGECORPORATION",
                                "limited-liability-partnership": "LIMITEDLIABILITYPARTNERSHIP",
                                "assurance-company": "ASSURANCECOMPANY",
                                "other": "OTHER",
                                "northern-ireland-other": "NORTHERNIRELANDOTHER",
                                "charitable-incorporated-organisation": "CHARITABLEINCORPORATEDORGANISATION",
                                "oversea-company": "OVERSEACOMPANY",
                                "icvc-securities": "ICVCSECURITIES",
                                "uk-establishment": "UKESTABLISHMENT",
                                "unregistered-company": "UNREGISTEREDCOMPANY",
                                "icvc-warrant": "ICVCWARRANT",
                                "registered-overseas-entity": "REGISTEREDOVERSEASENTITY",
                                "public-limited-company": "PUBLICLIMITEDCOMPANY",
                                "private-limited-company": "PRIVATELIMITEDCOMPANY",
                                "european-public-limited-liability-company-se": "EUROPEANPUBLICLIMITEDLIABILITYCOMPANYSE",
                                "private-unlimted-nsc": "PRIVATEUNLIMTEDNSC",
                                "northern-ireland": "NORTHERNIRELAND",
                                "icvc-umbrella": "ICVCUMBRELLA",
                                "scottish-partnership": "SCOTTISHPARTNERSHIP",
                            }
                        
                        @schemas.classproperty
                        def PRIVATELIMITEDGUARANTNSCLIMITEDEXEMPTION(cls):
                            return cls("private-limited-guarant-nsc-limited-exemption")
                        
                        @schemas.classproperty
                        def EEIG(cls):
                            return cls("eeig")
                        
                        @schemas.classproperty
                        def PRIVATELIMITEDSHARESSECTION30EXEMPTION(cls):
                            return cls("private-limited-shares-section-30-exemption")
                        
                        @schemas.classproperty
                        def LIMITEDPARTNERSHIP(cls):
                            return cls("limited-partnership")
                        
                        @schemas.classproperty
                        def ROYALCHARTER(cls):
                            return cls("royal-charter")
                        
                        @schemas.classproperty
                        def PRIVATEUNLIMITEDNSC(cls):
                            return cls("private-unlimited-nsc")
                        
                        @schemas.classproperty
                        def OLDPUBLICCOMPANY(cls):
                            return cls("old-public-company")
                        
                        @schemas.classproperty
                        def INVESTMENTCOMPANYWITHVARIABLECAPITAL(cls):
                            return cls("investment-company-with-variable-capital")
                        
                        @schemas.classproperty
                        def OTHERCOMPANYTYPE(cls):
                            return cls("other-company-type")
                        
                        @schemas.classproperty
                        def CONVERTEDORCLOSED(cls):
                            return cls("converted-or-closed")
                        
                        @schemas.classproperty
                        def PROTECTEDCELLCOMPANY(cls):
                            return cls("protected-cell-company")
                        
                        @schemas.classproperty
                        def PRIVATELIMITEDGUARANTNSC(cls):
                            return cls("private-limited-guarant-nsc")
                        
                        @schemas.classproperty
                        def SCOTTISHCHARITABLEINCORPORATEDORGANISATION(cls):
                            return cls("scottish-charitable-incorporated-organisation")
                        
                        @schemas.classproperty
                        def INDUSTRIALANDPROVIDENTSOCIETY(cls):
                            return cls("industrial-and-provident-society")
                        
                        @schemas.classproperty
                        def REGISTEREDSOCIETYNONJURISDICTIONAL(cls):
                            return cls("registered-society-non-jurisdictional")
                        
                        @schemas.classproperty
                        def PRIVATEUNLIMITED(cls):
                            return cls("private-unlimited")
                        
                        @schemas.classproperty
                        def FURTHEREDUCATIONORSIXTHFORMCOLLEGECORPORATION(cls):
                            return cls("further-education-or-sixth-form-college-corporation")
                        
                        @schemas.classproperty
                        def LIMITEDLIABILITYPARTNERSHIP(cls):
                            return cls("limited-liability-partnership")
                        
                        @schemas.classproperty
                        def ASSURANCECOMPANY(cls):
                            return cls("assurance-company")
                        
                        @schemas.classproperty
                        def OTHER(cls):
                            return cls("other")
                        
                        @schemas.classproperty
                        def NORTHERNIRELANDOTHER(cls):
                            return cls("northern-ireland-other")
                        
                        @schemas.classproperty
                        def CHARITABLEINCORPORATEDORGANISATION(cls):
                            return cls("charitable-incorporated-organisation")
                        
                        @schemas.classproperty
                        def OVERSEACOMPANY(cls):
                            return cls("oversea-company")
                        
                        @schemas.classproperty
                        def ICVCSECURITIES(cls):
                            return cls("icvc-securities")
                        
                        @schemas.classproperty
                        def UKESTABLISHMENT(cls):
                            return cls("uk-establishment")
                        
                        @schemas.classproperty
                        def UNREGISTEREDCOMPANY(cls):
                            return cls("unregistered-company")
                        
                        @schemas.classproperty
                        def ICVCWARRANT(cls):
                            return cls("icvc-warrant")
                        
                        @schemas.classproperty
                        def REGISTEREDOVERSEASENTITY(cls):
                            return cls("registered-overseas-entity")
                        
                        @schemas.classproperty
                        def PUBLICLIMITEDCOMPANY(cls):
                            return cls("public-limited-company")
                        
                        @schemas.classproperty
                        def PRIVATELIMITEDCOMPANY(cls):
                            return cls("private-limited-company")
                        
                        @schemas.classproperty
                        def EUROPEANPUBLICLIMITEDLIABILITYCOMPANYSE(cls):
                            return cls("european-public-limited-liability-company-se")
                        
                        @schemas.classproperty
                        def PRIVATEUNLIMTEDNSC(cls):
                            return cls("private-unlimted-nsc")
                        
                        @schemas.classproperty
                        def NORTHERNIRELAND(cls):
                            return cls("northern-ireland")
                        
                        @schemas.classproperty
                        def ICVCUMBRELLA(cls):
                            return cls("icvc-umbrella")
                        
                        @schemas.classproperty
                        def SCOTTISHPARTNERSHIP(cls):
                            return cls("scottish-partnership")
                    
                    
                    class telephone_number(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'(\+[1-9])?\d{1,14}',
                            }]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'telephone_number':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    building_number = schemas.StrSchema
                    
                    
                    class country_code(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 2
                            min_length = 2
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'country_code':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    date_of_incorporation = schemas.DateSchema
                    
                    
                    class entity_registration_number(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            min_length = 1
                    __annotations__ = {
                        "email-address": email_address,
                        "claim-type": claim_type,
                        "city": city,
                        "building-name": building_name,
                        "street-name": street_name,
                        "entity-name": entity_name,
                        "postal-code": postal_code,
                        "corporation-type": corporation_type,
                        "telephone-number": telephone_number,
                        "building-number": building_number,
                        "country-code": country_code,
                        "date-of-incorporation": date_of_incorporation,
                        "entity-registration-number": entity_registration_number,
                    }
            
            city: MetaOapg.properties.city
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["email-address"]) -> MetaOapg.properties.email_address: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["street-name"]) -> MetaOapg.properties.street_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["entity-name"]) -> MetaOapg.properties.entity_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["postal-code"]) -> MetaOapg.properties.postal_code: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["corporation-type"]) -> MetaOapg.properties.corporation_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["telephone-number"]) -> MetaOapg.properties.telephone_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["country-code"]) -> MetaOapg.properties.country_code: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["date-of-incorporation"]) -> MetaOapg.properties.date_of_incorporation: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["entity-registration-number"]) -> MetaOapg.properties.entity_registration_number: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["email-address", "claim-type", "city", "building-name", "street-name", "entity-name", "postal-code", "corporation-type", "telephone-number", "building-number", "country-code", "date-of-incorporation", "entity-registration-number", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["email-address"]) -> typing.Union[MetaOapg.properties.email_address, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["building-name"]) -> typing.Union[MetaOapg.properties.building_name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["street-name"]) -> MetaOapg.properties.street_name: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["entity-name"]) -> MetaOapg.properties.entity_name: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["postal-code"]) -> MetaOapg.properties.postal_code: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["corporation-type"]) -> MetaOapg.properties.corporation_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["telephone-number"]) -> typing.Union[MetaOapg.properties.telephone_number, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["building-number"]) -> typing.Union[MetaOapg.properties.building_number, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["country-code"]) -> MetaOapg.properties.country_code: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["date-of-incorporation"]) -> typing.Union[MetaOapg.properties.date_of_incorporation, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["entity-registration-number"]) -> MetaOapg.properties.entity_registration_number: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email-address", "claim-type", "city", "building-name", "street-name", "entity-name", "postal-code", "corporation-type", "telephone-number", "building-number", "country-code", "date-of-incorporation", "entity-registration-number", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                city: typing.Union[MetaOapg.properties.city, str, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_3':
                return super().__new__(
                    cls,
                    *args,
                    city=city,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_4(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "income",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class income(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "currency",
                                "value",
                            }
                            
                            class properties:
                                
                                
                                class currency(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        enum_value_to_name = {
                                            "GBP": "GBP",
                                        }
                                    
                                    @schemas.classproperty
                                    def GBP(cls):
                                        return cls("GBP")
                                value = schemas.StrSchema
                                __annotations__ = {
                                    "currency": currency,
                                    "value": value,
                                }
                        
                        currency: MetaOapg.properties.currency
                        value: MetaOapg.properties.value
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["currency", "value", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currency", "value", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            currency: typing.Union[MetaOapg.properties.currency, str, ],
                            value: typing.Union[MetaOapg.properties.value, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'income':
                            return super().__new__(
                                cls,
                                *args,
                                currency=currency,
                                value=value,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "individual-income": "INDIVIDUALINCOME",
                            }
                        
                        @schemas.classproperty
                        def INDIVIDUALINCOME(cls):
                            return cls("individual-income")
                    __annotations__ = {
                        "income": income,
                        "claim-type": claim_type,
                    }
            
            income: MetaOapg.properties.income
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["income"]) -> MetaOapg.properties.income: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["income", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["income"]) -> MetaOapg.properties.income: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["income", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                income: typing.Union[MetaOapg.properties.income, dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_4':
                return super().__new__(
                    cls,
                    *args,
                    income=income,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_5(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "initial-deposit",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class initial_deposit(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "currency",
                                "value",
                            }
                            
                            class properties:
                                
                                
                                class currency(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        enum_value_to_name = {
                                            "GBP": "GBP",
                                        }
                                    
                                    @schemas.classproperty
                                    def GBP(cls):
                                        return cls("GBP")
                                value = schemas.StrSchema
                                __annotations__ = {
                                    "currency": currency,
                                    "value": value,
                                }
                        
                        currency: MetaOapg.properties.currency
                        value: MetaOapg.properties.value
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["currency", "value", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currency", "value", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            currency: typing.Union[MetaOapg.properties.currency, str, ],
                            value: typing.Union[MetaOapg.properties.value, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'initial_deposit':
                            return super().__new__(
                                cls,
                                *args,
                                currency=currency,
                                value=value,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "initial-deposit": "INITIALDEPOSIT",
                            }
                        
                        @schemas.classproperty
                        def INITIALDEPOSIT(cls):
                            return cls("initial-deposit")
                    __annotations__ = {
                        "initial-deposit": initial_deposit,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["initial-deposit"]) -> MetaOapg.properties.initial_deposit: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["initial-deposit", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["initial-deposit"]) -> MetaOapg.properties.initial_deposit: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["initial-deposit", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_5':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_6(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "international-payments-countries",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class international_payments_countries(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class items(
                                schemas.AnyTypeSchema,
                            ):
                            
                            
                                class MetaOapg:
                                    max_length = 2
                                    min_length = 2
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'items':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'international_payments_countries':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "international-payments-countries": "INTERNATIONALPAYMENTSCOUNTRIES",
                            }
                        
                        @schemas.classproperty
                        def INTERNATIONALPAYMENTSCOUNTRIES(cls):
                            return cls("international-payments-countries")
                    __annotations__ = {
                        "international-payments-countries": international_payments_countries,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["international-payments-countries"]) -> MetaOapg.properties.international_payments_countries: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["international-payments-countries", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["international-payments-countries"]) -> MetaOapg.properties.international_payments_countries: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["international-payments-countries", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_6':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_7(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "telephone-number",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class telephone_number(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'(\+[1-9])?\d{1,14}',
                            }]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'telephone_number':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "company-telephone-number": "COMPANYTELEPHONENUMBER",
                            }
                        
                        @schemas.classproperty
                        def COMPANYTELEPHONENUMBER(cls):
                            return cls("company-telephone-number")
                    __annotations__ = {
                        "telephone-number": telephone_number,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["telephone-number"]) -> MetaOapg.properties.telephone_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["telephone-number", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["telephone-number"]) -> MetaOapg.properties.telephone_number: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["telephone-number", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_7':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_8(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "legal-person-url",
                    "claim-type",
                    "ownership-percent",
                }
                
                class properties:
                    legal_person_url = schemas.StrSchema
                    ownership_percent = schemas.StrSchema
                    companies_house_url = schemas.StrSchema
                    senior_manager = schemas.BoolSchema
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "person-with-significant-control": "PERSONWITHSIGNIFICANTCONTROL",
                            }
                        
                        @schemas.classproperty
                        def PERSONWITHSIGNIFICANTCONTROL(cls):
                            return cls("person-with-significant-control")
                    __annotations__ = {
                        "legal-person-url": legal_person_url,
                        "ownership-percent": ownership_percent,
                        "companies-house-url": companies_house_url,
                        "senior-manager?": senior_manager,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["legal-person-url"]) -> MetaOapg.properties.legal_person_url: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["ownership-percent"]) -> MetaOapg.properties.ownership_percent: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["companies-house-url"]) -> MetaOapg.properties.companies_house_url: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["senior-manager?"]) -> MetaOapg.properties.senior_manager: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["legal-person-url", "ownership-percent", "companies-house-url", "senior-manager?", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["legal-person-url"]) -> MetaOapg.properties.legal_person_url: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["ownership-percent"]) -> MetaOapg.properties.ownership_percent: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["companies-house-url"]) -> typing.Union[MetaOapg.properties.companies_house_url, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["senior-manager?"]) -> typing.Union[MetaOapg.properties.senior_manager, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["legal-person-url", "ownership-percent", "companies-house-url", "senior-manager?", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_8':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_9(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "email-address",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class email_address(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'.+\@.+\..+',
                            }]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'email_address':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "company-email-address": "COMPANYEMAILADDRESS",
                            }
                        
                        @schemas.classproperty
                        def COMPANYEMAILADDRESS(cls):
                            return cls("company-email-address")
                    __annotations__ = {
                        "email-address": email_address,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["email-address"]) -> MetaOapg.properties.email_address: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["email-address", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["email-address"]) -> MetaOapg.properties.email_address: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email-address", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_9':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_10(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "claim-type",
                    "tax-residency",
                }
                
                class properties:
                    
                    
                    class tax_residency(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 2
                            min_length = 2
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'tax_residency':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "tax-residency": "TAXRESIDENCY",
                            }
                        
                        @schemas.classproperty
                        def TAXRESIDENCY(cls):
                            return cls("tax-residency")
                    __annotations__ = {
                        "tax-residency": tax_residency,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["tax-residency"]) -> MetaOapg.properties.tax_residency: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["tax-residency", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["tax-residency"]) -> MetaOapg.properties.tax_residency: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tax-residency", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_10':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_11(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "uk-regulatory-permissions",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class uk_regulatory_permissions(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class items(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "electronic-money-institution": "ELECTRONICMONEYINSTITUTION",
                                        "payment-institution": "PAYMENTINSTITUTION",
                                        "client-money": "CLIENTMONEY",
                                        "bank": "BANK",
                                    }
                                
                                @schemas.classproperty
                                def ELECTRONICMONEYINSTITUTION(cls):
                                    return cls("electronic-money-institution")
                                
                                @schemas.classproperty
                                def PAYMENTINSTITUTION(cls):
                                    return cls("payment-institution")
                                
                                @schemas.classproperty
                                def CLIENTMONEY(cls):
                                    return cls("client-money")
                                
                                @schemas.classproperty
                                def BANK(cls):
                                    return cls("bank")
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'uk_regulatory_permissions':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    date_of_incorporation = schemas.DateSchema
                    entity_name = schemas.StrSchema
                    
                    
                    class entity_registration_number(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            min_length = 1
                    
                    
                    class corporation_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "private-limited-guarant-nsc-limited-exemption": "PRIVATELIMITEDGUARANTNSCLIMITEDEXEMPTION",
                                "eeig": "EEIG",
                                "private-limited-shares-section-30-exemption": "PRIVATELIMITEDSHARESSECTION30EXEMPTION",
                                "limited-partnership": "LIMITEDPARTNERSHIP",
                                "royal-charter": "ROYALCHARTER",
                                "private-unlimited-nsc": "PRIVATEUNLIMITEDNSC",
                                "old-public-company": "OLDPUBLICCOMPANY",
                                "investment-company-with-variable-capital": "INVESTMENTCOMPANYWITHVARIABLECAPITAL",
                                "other-company-type": "OTHERCOMPANYTYPE",
                                "converted-or-closed": "CONVERTEDORCLOSED",
                                "protected-cell-company": "PROTECTEDCELLCOMPANY",
                                "private-limited-guarant-nsc": "PRIVATELIMITEDGUARANTNSC",
                                "scottish-charitable-incorporated-organisation": "SCOTTISHCHARITABLEINCORPORATEDORGANISATION",
                                "industrial-and-provident-society": "INDUSTRIALANDPROVIDENTSOCIETY",
                                "registered-society-non-jurisdictional": "REGISTEREDSOCIETYNONJURISDICTIONAL",
                                "private-unlimited": "PRIVATEUNLIMITED",
                                "further-education-or-sixth-form-college-corporation": "FURTHEREDUCATIONORSIXTHFORMCOLLEGECORPORATION",
                                "limited-liability-partnership": "LIMITEDLIABILITYPARTNERSHIP",
                                "assurance-company": "ASSURANCECOMPANY",
                                "other": "OTHER",
                                "northern-ireland-other": "NORTHERNIRELANDOTHER",
                                "charitable-incorporated-organisation": "CHARITABLEINCORPORATEDORGANISATION",
                                "oversea-company": "OVERSEACOMPANY",
                                "icvc-securities": "ICVCSECURITIES",
                                "uk-establishment": "UKESTABLISHMENT",
                                "unregistered-company": "UNREGISTEREDCOMPANY",
                                "icvc-warrant": "ICVCWARRANT",
                                "registered-overseas-entity": "REGISTEREDOVERSEASENTITY",
                                "public-limited-company": "PUBLICLIMITEDCOMPANY",
                                "private-limited-company": "PRIVATELIMITEDCOMPANY",
                                "european-public-limited-liability-company-se": "EUROPEANPUBLICLIMITEDLIABILITYCOMPANYSE",
                                "private-unlimted-nsc": "PRIVATEUNLIMTEDNSC",
                                "northern-ireland": "NORTHERNIRELAND",
                                "icvc-umbrella": "ICVCUMBRELLA",
                                "scottish-partnership": "SCOTTISHPARTNERSHIP",
                            }
                        
                        @schemas.classproperty
                        def PRIVATELIMITEDGUARANTNSCLIMITEDEXEMPTION(cls):
                            return cls("private-limited-guarant-nsc-limited-exemption")
                        
                        @schemas.classproperty
                        def EEIG(cls):
                            return cls("eeig")
                        
                        @schemas.classproperty
                        def PRIVATELIMITEDSHARESSECTION30EXEMPTION(cls):
                            return cls("private-limited-shares-section-30-exemption")
                        
                        @schemas.classproperty
                        def LIMITEDPARTNERSHIP(cls):
                            return cls("limited-partnership")
                        
                        @schemas.classproperty
                        def ROYALCHARTER(cls):
                            return cls("royal-charter")
                        
                        @schemas.classproperty
                        def PRIVATEUNLIMITEDNSC(cls):
                            return cls("private-unlimited-nsc")
                        
                        @schemas.classproperty
                        def OLDPUBLICCOMPANY(cls):
                            return cls("old-public-company")
                        
                        @schemas.classproperty
                        def INVESTMENTCOMPANYWITHVARIABLECAPITAL(cls):
                            return cls("investment-company-with-variable-capital")
                        
                        @schemas.classproperty
                        def OTHERCOMPANYTYPE(cls):
                            return cls("other-company-type")
                        
                        @schemas.classproperty
                        def CONVERTEDORCLOSED(cls):
                            return cls("converted-or-closed")
                        
                        @schemas.classproperty
                        def PROTECTEDCELLCOMPANY(cls):
                            return cls("protected-cell-company")
                        
                        @schemas.classproperty
                        def PRIVATELIMITEDGUARANTNSC(cls):
                            return cls("private-limited-guarant-nsc")
                        
                        @schemas.classproperty
                        def SCOTTISHCHARITABLEINCORPORATEDORGANISATION(cls):
                            return cls("scottish-charitable-incorporated-organisation")
                        
                        @schemas.classproperty
                        def INDUSTRIALANDPROVIDENTSOCIETY(cls):
                            return cls("industrial-and-provident-society")
                        
                        @schemas.classproperty
                        def REGISTEREDSOCIETYNONJURISDICTIONAL(cls):
                            return cls("registered-society-non-jurisdictional")
                        
                        @schemas.classproperty
                        def PRIVATEUNLIMITED(cls):
                            return cls("private-unlimited")
                        
                        @schemas.classproperty
                        def FURTHEREDUCATIONORSIXTHFORMCOLLEGECORPORATION(cls):
                            return cls("further-education-or-sixth-form-college-corporation")
                        
                        @schemas.classproperty
                        def LIMITEDLIABILITYPARTNERSHIP(cls):
                            return cls("limited-liability-partnership")
                        
                        @schemas.classproperty
                        def ASSURANCECOMPANY(cls):
                            return cls("assurance-company")
                        
                        @schemas.classproperty
                        def OTHER(cls):
                            return cls("other")
                        
                        @schemas.classproperty
                        def NORTHERNIRELANDOTHER(cls):
                            return cls("northern-ireland-other")
                        
                        @schemas.classproperty
                        def CHARITABLEINCORPORATEDORGANISATION(cls):
                            return cls("charitable-incorporated-organisation")
                        
                        @schemas.classproperty
                        def OVERSEACOMPANY(cls):
                            return cls("oversea-company")
                        
                        @schemas.classproperty
                        def ICVCSECURITIES(cls):
                            return cls("icvc-securities")
                        
                        @schemas.classproperty
                        def UKESTABLISHMENT(cls):
                            return cls("uk-establishment")
                        
                        @schemas.classproperty
                        def UNREGISTEREDCOMPANY(cls):
                            return cls("unregistered-company")
                        
                        @schemas.classproperty
                        def ICVCWARRANT(cls):
                            return cls("icvc-warrant")
                        
                        @schemas.classproperty
                        def REGISTEREDOVERSEASENTITY(cls):
                            return cls("registered-overseas-entity")
                        
                        @schemas.classproperty
                        def PUBLICLIMITEDCOMPANY(cls):
                            return cls("public-limited-company")
                        
                        @schemas.classproperty
                        def PRIVATELIMITEDCOMPANY(cls):
                            return cls("private-limited-company")
                        
                        @schemas.classproperty
                        def EUROPEANPUBLICLIMITEDLIABILITYCOMPANYSE(cls):
                            return cls("european-public-limited-liability-company-se")
                        
                        @schemas.classproperty
                        def PRIVATEUNLIMTEDNSC(cls):
                            return cls("private-unlimted-nsc")
                        
                        @schemas.classproperty
                        def NORTHERNIRELAND(cls):
                            return cls("northern-ireland")
                        
                        @schemas.classproperty
                        def ICVCUMBRELLA(cls):
                            return cls("icvc-umbrella")
                        
                        @schemas.classproperty
                        def SCOTTISHPARTNERSHIP(cls):
                            return cls("scottish-partnership")
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "uk-financial-services-register": "UKFINANCIALSERVICESREGISTER",
                            }
                        
                        @schemas.classproperty
                        def UKFINANCIALSERVICESREGISTER(cls):
                            return cls("uk-financial-services-register")
                    __annotations__ = {
                        "uk-regulatory-permissions": uk_regulatory_permissions,
                        "date-of-incorporation": date_of_incorporation,
                        "entity-name": entity_name,
                        "entity-registration-number": entity_registration_number,
                        "corporation-type": corporation_type,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["uk-regulatory-permissions"]) -> MetaOapg.properties.uk_regulatory_permissions: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["date-of-incorporation"]) -> MetaOapg.properties.date_of_incorporation: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["entity-name"]) -> MetaOapg.properties.entity_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["entity-registration-number"]) -> MetaOapg.properties.entity_registration_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["corporation-type"]) -> MetaOapg.properties.corporation_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["uk-regulatory-permissions", "date-of-incorporation", "entity-name", "entity-registration-number", "corporation-type", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["uk-regulatory-permissions"]) -> MetaOapg.properties.uk_regulatory_permissions: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["date-of-incorporation"]) -> typing.Union[MetaOapg.properties.date_of_incorporation, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["entity-name"]) -> typing.Union[MetaOapg.properties.entity_name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["entity-registration-number"]) -> typing.Union[MetaOapg.properties.entity_registration_number, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["corporation-type"]) -> typing.Union[MetaOapg.properties.corporation_type, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uk-regulatory-permissions", "date-of-incorporation", "entity-name", "entity-registration-number", "corporation-type", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_11':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_12(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "business-description",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class business_description(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            min_length = 1
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "business-description": "BUSINESSDESCRIPTION",
                            }
                        
                        @schemas.classproperty
                        def BUSINESSDESCRIPTION(cls):
                            return cls("business-description")
                    __annotations__ = {
                        "business-description": business_description,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["business-description"]) -> MetaOapg.properties.business_description: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["business-description", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["business-description"]) -> MetaOapg.properties.business_description: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["business-description", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_12':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_13(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "individual-sources-of-funds",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class individual_sources_of_funds(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            unique_items = True
                            
                            
                            class items(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "gambling-or-lottery": "GAMBLINGORLOTTERY",
                                        "investments": "INVESTMENTS",
                                        "property-or-asset-sale": "PROPERTYORASSETSALE",
                                        "savings": "SAVINGS",
                                        "salary-or-bonus": "SALARYORBONUS",
                                        "student-loans-or-bursary": "STUDENTLOANSORBURSARY",
                                        "retirement-or-pension": "RETIREMENTORPENSION",
                                        "legal-settlement": "LEGALSETTLEMENT",
                                        "family-or-gifted": "FAMILYORGIFTED",
                                        "loan": "LOAN",
                                        "inheritance": "INHERITANCE",
                                    }
                                
                                @schemas.classproperty
                                def GAMBLINGORLOTTERY(cls):
                                    return cls("gambling-or-lottery")
                                
                                @schemas.classproperty
                                def INVESTMENTS(cls):
                                    return cls("investments")
                                
                                @schemas.classproperty
                                def PROPERTYORASSETSALE(cls):
                                    return cls("property-or-asset-sale")
                                
                                @schemas.classproperty
                                def SAVINGS(cls):
                                    return cls("savings")
                                
                                @schemas.classproperty
                                def SALARYORBONUS(cls):
                                    return cls("salary-or-bonus")
                                
                                @schemas.classproperty
                                def STUDENTLOANSORBURSARY(cls):
                                    return cls("student-loans-or-bursary")
                                
                                @schemas.classproperty
                                def RETIREMENTORPENSION(cls):
                                    return cls("retirement-or-pension")
                                
                                @schemas.classproperty
                                def LEGALSETTLEMENT(cls):
                                    return cls("legal-settlement")
                                
                                @schemas.classproperty
                                def FAMILYORGIFTED(cls):
                                    return cls("family-or-gifted")
                                
                                @schemas.classproperty
                                def LOAN(cls):
                                    return cls("loan")
                                
                                @schemas.classproperty
                                def INHERITANCE(cls):
                                    return cls("inheritance")
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'individual_sources_of_funds':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "individual-sources-of-funds": "INDIVIDUALSOURCESOFFUNDS",
                            }
                        
                        @schemas.classproperty
                        def INDIVIDUALSOURCESOFFUNDS(cls):
                            return cls("individual-sources-of-funds")
                    __annotations__ = {
                        "individual-sources-of-funds": individual_sources_of_funds,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["individual-sources-of-funds"]) -> MetaOapg.properties.individual_sources_of_funds: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["individual-sources-of-funds", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["individual-sources-of-funds"]) -> MetaOapg.properties.individual_sources_of_funds: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["individual-sources-of-funds", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_13':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_14(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "business-address",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class business_address(
                        schemas.ComposedBase,
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "country-code",
                                "postal-code",
                                "city",
                                "street-name",
                            }
                            
                            class properties:
                                street_name = schemas.StrSchema
                                city = schemas.StrSchema
                                
                                
                                class postal_code(
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        max_length = 10
                                        min_length = 0
                                
                                
                                class country_code(
                                    schemas.AnyTypeSchema,
                                ):
                                
                                
                                    class MetaOapg:
                                        max_length = 2
                                        min_length = 2
                                
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'country_code':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                __annotations__ = {
                                    "street-name": street_name,
                                    "city": city,
                                    "postal-code": postal_code,
                                    "country-code": country_code,
                                }
                            
                            
                            class any_of_0(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "building-number",
                                        "building-name",
                                    }
                                    
                                    class properties:
                                        building_name = schemas.StrSchema
                                        building_number = schemas.StrSchema
                                        __annotations__ = {
                                            "building-name": building_name,
                                            "building-number": building_number,
                                        }
                                
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["building-name", "building-number", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building-name", "building-number", ], str]):
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
                            
                            
                            class any_of_1(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "building-name",
                                    }
                                    
                                    class properties:
                                        building_name = schemas.StrSchema
                                        __annotations__ = {
                                            "building-name": building_name,
                                        }
                                
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["building-name", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building-name", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'any_of_1':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            
                            class any_of_2(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "building-number",
                                    }
                                    
                                    class properties:
                                        building_number = schemas.StrSchema
                                        __annotations__ = {
                                            "building-number": building_number,
                                        }
                                
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["building-number", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building-number", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'any_of_2':
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
                                    cls.any_of_1,
                                    cls.any_of_2,
                                ]
                    
                        
                        city: MetaOapg.properties.city
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["street-name"]) -> MetaOapg.properties.street_name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["postal-code"]) -> MetaOapg.properties.postal_code: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["country-code"]) -> MetaOapg.properties.country_code: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["street-name", "city", "postal-code", "country-code", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["street-name"]) -> MetaOapg.properties.street_name: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["postal-code"]) -> MetaOapg.properties.postal_code: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["country-code"]) -> MetaOapg.properties.country_code: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["street-name", "city", "postal-code", "country-code", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            city: typing.Union[MetaOapg.properties.city, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'business_address':
                            return super().__new__(
                                cls,
                                *args,
                                city=city,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "business-address": "BUSINESSADDRESS",
                            }
                        
                        @schemas.classproperty
                        def BUSINESSADDRESS(cls):
                            return cls("business-address")
                    __annotations__ = {
                        "business-address": business_address,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["business-address"]) -> MetaOapg.properties.business_address: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["business-address", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["business-address"]) -> MetaOapg.properties.business_address: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["business-address", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_14':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_15(
            schemas.ComposedBase,
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "employment-status",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "employment": "EMPLOYMENT",
                            }
                        
                        @schemas.classproperty
                        def EMPLOYMENT(cls):
                            return cls("employment")
                    __annotations__ = {
                        "claim-type": claim_type,
                    }
                
                
                class any_of_0(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "occupation",
                            "employment-status",
                            "industry-of-occupation",
                        }
                        
                        class properties:
                            occupation = schemas.StrSchema
                            
                            
                            class industry_of_occupation(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "property-and-construction": "PROPERTYANDCONSTRUCTION",
                                        "recruitment-and-hr": "RECRUITMENTANDHR",
                                        "creative-arts-and-design": "CREATIVEARTSANDDESIGN",
                                        "healthcare": "HEALTHCARE",
                                        "teacher-training-and-education": "TEACHERTRAININGANDEDUCATION",
                                        "engineering-and-manufacturing": "ENGINEERINGANDMANUFACTURING",
                                        "business-consulting-and-management": "BUSINESSCONSULTINGANDMANAGEMENT",
                                        "leisure-sport-and-tourism": "LEISURESPORTANDTOURISM",
                                        "transport-and-logistics": "TRANSPORTANDLOGISTICS",
                                        "charity-and-not-for-profit-organizations": "CHARITYANDNOTFORPROFITORGANIZATIONS",
                                        "social-and-humanities-scientists": "SOCIALANDHUMANITIESSCIENTISTS",
                                        "science-and-pharmaceuticals": "SCIENCEANDPHARMACEUTICALS",
                                        "retail-and-wholesale": "RETAILANDWHOLESALE",
                                        "social-care": "SOCIALCARE",
                                        "accountancy-banking-and-finance": "ACCOUNTANCYBANKINGANDFINANCE",
                                        "marketing-advertising-and-pr": "MARKETINGADVERTISINGANDPR",
                                        "law": "LAW",
                                        "hospitality-and-events-management": "HOSPITALITYANDEVENTSMANAGEMENT",
                                        "sales": "SALES",
                                        "environment-and-agriculture": "ENVIRONMENTANDAGRICULTURE",
                                        "media-and-internet": "MEDIAANDINTERNET",
                                        "personal-care-and-lifestyle": "PERSONALCAREANDLIFESTYLE",
                                        "information-technology": "INFORMATIONTECHNOLOGY",
                                        "law-enforcement-and-security": "LAWENFORCEMENTANDSECURITY",
                                        "public-services-and-administration": "PUBLICSERVICESANDADMINISTRATION",
                                        "energy-and-utilities": "ENERGYANDUTILITIES",
                                    }
                                
                                @schemas.classproperty
                                def PROPERTYANDCONSTRUCTION(cls):
                                    return cls("property-and-construction")
                                
                                @schemas.classproperty
                                def RECRUITMENTANDHR(cls):
                                    return cls("recruitment-and-hr")
                                
                                @schemas.classproperty
                                def CREATIVEARTSANDDESIGN(cls):
                                    return cls("creative-arts-and-design")
                                
                                @schemas.classproperty
                                def HEALTHCARE(cls):
                                    return cls("healthcare")
                                
                                @schemas.classproperty
                                def TEACHERTRAININGANDEDUCATION(cls):
                                    return cls("teacher-training-and-education")
                                
                                @schemas.classproperty
                                def ENGINEERINGANDMANUFACTURING(cls):
                                    return cls("engineering-and-manufacturing")
                                
                                @schemas.classproperty
                                def BUSINESSCONSULTINGANDMANAGEMENT(cls):
                                    return cls("business-consulting-and-management")
                                
                                @schemas.classproperty
                                def LEISURESPORTANDTOURISM(cls):
                                    return cls("leisure-sport-and-tourism")
                                
                                @schemas.classproperty
                                def TRANSPORTANDLOGISTICS(cls):
                                    return cls("transport-and-logistics")
                                
                                @schemas.classproperty
                                def CHARITYANDNOTFORPROFITORGANIZATIONS(cls):
                                    return cls("charity-and-not-for-profit-organizations")
                                
                                @schemas.classproperty
                                def SOCIALANDHUMANITIESSCIENTISTS(cls):
                                    return cls("social-and-humanities-scientists")
                                
                                @schemas.classproperty
                                def SCIENCEANDPHARMACEUTICALS(cls):
                                    return cls("science-and-pharmaceuticals")
                                
                                @schemas.classproperty
                                def RETAILANDWHOLESALE(cls):
                                    return cls("retail-and-wholesale")
                                
                                @schemas.classproperty
                                def SOCIALCARE(cls):
                                    return cls("social-care")
                                
                                @schemas.classproperty
                                def ACCOUNTANCYBANKINGANDFINANCE(cls):
                                    return cls("accountancy-banking-and-finance")
                                
                                @schemas.classproperty
                                def MARKETINGADVERTISINGANDPR(cls):
                                    return cls("marketing-advertising-and-pr")
                                
                                @schemas.classproperty
                                def LAW(cls):
                                    return cls("law")
                                
                                @schemas.classproperty
                                def HOSPITALITYANDEVENTSMANAGEMENT(cls):
                                    return cls("hospitality-and-events-management")
                                
                                @schemas.classproperty
                                def SALES(cls):
                                    return cls("sales")
                                
                                @schemas.classproperty
                                def ENVIRONMENTANDAGRICULTURE(cls):
                                    return cls("environment-and-agriculture")
                                
                                @schemas.classproperty
                                def MEDIAANDINTERNET(cls):
                                    return cls("media-and-internet")
                                
                                @schemas.classproperty
                                def PERSONALCAREANDLIFESTYLE(cls):
                                    return cls("personal-care-and-lifestyle")
                                
                                @schemas.classproperty
                                def INFORMATIONTECHNOLOGY(cls):
                                    return cls("information-technology")
                                
                                @schemas.classproperty
                                def LAWENFORCEMENTANDSECURITY(cls):
                                    return cls("law-enforcement-and-security")
                                
                                @schemas.classproperty
                                def PUBLICSERVICESANDADMINISTRATION(cls):
                                    return cls("public-services-and-administration")
                                
                                @schemas.classproperty
                                def ENERGYANDUTILITIES(cls):
                                    return cls("energy-and-utilities")
                            
                            
                            class employment_status(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "self-employed": "SELFEMPLOYED",
                                    }
                                
                                @schemas.classproperty
                                def SELFEMPLOYED(cls):
                                    return cls("self-employed")
                            __annotations__ = {
                                "occupation": occupation,
                                "industry-of-occupation": industry_of_occupation,
                                "employment-status": employment_status,
                            }
                    
                    occupation: MetaOapg.properties.occupation
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["occupation"]) -> MetaOapg.properties.occupation: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["industry-of-occupation"]) -> MetaOapg.properties.industry_of_occupation: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["employment-status"]) -> MetaOapg.properties.employment_status: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["occupation", "industry-of-occupation", "employment-status", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["occupation"]) -> MetaOapg.properties.occupation: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["industry-of-occupation"]) -> MetaOapg.properties.industry_of_occupation: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["employment-status"]) -> MetaOapg.properties.employment_status: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["occupation", "industry-of-occupation", "employment-status", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        occupation: typing.Union[MetaOapg.properties.occupation, str, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'any_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            occupation=occupation,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                
                class any_of_1(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "employment-status",
                        }
                        
                        class properties:
                            
                            
                            class employment_status(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "retired": "RETIRED",
                                    }
                                
                                @schemas.classproperty
                                def RETIRED(cls):
                                    return cls("retired")
                            __annotations__ = {
                                "employment-status": employment_status,
                            }
                    
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["employment-status"]) -> MetaOapg.properties.employment_status: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employment-status", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["employment-status"]) -> MetaOapg.properties.employment_status: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employment-status", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'any_of_1':
                        return super().__new__(
                            cls,
                            *args,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                
                class any_of_2(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "employment-status",
                        }
                        
                        class properties:
                            
                            
                            class employment_status(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "unemployed": "UNEMPLOYED",
                                    }
                                
                                @schemas.classproperty
                                def UNEMPLOYED(cls):
                                    return cls("unemployed")
                            __annotations__ = {
                                "employment-status": employment_status,
                            }
                    
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["employment-status"]) -> MetaOapg.properties.employment_status: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employment-status", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["employment-status"]) -> MetaOapg.properties.employment_status: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employment-status", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'any_of_2':
                        return super().__new__(
                            cls,
                            *args,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                
                class any_of_3(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "occupation",
                            "employment-status",
                            "industry-of-occupation",
                        }
                        
                        class properties:
                            occupation = schemas.StrSchema
                            
                            
                            class industry_of_occupation(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "property-and-construction": "PROPERTYANDCONSTRUCTION",
                                        "recruitment-and-hr": "RECRUITMENTANDHR",
                                        "creative-arts-and-design": "CREATIVEARTSANDDESIGN",
                                        "healthcare": "HEALTHCARE",
                                        "teacher-training-and-education": "TEACHERTRAININGANDEDUCATION",
                                        "engineering-and-manufacturing": "ENGINEERINGANDMANUFACTURING",
                                        "business-consulting-and-management": "BUSINESSCONSULTINGANDMANAGEMENT",
                                        "leisure-sport-and-tourism": "LEISURESPORTANDTOURISM",
                                        "transport-and-logistics": "TRANSPORTANDLOGISTICS",
                                        "charity-and-not-for-profit-organizations": "CHARITYANDNOTFORPROFITORGANIZATIONS",
                                        "social-and-humanities-scientists": "SOCIALANDHUMANITIESSCIENTISTS",
                                        "science-and-pharmaceuticals": "SCIENCEANDPHARMACEUTICALS",
                                        "retail-and-wholesale": "RETAILANDWHOLESALE",
                                        "social-care": "SOCIALCARE",
                                        "accountancy-banking-and-finance": "ACCOUNTANCYBANKINGANDFINANCE",
                                        "marketing-advertising-and-pr": "MARKETINGADVERTISINGANDPR",
                                        "law": "LAW",
                                        "hospitality-and-events-management": "HOSPITALITYANDEVENTSMANAGEMENT",
                                        "sales": "SALES",
                                        "environment-and-agriculture": "ENVIRONMENTANDAGRICULTURE",
                                        "media-and-internet": "MEDIAANDINTERNET",
                                        "personal-care-and-lifestyle": "PERSONALCAREANDLIFESTYLE",
                                        "information-technology": "INFORMATIONTECHNOLOGY",
                                        "law-enforcement-and-security": "LAWENFORCEMENTANDSECURITY",
                                        "public-services-and-administration": "PUBLICSERVICESANDADMINISTRATION",
                                        "energy-and-utilities": "ENERGYANDUTILITIES",
                                    }
                                
                                @schemas.classproperty
                                def PROPERTYANDCONSTRUCTION(cls):
                                    return cls("property-and-construction")
                                
                                @schemas.classproperty
                                def RECRUITMENTANDHR(cls):
                                    return cls("recruitment-and-hr")
                                
                                @schemas.classproperty
                                def CREATIVEARTSANDDESIGN(cls):
                                    return cls("creative-arts-and-design")
                                
                                @schemas.classproperty
                                def HEALTHCARE(cls):
                                    return cls("healthcare")
                                
                                @schemas.classproperty
                                def TEACHERTRAININGANDEDUCATION(cls):
                                    return cls("teacher-training-and-education")
                                
                                @schemas.classproperty
                                def ENGINEERINGANDMANUFACTURING(cls):
                                    return cls("engineering-and-manufacturing")
                                
                                @schemas.classproperty
                                def BUSINESSCONSULTINGANDMANAGEMENT(cls):
                                    return cls("business-consulting-and-management")
                                
                                @schemas.classproperty
                                def LEISURESPORTANDTOURISM(cls):
                                    return cls("leisure-sport-and-tourism")
                                
                                @schemas.classproperty
                                def TRANSPORTANDLOGISTICS(cls):
                                    return cls("transport-and-logistics")
                                
                                @schemas.classproperty
                                def CHARITYANDNOTFORPROFITORGANIZATIONS(cls):
                                    return cls("charity-and-not-for-profit-organizations")
                                
                                @schemas.classproperty
                                def SOCIALANDHUMANITIESSCIENTISTS(cls):
                                    return cls("social-and-humanities-scientists")
                                
                                @schemas.classproperty
                                def SCIENCEANDPHARMACEUTICALS(cls):
                                    return cls("science-and-pharmaceuticals")
                                
                                @schemas.classproperty
                                def RETAILANDWHOLESALE(cls):
                                    return cls("retail-and-wholesale")
                                
                                @schemas.classproperty
                                def SOCIALCARE(cls):
                                    return cls("social-care")
                                
                                @schemas.classproperty
                                def ACCOUNTANCYBANKINGANDFINANCE(cls):
                                    return cls("accountancy-banking-and-finance")
                                
                                @schemas.classproperty
                                def MARKETINGADVERTISINGANDPR(cls):
                                    return cls("marketing-advertising-and-pr")
                                
                                @schemas.classproperty
                                def LAW(cls):
                                    return cls("law")
                                
                                @schemas.classproperty
                                def HOSPITALITYANDEVENTSMANAGEMENT(cls):
                                    return cls("hospitality-and-events-management")
                                
                                @schemas.classproperty
                                def SALES(cls):
                                    return cls("sales")
                                
                                @schemas.classproperty
                                def ENVIRONMENTANDAGRICULTURE(cls):
                                    return cls("environment-and-agriculture")
                                
                                @schemas.classproperty
                                def MEDIAANDINTERNET(cls):
                                    return cls("media-and-internet")
                                
                                @schemas.classproperty
                                def PERSONALCAREANDLIFESTYLE(cls):
                                    return cls("personal-care-and-lifestyle")
                                
                                @schemas.classproperty
                                def INFORMATIONTECHNOLOGY(cls):
                                    return cls("information-technology")
                                
                                @schemas.classproperty
                                def LAWENFORCEMENTANDSECURITY(cls):
                                    return cls("law-enforcement-and-security")
                                
                                @schemas.classproperty
                                def PUBLICSERVICESANDADMINISTRATION(cls):
                                    return cls("public-services-and-administration")
                                
                                @schemas.classproperty
                                def ENERGYANDUTILITIES(cls):
                                    return cls("energy-and-utilities")
                            
                            
                            class employment_status(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "employed": "EMPLOYED",
                                    }
                                
                                @schemas.classproperty
                                def EMPLOYED(cls):
                                    return cls("employed")
                            __annotations__ = {
                                "occupation": occupation,
                                "industry-of-occupation": industry_of_occupation,
                                "employment-status": employment_status,
                            }
                    
                    occupation: MetaOapg.properties.occupation
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["occupation"]) -> MetaOapg.properties.occupation: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["industry-of-occupation"]) -> MetaOapg.properties.industry_of_occupation: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["employment-status"]) -> MetaOapg.properties.employment_status: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["occupation", "industry-of-occupation", "employment-status", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["occupation"]) -> MetaOapg.properties.occupation: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["industry-of-occupation"]) -> MetaOapg.properties.industry_of_occupation: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["employment-status"]) -> MetaOapg.properties.employment_status: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["occupation", "industry-of-occupation", "employment-status", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        occupation: typing.Union[MetaOapg.properties.occupation, str, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'any_of_3':
                        return super().__new__(
                            cls,
                            *args,
                            occupation=occupation,
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
                        cls.any_of_2,
                        cls.any_of_3,
                    ]
        
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_15':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_16(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "annual-turnover",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class annual_turnover(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "currency",
                                "value",
                            }
                            
                            class properties:
                                
                                
                                class currency(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        enum_value_to_name = {
                                            "GBP": "GBP",
                                        }
                                    
                                    @schemas.classproperty
                                    def GBP(cls):
                                        return cls("GBP")
                                value = schemas.StrSchema
                                __annotations__ = {
                                    "currency": currency,
                                    "value": value,
                                }
                        
                        currency: MetaOapg.properties.currency
                        value: MetaOapg.properties.value
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["currency", "value", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currency", "value", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            currency: typing.Union[MetaOapg.properties.currency, str, ],
                            value: typing.Union[MetaOapg.properties.value, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'annual_turnover':
                            return super().__new__(
                                cls,
                                *args,
                                currency=currency,
                                value=value,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "annual-turnover": "ANNUALTURNOVER",
                            }
                        
                        @schemas.classproperty
                        def ANNUALTURNOVER(cls):
                            return cls("annual-turnover")
                    __annotations__ = {
                        "annual-turnover": annual_turnover,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["annual-turnover"]) -> MetaOapg.properties.annual_turnover: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["annual-turnover", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["annual-turnover"]) -> MetaOapg.properties.annual_turnover: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["annual-turnover", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_16':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_17(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "purposes-of-account",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class purposes_of_account(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            unique_items = True
                            
                            
                            class items(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "short-term-investment": "SHORTTERMINVESTMENT",
                                        "long-term-investment": "LONGTERMINVESTMENT",
                                        "safeguarding": "SAFEGUARDING",
                                        "staff-payroll": "STAFFPAYROLL",
                                        "client-money": "CLIENTMONEY",
                                        "business-expenses": "BUSINESSEXPENSES",
                                        "receiving-payments": "RECEIVINGPAYMENTS",
                                        "operational-spend": "OPERATIONALSPEND",
                                    }
                                
                                @schemas.classproperty
                                def SHORTTERMINVESTMENT(cls):
                                    return cls("short-term-investment")
                                
                                @schemas.classproperty
                                def LONGTERMINVESTMENT(cls):
                                    return cls("long-term-investment")
                                
                                @schemas.classproperty
                                def SAFEGUARDING(cls):
                                    return cls("safeguarding")
                                
                                @schemas.classproperty
                                def STAFFPAYROLL(cls):
                                    return cls("staff-payroll")
                                
                                @schemas.classproperty
                                def CLIENTMONEY(cls):
                                    return cls("client-money")
                                
                                @schemas.classproperty
                                def BUSINESSEXPENSES(cls):
                                    return cls("business-expenses")
                                
                                @schemas.classproperty
                                def RECEIVINGPAYMENTS(cls):
                                    return cls("receiving-payments")
                                
                                @schemas.classproperty
                                def OPERATIONALSPEND(cls):
                                    return cls("operational-spend")
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'purposes_of_account':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "purposes-of-account": "PURPOSESOFACCOUNT",
                            }
                        
                        @schemas.classproperty
                        def PURPOSESOFACCOUNT(cls):
                            return cls("purposes-of-account")
                    __annotations__ = {
                        "purposes-of-account": purposes_of_account,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["purposes-of-account"]) -> MetaOapg.properties.purposes_of_account: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["purposes-of-account", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["purposes-of-account"]) -> MetaOapg.properties.purposes_of_account: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["purposes-of-account", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_17':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_18(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "sic-codes",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class sic_codes(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class items(
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    max_length = 5
                                    min_length = 4
                                    regex=[{
                                        'pattern': r'^[0-9]*$',
                                    }]
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'sic_codes':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "sic-codes": "SICCODES",
                            }
                        
                        @schemas.classproperty
                        def SICCODES(cls):
                            return cls("sic-codes")
                    __annotations__ = {
                        "sic-codes": sic_codes,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["sic-codes"]) -> MetaOapg.properties.sic_codes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["sic-codes", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["sic-codes"]) -> MetaOapg.properties.sic_codes: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sic-codes", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_18':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_19(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "international-operations-countries",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class international_operations_countries(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class items(
                                schemas.AnyTypeSchema,
                            ):
                            
                            
                                class MetaOapg:
                                    max_length = 2
                                    min_length = 2
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'items':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'international_operations_countries':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "international-operations-countries": "INTERNATIONALOPERATIONSCOUNTRIES",
                            }
                        
                        @schemas.classproperty
                        def INTERNATIONALOPERATIONSCOUNTRIES(cls):
                            return cls("international-operations-countries")
                    __annotations__ = {
                        "international-operations-countries": international_operations_countries,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["international-operations-countries"]) -> MetaOapg.properties.international_operations_countries: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["international-operations-countries", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["international-operations-countries"]) -> MetaOapg.properties.international_operations_countries: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["international-operations-countries", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_19':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_20(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "sources-of-funds",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class sources_of_funds(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            unique_items = True
                            
                            
                            class items(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "gambling-or-lottery": "GAMBLINGORLOTTERY",
                                        "investments": "INVESTMENTS",
                                        "property-or-asset-sale": "PROPERTYORASSETSALE",
                                        "business-income": "BUSINESSINCOME",
                                        "savings": "SAVINGS",
                                        "salary-or-bonus": "SALARYORBONUS",
                                        "student-loans-or-bursary": "STUDENTLOANSORBURSARY",
                                        "retirement-or-pension": "RETIREMENTORPENSION",
                                        "legal-settlement": "LEGALSETTLEMENT",
                                        "family-or-gifted": "FAMILYORGIFTED",
                                        "loan": "LOAN",
                                        "inheritance": "INHERITANCE",
                                    }
                                
                                @schemas.classproperty
                                def GAMBLINGORLOTTERY(cls):
                                    return cls("gambling-or-lottery")
                                
                                @schemas.classproperty
                                def INVESTMENTS(cls):
                                    return cls("investments")
                                
                                @schemas.classproperty
                                def PROPERTYORASSETSALE(cls):
                                    return cls("property-or-asset-sale")
                                
                                @schemas.classproperty
                                def BUSINESSINCOME(cls):
                                    return cls("business-income")
                                
                                @schemas.classproperty
                                def SAVINGS(cls):
                                    return cls("savings")
                                
                                @schemas.classproperty
                                def SALARYORBONUS(cls):
                                    return cls("salary-or-bonus")
                                
                                @schemas.classproperty
                                def STUDENTLOANSORBURSARY(cls):
                                    return cls("student-loans-or-bursary")
                                
                                @schemas.classproperty
                                def RETIREMENTORPENSION(cls):
                                    return cls("retirement-or-pension")
                                
                                @schemas.classproperty
                                def LEGALSETTLEMENT(cls):
                                    return cls("legal-settlement")
                                
                                @schemas.classproperty
                                def FAMILYORGIFTED(cls):
                                    return cls("family-or-gifted")
                                
                                @schemas.classproperty
                                def LOAN(cls):
                                    return cls("loan")
                                
                                @schemas.classproperty
                                def INHERITANCE(cls):
                                    return cls("inheritance")
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'sources_of_funds':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "sources-of-funds": "SOURCESOFFUNDS",
                            }
                        
                        @schemas.classproperty
                        def SOURCESOFFUNDS(cls):
                            return cls("sources-of-funds")
                    __annotations__ = {
                        "sources-of-funds": sources_of_funds,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["sources-of-funds"]) -> MetaOapg.properties.sources_of_funds: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["sources-of-funds", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["sources-of-funds"]) -> MetaOapg.properties.sources_of_funds: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sources-of-funds", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_20':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_21(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "email-address",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class email_address(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'.+\@.+\..+',
                            }]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'email_address':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class mobile_number(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'(\+[1-9])?\d{1,14}',
                            }]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'mobile_number':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class telephone_number(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'(\+[1-9])?\d{1,14}',
                            }]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'telephone_number':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "contact-details": "CONTACTDETAILS",
                            }
                        
                        @schemas.classproperty
                        def CONTACTDETAILS(cls):
                            return cls("contact-details")
                    __annotations__ = {
                        "email-address": email_address,
                        "mobile-number": mobile_number,
                        "telephone-number": telephone_number,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["email-address"]) -> MetaOapg.properties.email_address: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["mobile-number"]) -> MetaOapg.properties.mobile_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["telephone-number"]) -> MetaOapg.properties.telephone_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["email-address", "mobile-number", "telephone-number", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["email-address"]) -> MetaOapg.properties.email_address: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["mobile-number"]) -> typing.Union[MetaOapg.properties.mobile_number, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["telephone-number"]) -> typing.Union[MetaOapg.properties.telephone_number, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email-address", "mobile-number", "telephone-number", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_21':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_22(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "reliance-verification-methods",
                    "claim-type",
                    "reliance-verification-standard",
                }
                
                class properties:
                    
                    
                    class reliance_verification_methods(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            unique_items = True
                            
                            
                            class items(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "manual-document": "MANUALDOCUMENT",
                                        "physical": "PHYSICAL",
                                        "electronic": "ELECTRONIC",
                                        "manual-biometric": "MANUALBIOMETRIC",
                                    }
                                
                                @schemas.classproperty
                                def MANUALDOCUMENT(cls):
                                    return cls("manual-document")
                                
                                @schemas.classproperty
                                def PHYSICAL(cls):
                                    return cls("physical")
                                
                                @schemas.classproperty
                                def ELECTRONIC(cls):
                                    return cls("electronic")
                                
                                @schemas.classproperty
                                def MANUALBIOMETRIC(cls):
                                    return cls("manual-biometric")
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'reliance_verification_methods':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    
                    class reliance_verification_standard(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "jmlsg": "JMLSG",
                            }
                        
                        @schemas.classproperty
                        def JMLSG(cls):
                            return cls("jmlsg")
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "reliance-verification": "RELIANCEVERIFICATION",
                            }
                        
                        @schemas.classproperty
                        def RELIANCEVERIFICATION(cls):
                            return cls("reliance-verification")
                    __annotations__ = {
                        "reliance-verification-methods": reliance_verification_methods,
                        "reliance-verification-standard": reliance_verification_standard,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["reliance-verification-methods"]) -> MetaOapg.properties.reliance_verification_methods: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["reliance-verification-standard"]) -> MetaOapg.properties.reliance_verification_standard: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["reliance-verification-methods", "reliance-verification-standard", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["reliance-verification-methods"]) -> MetaOapg.properties.reliance_verification_methods: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["reliance-verification-standard"]) -> MetaOapg.properties.reliance_verification_standard: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["reliance-verification-methods", "reliance-verification-standard", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_22':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_23(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "business-name",
                    "claim-type",
                }
                
                class properties:
                    business_name = schemas.StrSchema
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "business-name": "BUSINESSNAME",
                            }
                        
                        @schemas.classproperty
                        def BUSINESSNAME(cls):
                            return cls("business-name")
                    __annotations__ = {
                        "business-name": business_name,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["business-name"]) -> MetaOapg.properties.business_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["business-name", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["business-name"]) -> MetaOapg.properties.business_name: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["business-name", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_23':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_24(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "individual-purposes-of-account",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class individual_purposes_of_account(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            unique_items = True
                            
                            
                            class items(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "savings": "SAVINGS",
                                        "bills-and-repayment": "BILLSANDREPAYMENT",
                                        "everyday-spending": "EVERYDAYSPENDING",
                                    }
                                
                                @schemas.classproperty
                                def SAVINGS(cls):
                                    return cls("savings")
                                
                                @schemas.classproperty
                                def BILLSANDREPAYMENT(cls):
                                    return cls("bills-and-repayment")
                                
                                @schemas.classproperty
                                def EVERYDAYSPENDING(cls):
                                    return cls("everyday-spending")
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'individual_purposes_of_account':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "individual-purposes-of-account": "INDIVIDUALPURPOSESOFACCOUNT",
                            }
                        
                        @schemas.classproperty
                        def INDIVIDUALPURPOSESOFACCOUNT(cls):
                            return cls("individual-purposes-of-account")
                    __annotations__ = {
                        "individual-purposes-of-account": individual_purposes_of_account,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["individual-purposes-of-account"]) -> MetaOapg.properties.individual_purposes_of_account: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["individual-purposes-of-account", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["individual-purposes-of-account"]) -> MetaOapg.properties.individual_purposes_of_account: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["individual-purposes-of-account", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_24':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_25(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "nationality",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class nationality(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 2
                            min_length = 2
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'nationality':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "nationality": "NATIONALITY",
                            }
                        
                        @schemas.classproperty
                        def NATIONALITY(cls):
                            return cls("nationality")
                    __annotations__ = {
                        "nationality": nationality,
                        "claim-type": claim_type,
                    }
            
            nationality: MetaOapg.properties.nationality
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["nationality"]) -> MetaOapg.properties.nationality: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["nationality", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["nationality"]) -> MetaOapg.properties.nationality: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nationality", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                nationality: typing.Union[MetaOapg.properties.nationality, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_25':
                return super().__new__(
                    cls,
                    *args,
                    nationality=nationality,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_26(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "trading-name",
                    "claim-type",
                }
                
                class properties:
                    trading_name = schemas.StrSchema
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "trading-name": "TRADINGNAME",
                            }
                        
                        @schemas.classproperty
                        def TRADINGNAME(cls):
                            return cls("trading-name")
                    __annotations__ = {
                        "trading-name": trading_name,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["trading-name"]) -> MetaOapg.properties.trading_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["trading-name", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["trading-name"]) -> MetaOapg.properties.trading_name: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["trading-name", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_26':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_27(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "claim-type",
                    "social-media",
                }
                
                class properties:
                    
                    
                    class social_media(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            min_length = 1
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "social-media": "SOCIALMEDIA",
                            }
                        
                        @schemas.classproperty
                        def SOCIALMEDIA(cls):
                            return cls("social-media")
                    __annotations__ = {
                        "social-media": social_media,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["social-media"]) -> MetaOapg.properties.social_media: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["social-media", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["social-media"]) -> MetaOapg.properties.social_media: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["social-media", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_27':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_28(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "trading-address",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class trading_address(
                        schemas.ComposedBase,
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "country-code",
                                "postal-code",
                                "city",
                                "street-name",
                            }
                            
                            class properties:
                                street_name = schemas.StrSchema
                                city = schemas.StrSchema
                                
                                
                                class postal_code(
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        max_length = 10
                                        min_length = 0
                                
                                
                                class country_code(
                                    schemas.AnyTypeSchema,
                                ):
                                
                                
                                    class MetaOapg:
                                        max_length = 2
                                        min_length = 2
                                
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'country_code':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                __annotations__ = {
                                    "street-name": street_name,
                                    "city": city,
                                    "postal-code": postal_code,
                                    "country-code": country_code,
                                }
                            
                            
                            class any_of_0(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "building-number",
                                        "building-name",
                                    }
                                    
                                    class properties:
                                        building_name = schemas.StrSchema
                                        building_number = schemas.StrSchema
                                        __annotations__ = {
                                            "building-name": building_name,
                                            "building-number": building_number,
                                        }
                                
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["building-name", "building-number", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building-name", "building-number", ], str]):
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
                            
                            
                            class any_of_1(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "building-name",
                                    }
                                    
                                    class properties:
                                        building_name = schemas.StrSchema
                                        __annotations__ = {
                                            "building-name": building_name,
                                        }
                                
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["building-name", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building-name", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'any_of_1':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            
                            class any_of_2(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "building-number",
                                    }
                                    
                                    class properties:
                                        building_number = schemas.StrSchema
                                        __annotations__ = {
                                            "building-number": building_number,
                                        }
                                
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["building-number", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building-number", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'any_of_2':
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
                                    cls.any_of_1,
                                    cls.any_of_2,
                                ]
                    
                        
                        city: MetaOapg.properties.city
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["street-name"]) -> MetaOapg.properties.street_name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["postal-code"]) -> MetaOapg.properties.postal_code: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["country-code"]) -> MetaOapg.properties.country_code: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["street-name", "city", "postal-code", "country-code", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["street-name"]) -> MetaOapg.properties.street_name: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["postal-code"]) -> MetaOapg.properties.postal_code: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["country-code"]) -> MetaOapg.properties.country_code: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["street-name", "city", "postal-code", "country-code", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            city: typing.Union[MetaOapg.properties.city, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'trading_address':
                            return super().__new__(
                                cls,
                                *args,
                                city=city,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "trading-address": "TRADINGADDRESS",
                            }
                        
                        @schemas.classproperty
                        def TRADINGADDRESS(cls):
                            return cls("trading-address")
                    __annotations__ = {
                        "trading-address": trading_address,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["trading-address"]) -> MetaOapg.properties.trading_address: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["trading-address", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["trading-address"]) -> MetaOapg.properties.trading_address: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["trading-address", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_28':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_29(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "website-url",
                    "claim-type",
                }
                
                class properties:
                    website_url = schemas.StrSchema
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "company-website": "COMPANYWEBSITE",
                            }
                        
                        @schemas.classproperty
                        def COMPANYWEBSITE(cls):
                            return cls("company-website")
                    __annotations__ = {
                        "website-url": website_url,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["website-url"]) -> MetaOapg.properties.website_url: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["website-url", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["website-url"]) -> MetaOapg.properties.website_url: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["website-url", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_29':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_30(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "legal-person-url",
                    "claim-type",
                }
                
                class properties:
                    legal_person_url = schemas.StrSchema
                    companies_house_url = schemas.StrSchema
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "director": "DIRECTOR",
                            }
                        
                        @schemas.classproperty
                        def DIRECTOR(cls):
                            return cls("director")
                    __annotations__ = {
                        "legal-person-url": legal_person_url,
                        "companies-house-url": companies_house_url,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["legal-person-url"]) -> MetaOapg.properties.legal_person_url: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["companies-house-url"]) -> MetaOapg.properties.companies_house_url: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["legal-person-url", "companies-house-url", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["legal-person-url"]) -> MetaOapg.properties.legal_person_url: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["companies-house-url"]) -> typing.Union[MetaOapg.properties.companies_house_url, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["legal-person-url", "companies-house-url", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_30':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_31(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "telephone-number",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class telephone_number(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'(\+[1-9])?\d{1,14}',
                            }]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'telephone_number':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "alternative-number": "ALTERNATIVENUMBER",
                            }
                        
                        @schemas.classproperty
                        def ALTERNATIVENUMBER(cls):
                            return cls("alternative-number")
                    __annotations__ = {
                        "telephone-number": telephone_number,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["telephone-number"]) -> MetaOapg.properties.telephone_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["telephone-number", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["telephone-number"]) -> MetaOapg.properties.telephone_number: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["telephone-number", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_31':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_32(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "tax-identification-number",
                    "claim-type",
                }
                
                class properties:
                    
                    
                    class tax_identification_number(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            min_length = 1
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "tax-identification-number": "TAXIDENTIFICATIONNUMBER",
                            }
                        
                        @schemas.classproperty
                        def TAXIDENTIFICATIONNUMBER(cls):
                            return cls("tax-identification-number")
                    __annotations__ = {
                        "tax-identification-number": tax_identification_number,
                        "claim-type": claim_type,
                    }
            
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["tax-identification-number"]) -> MetaOapg.properties.tax_identification_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["tax-identification-number", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["tax-identification-number"]) -> MetaOapg.properties.tax_identification_number: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tax-identification-number", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_32':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_33(
            schemas.ComposedBase,
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "country-code",
                    "postal-code",
                    "city",
                    "claim-type",
                    "street-name",
                }
                
                class properties:
                    street_name = schemas.StrSchema
                    city = schemas.StrSchema
                    
                    
                    class postal_code(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 10
                            min_length = 0
                    
                    
                    class country_code(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 2
                            min_length = 2
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'country_code':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class claim_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "individual-residence": "INDIVIDUALRESIDENCE",
                            }
                        
                        @schemas.classproperty
                        def INDIVIDUALRESIDENCE(cls):
                            return cls("individual-residence")
                    __annotations__ = {
                        "street-name": street_name,
                        "city": city,
                        "postal-code": postal_code,
                        "country-code": country_code,
                        "claim-type": claim_type,
                    }
                
                
                class any_of_0(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "building-number",
                            "building-name",
                        }
                        
                        class properties:
                            building_name = schemas.StrSchema
                            building_number = schemas.StrSchema
                            __annotations__ = {
                                "building-name": building_name,
                                "building-number": building_number,
                            }
                    
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["building-name", "building-number", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building-name", "building-number", ], str]):
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
                
                
                class any_of_1(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "building-name",
                        }
                        
                        class properties:
                            building_name = schemas.StrSchema
                            __annotations__ = {
                                "building-name": building_name,
                            }
                    
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["building-name", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["building-name"]) -> MetaOapg.properties.building_name: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building-name", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'any_of_1':
                        return super().__new__(
                            cls,
                            *args,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                
                class any_of_2(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "building-number",
                        }
                        
                        class properties:
                            building_number = schemas.StrSchema
                            __annotations__ = {
                                "building-number": building_number,
                            }
                    
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["building-number", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["building-number"]) -> MetaOapg.properties.building_number: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["building-number", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'any_of_2':
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
                        cls.any_of_1,
                        cls.any_of_2,
                    ]
        
            
            city: MetaOapg.properties.city
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["street-name"]) -> MetaOapg.properties.street_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["postal-code"]) -> MetaOapg.properties.postal_code: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["country-code"]) -> MetaOapg.properties.country_code: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["street-name", "city", "postal-code", "country-code", "claim-type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["street-name"]) -> MetaOapg.properties.street_name: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["postal-code"]) -> MetaOapg.properties.postal_code: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["country-code"]) -> MetaOapg.properties.country_code: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["claim-type"]) -> MetaOapg.properties.claim_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["street-name", "city", "postal-code", "country-code", "claim-type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                city: typing.Union[MetaOapg.properties.city, str, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_33':
                return super().__new__(
                    cls,
                    *args,
                    city=city,
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
                cls.any_of_2,
                cls.any_of_3,
                cls.any_of_4,
                cls.any_of_5,
                cls.any_of_6,
                cls.any_of_7,
                cls.any_of_8,
                cls.any_of_9,
                cls.any_of_10,
                cls.any_of_11,
                cls.any_of_12,
                cls.any_of_13,
                cls.any_of_14,
                cls.any_of_15,
                cls.any_of_16,
                cls.any_of_17,
                cls.any_of_18,
                cls.any_of_19,
                cls.any_of_20,
                cls.any_of_21,
                cls.any_of_22,
                cls.any_of_23,
                cls.any_of_24,
                cls.any_of_25,
                cls.any_of_26,
                cls.any_of_27,
                cls.any_of_28,
                cls.any_of_29,
                cls.any_of_30,
                cls.any_of_31,
                cls.any_of_32,
                cls.any_of_33,
            ]

    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClaimsCreateNewClaimResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
