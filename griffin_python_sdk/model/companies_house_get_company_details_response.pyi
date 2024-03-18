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


class CompaniesHouseGetCompanyDetailsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "persons-with-significant-control",
            "company-status",
            "corporation-type",
            "entity-name",
            "date-of-incorporation",
            "directors",
            "entity-registration-number",
        }
        
        class properties:
            entity_name = schemas.StrSchema
        
            @staticmethod
            def directors() -> typing.Type['CompaniesHouseGetCompanyDetailsResponseDirectors']:
                return CompaniesHouseGetCompanyDetailsResponseDirectors
            
            
            class corporation_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
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
            
            
            class company_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DISSOLVED(cls):
                    return cls("dissolved")
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("active")
                
                @schemas.classproperty
                def RECEIVERSHIP(cls):
                    return cls("receivership")
                
                @schemas.classproperty
                def REGISTERED(cls):
                    return cls("registered")
                
                @schemas.classproperty
                def REMOVED(cls):
                    return cls("removed")
                
                @schemas.classproperty
                def ADMINISTRATION(cls):
                    return cls("administration")
                
                @schemas.classproperty
                def OPEN(cls):
                    return cls("open")
                
                @schemas.classproperty
                def CLOSED(cls):
                    return cls("closed")
                
                @schemas.classproperty
                def VOLUNTARYARRANGEMENT(cls):
                    return cls("voluntary-arrangement")
                
                @schemas.classproperty
                def LIQUIDATION(cls):
                    return cls("liquidation")
                
                @schemas.classproperty
                def CONVERTEDCLOSED(cls):
                    return cls("converted-closed")
                
                @schemas.classproperty
                def INSOLVENCYPROCEEDINGS(cls):
                    return cls("insolvency-proceedings")
        
            @staticmethod
            def persons_with_significant_control() -> typing.Type['CompaniesHouseGetCompanyDetailsResponsePersonsWithSignificantControl']:
                return CompaniesHouseGetCompanyDetailsResponsePersonsWithSignificantControl
            date_of_incorporation = schemas.DateSchema
            
            
            class entity_registration_number(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def company_address() -> typing.Type['CompaniesHouseGetCompanyDetailsResponseCompanyAddress']:
                return CompaniesHouseGetCompanyDetailsResponseCompanyAddress
            date_of_latest_accounts = schemas.DateSchema
            date_of_latest_confirmation_statement = schemas.DateSchema
            accounts_overdue = schemas.BoolSchema
        
            @staticmethod
            def sic_codes() -> typing.Type['CompaniesHouseGetCompanyDetailsResponseSicCodes']:
                return CompaniesHouseGetCompanyDetailsResponseSicCodes
            confirmation_statement_overdue = schemas.BoolSchema
            __annotations__ = {
                "entity-name": entity_name,
                "directors": directors,
                "corporation-type": corporation_type,
                "company-status": company_status,
                "persons-with-significant-control": persons_with_significant_control,
                "date-of-incorporation": date_of_incorporation,
                "entity-registration-number": entity_registration_number,
                "company-address": company_address,
                "date-of-latest-accounts": date_of_latest_accounts,
                "date-of-latest-confirmation-statement": date_of_latest_confirmation_statement,
                "accounts-overdue": accounts_overdue,
                "sic-codes": sic_codes,
                "confirmation-statement-overdue": confirmation_statement_overdue,
            }
    
    directors: 'CompaniesHouseGetCompanyDetailsResponseDirectors'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity-name"]) -> MetaOapg.properties.entity_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directors"]) -> 'CompaniesHouseGetCompanyDetailsResponseDirectors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["corporation-type"]) -> MetaOapg.properties.corporation_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company-status"]) -> MetaOapg.properties.company_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["persons-with-significant-control"]) -> 'CompaniesHouseGetCompanyDetailsResponsePersonsWithSignificantControl': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date-of-incorporation"]) -> MetaOapg.properties.date_of_incorporation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity-registration-number"]) -> MetaOapg.properties.entity_registration_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company-address"]) -> 'CompaniesHouseGetCompanyDetailsResponseCompanyAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date-of-latest-accounts"]) -> MetaOapg.properties.date_of_latest_accounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date-of-latest-confirmation-statement"]) -> MetaOapg.properties.date_of_latest_confirmation_statement: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accounts-overdue"]) -> MetaOapg.properties.accounts_overdue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sic-codes"]) -> 'CompaniesHouseGetCompanyDetailsResponseSicCodes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["confirmation-statement-overdue"]) -> MetaOapg.properties.confirmation_statement_overdue: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["entity-name", "directors", "corporation-type", "company-status", "persons-with-significant-control", "date-of-incorporation", "entity-registration-number", "company-address", "date-of-latest-accounts", "date-of-latest-confirmation-statement", "accounts-overdue", "sic-codes", "confirmation-statement-overdue", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity-name"]) -> MetaOapg.properties.entity_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directors"]) -> 'CompaniesHouseGetCompanyDetailsResponseDirectors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["corporation-type"]) -> MetaOapg.properties.corporation_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company-status"]) -> MetaOapg.properties.company_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["persons-with-significant-control"]) -> 'CompaniesHouseGetCompanyDetailsResponsePersonsWithSignificantControl': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date-of-incorporation"]) -> MetaOapg.properties.date_of_incorporation: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity-registration-number"]) -> MetaOapg.properties.entity_registration_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company-address"]) -> typing.Union['CompaniesHouseGetCompanyDetailsResponseCompanyAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date-of-latest-accounts"]) -> typing.Union[MetaOapg.properties.date_of_latest_accounts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date-of-latest-confirmation-statement"]) -> typing.Union[MetaOapg.properties.date_of_latest_confirmation_statement, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accounts-overdue"]) -> typing.Union[MetaOapg.properties.accounts_overdue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sic-codes"]) -> typing.Union['CompaniesHouseGetCompanyDetailsResponseSicCodes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["confirmation-statement-overdue"]) -> typing.Union[MetaOapg.properties.confirmation_statement_overdue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["entity-name", "directors", "corporation-type", "company-status", "persons-with-significant-control", "date-of-incorporation", "entity-registration-number", "company-address", "date-of-latest-accounts", "date-of-latest-confirmation-statement", "accounts-overdue", "sic-codes", "confirmation-statement-overdue", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        directors: 'CompaniesHouseGetCompanyDetailsResponseDirectors',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompaniesHouseGetCompanyDetailsResponse':
        return super().__new__(
            cls,
            *args,
            directors=directors,
            _configuration=_configuration,
            **kwargs,
        )

from griffin_python_sdk.model.companies_house_get_company_details_response_company_address import CompaniesHouseGetCompanyDetailsResponseCompanyAddress
from griffin_python_sdk.model.companies_house_get_company_details_response_directors import CompaniesHouseGetCompanyDetailsResponseDirectors
from griffin_python_sdk.model.companies_house_get_company_details_response_persons_with_significant_control import CompaniesHouseGetCompanyDetailsResponsePersonsWithSignificantControl
from griffin_python_sdk.model.companies_house_get_company_details_response_sic_codes import CompaniesHouseGetCompanyDetailsResponseSicCodes
