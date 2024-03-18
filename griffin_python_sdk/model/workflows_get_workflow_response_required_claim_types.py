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


class WorkflowsGetWorkflowResponseRequiredClaimTypes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A mapping of workflow-appropriate legal person types
                                 to claims that are required for each type.
    """


    class MetaOapg:
        
        
        class additional_properties(
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
                            "mobile-number": "MOBILENUMBER",
                            "individual-identity": "INDIVIDUALIDENTITY",
                            "sole-trader": "SOLETRADER",
                            "uk-company-register": "UKCOMPANYREGISTER",
                            "individual-income": "INDIVIDUALINCOME",
                            "business-website": "BUSINESSWEBSITE",
                            "initial-deposit": "INITIALDEPOSIT",
                            "international-payments-countries": "INTERNATIONALPAYMENTSCOUNTRIES",
                            "company-telephone-number": "COMPANYTELEPHONENUMBER",
                            "managed-properties": "MANAGEDPROPERTIES",
                            "person-with-significant-control": "PERSONWITHSIGNIFICANTCONTROL",
                            "tenant-cash-payments": "TENANTCASHPAYMENTS",
                            "verified-bank-account": "VERIFIEDBANKACCOUNT",
                            "company-email-address": "COMPANYEMAILADDRESS",
                            "tax-residency": "TAXRESIDENCY",
                            "uk-financial-services-register": "UKFINANCIALSERVICESREGISTER",
                            "non-tenant-balance": "NONTENANTBALANCE",
                            "business-description": "BUSINESSDESCRIPTION",
                            "hmrc-register": "HMRCREGISTER",
                            "business-email-address": "BUSINESSEMAILADDRESS",
                            "client-money-protection-scheme": "CLIENTMONEYPROTECTIONSCHEME",
                            "individual-sources-of-funds": "INDIVIDUALSOURCESOFFUNDS",
                            "hmo-verification": "HMOVERIFICATION",
                            "business-address": "BUSINESSADDRESS",
                            "employment": "EMPLOYMENT",
                            "annual-turnover": "ANNUALTURNOVER",
                            "purposes-of-account": "PURPOSESOFACCOUNT",
                            "sic-codes": "SICCODES",
                            "international-operations-countries": "INTERNATIONALOPERATIONSCOUNTRIES",
                            "sources-of-funds": "SOURCESOFFUNDS",
                            "business-owner": "BUSINESSOWNER",
                            "business-telephone-number": "BUSINESSTELEPHONENUMBER",
                            "individual-email-address": "INDIVIDUALEMAILADDRESS",
                            "business-start-date": "BUSINESSSTARTDATE",
                            "contact-details": "CONTACTDETAILS",
                            "reliance-verification": "RELIANCEVERIFICATION",
                            "ultimate-beneficial-owner": "ULTIMATEBENEFICIALOWNER",
                            "business-name": "BUSINESSNAME",
                            "individual-purposes-of-account": "INDIVIDUALPURPOSESOFACCOUNT",
                            "nationality": "NATIONALITY",
                            "trading-name": "TRADINGNAME",
                            "number-of-employees": "NUMBEROFEMPLOYEES",
                            "social-media": "SOCIALMEDIA",
                            "trading-address": "TRADINGADDRESS",
                            "company-website": "COMPANYWEBSITE",
                            "director": "DIRECTOR",
                            "alternative-number": "ALTERNATIVENUMBER",
                            "tax-identification-number": "TAXIDENTIFICATIONNUMBER",
                            "individual-residence": "INDIVIDUALRESIDENCE",
                        }
                    
                    @schemas.classproperty
                    def MOBILENUMBER(cls):
                        return cls("mobile-number")
                    
                    @schemas.classproperty
                    def INDIVIDUALIDENTITY(cls):
                        return cls("individual-identity")
                    
                    @schemas.classproperty
                    def SOLETRADER(cls):
                        return cls("sole-trader")
                    
                    @schemas.classproperty
                    def UKCOMPANYREGISTER(cls):
                        return cls("uk-company-register")
                    
                    @schemas.classproperty
                    def INDIVIDUALINCOME(cls):
                        return cls("individual-income")
                    
                    @schemas.classproperty
                    def BUSINESSWEBSITE(cls):
                        return cls("business-website")
                    
                    @schemas.classproperty
                    def INITIALDEPOSIT(cls):
                        return cls("initial-deposit")
                    
                    @schemas.classproperty
                    def INTERNATIONALPAYMENTSCOUNTRIES(cls):
                        return cls("international-payments-countries")
                    
                    @schemas.classproperty
                    def COMPANYTELEPHONENUMBER(cls):
                        return cls("company-telephone-number")
                    
                    @schemas.classproperty
                    def MANAGEDPROPERTIES(cls):
                        return cls("managed-properties")
                    
                    @schemas.classproperty
                    def PERSONWITHSIGNIFICANTCONTROL(cls):
                        return cls("person-with-significant-control")
                    
                    @schemas.classproperty
                    def TENANTCASHPAYMENTS(cls):
                        return cls("tenant-cash-payments")
                    
                    @schemas.classproperty
                    def VERIFIEDBANKACCOUNT(cls):
                        return cls("verified-bank-account")
                    
                    @schemas.classproperty
                    def COMPANYEMAILADDRESS(cls):
                        return cls("company-email-address")
                    
                    @schemas.classproperty
                    def TAXRESIDENCY(cls):
                        return cls("tax-residency")
                    
                    @schemas.classproperty
                    def UKFINANCIALSERVICESREGISTER(cls):
                        return cls("uk-financial-services-register")
                    
                    @schemas.classproperty
                    def NONTENANTBALANCE(cls):
                        return cls("non-tenant-balance")
                    
                    @schemas.classproperty
                    def BUSINESSDESCRIPTION(cls):
                        return cls("business-description")
                    
                    @schemas.classproperty
                    def HMRCREGISTER(cls):
                        return cls("hmrc-register")
                    
                    @schemas.classproperty
                    def BUSINESSEMAILADDRESS(cls):
                        return cls("business-email-address")
                    
                    @schemas.classproperty
                    def CLIENTMONEYPROTECTIONSCHEME(cls):
                        return cls("client-money-protection-scheme")
                    
                    @schemas.classproperty
                    def INDIVIDUALSOURCESOFFUNDS(cls):
                        return cls("individual-sources-of-funds")
                    
                    @schemas.classproperty
                    def HMOVERIFICATION(cls):
                        return cls("hmo-verification")
                    
                    @schemas.classproperty
                    def BUSINESSADDRESS(cls):
                        return cls("business-address")
                    
                    @schemas.classproperty
                    def EMPLOYMENT(cls):
                        return cls("employment")
                    
                    @schemas.classproperty
                    def ANNUALTURNOVER(cls):
                        return cls("annual-turnover")
                    
                    @schemas.classproperty
                    def PURPOSESOFACCOUNT(cls):
                        return cls("purposes-of-account")
                    
                    @schemas.classproperty
                    def SICCODES(cls):
                        return cls("sic-codes")
                    
                    @schemas.classproperty
                    def INTERNATIONALOPERATIONSCOUNTRIES(cls):
                        return cls("international-operations-countries")
                    
                    @schemas.classproperty
                    def SOURCESOFFUNDS(cls):
                        return cls("sources-of-funds")
                    
                    @schemas.classproperty
                    def BUSINESSOWNER(cls):
                        return cls("business-owner")
                    
                    @schemas.classproperty
                    def BUSINESSTELEPHONENUMBER(cls):
                        return cls("business-telephone-number")
                    
                    @schemas.classproperty
                    def INDIVIDUALEMAILADDRESS(cls):
                        return cls("individual-email-address")
                    
                    @schemas.classproperty
                    def BUSINESSSTARTDATE(cls):
                        return cls("business-start-date")
                    
                    @schemas.classproperty
                    def CONTACTDETAILS(cls):
                        return cls("contact-details")
                    
                    @schemas.classproperty
                    def RELIANCEVERIFICATION(cls):
                        return cls("reliance-verification")
                    
                    @schemas.classproperty
                    def ULTIMATEBENEFICIALOWNER(cls):
                        return cls("ultimate-beneficial-owner")
                    
                    @schemas.classproperty
                    def BUSINESSNAME(cls):
                        return cls("business-name")
                    
                    @schemas.classproperty
                    def INDIVIDUALPURPOSESOFACCOUNT(cls):
                        return cls("individual-purposes-of-account")
                    
                    @schemas.classproperty
                    def NATIONALITY(cls):
                        return cls("nationality")
                    
                    @schemas.classproperty
                    def TRADINGNAME(cls):
                        return cls("trading-name")
                    
                    @schemas.classproperty
                    def NUMBEROFEMPLOYEES(cls):
                        return cls("number-of-employees")
                    
                    @schemas.classproperty
                    def SOCIALMEDIA(cls):
                        return cls("social-media")
                    
                    @schemas.classproperty
                    def TRADINGADDRESS(cls):
                        return cls("trading-address")
                    
                    @schemas.classproperty
                    def COMPANYWEBSITE(cls):
                        return cls("company-website")
                    
                    @schemas.classproperty
                    def DIRECTOR(cls):
                        return cls("director")
                    
                    @schemas.classproperty
                    def ALTERNATIVENUMBER(cls):
                        return cls("alternative-number")
                    
                    @schemas.classproperty
                    def TAXIDENTIFICATIONNUMBER(cls):
                        return cls("tax-identification-number")
                    
                    @schemas.classproperty
                    def INDIVIDUALRESIDENCE(cls):
                        return cls("individual-residence")
        
            def __new__(
                cls,
                arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                _configuration: typing.Optional[schemas.Configuration] = None,
            ) -> 'additional_properties':
                return super().__new__(
                    cls,
                    arg,
                    _configuration=_configuration,
                )
        
            def __getitem__(self, i: int) -> MetaOapg.items:
                return super().__getitem__(i)
    
    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
    ) -> 'WorkflowsGetWorkflowResponseRequiredClaimTypes':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
