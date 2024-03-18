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


class BankAccountsListResponseAccountsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "pooled-funds",
            "account-url",
            "close-account-url",
            "available-balance",
            "account-status",
            "bank-product-type",
            "owner-url",
            "account-balance",
            "account-payments-url",
            "account-transactions-url",
            "display-name",
            "account-restricted",
            "account-submissions-url",
            "created-at",
            "account-admissions-url",
            "controller-url",
        }
        
        class properties:
            account_submissions_url = schemas.StrSchema
            account_restricted = schemas.BoolSchema
            account_payments_url = schemas.StrSchema
            account_admissions_url = schemas.StrSchema
            
            
            class bank_product_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SAVINGSACCOUNT(cls):
                    return cls("savings-account")
                
                @schemas.classproperty
                def CLIENTMONEYACCOUNT(cls):
                    return cls("client-money-account")
                
                @schemas.classproperty
                def SAFEGUARDINGACCOUNT(cls):
                    return cls("safeguarding-account")
                
                @schemas.classproperty
                def OPERATIONALACCOUNT(cls):
                    return cls("operational-account")
            
            
            class display_name(
                schemas.StrSchema
            ):
                pass
            controller_url = schemas.StrSchema
            pooled_funds = schemas.BoolSchema
            
            
            class account_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CLOSING(cls):
                    return cls("closing")
                
                @schemas.classproperty
                def OPEN(cls):
                    return cls("open")
                
                @schemas.classproperty
                def CLOSED(cls):
                    return cls("closed")
                
                @schemas.classproperty
                def OPENING(cls):
                    return cls("opening")
            owner_url = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            close_account_url = schemas.StrSchema
        
            @staticmethod
            def available_balance() -> typing.Type['BankAccountsListResponseAccountsItemAvailableBalance']:
                return BankAccountsListResponseAccountsItemAvailableBalance
            account_transactions_url = schemas.StrSchema
            account_url = schemas.StrSchema
        
            @staticmethod
            def account_balance() -> typing.Type['BankAccountsListResponseAccountsItemAccountBalance']:
                return BankAccountsListResponseAccountsItemAccountBalance
            pooled_account_memberships_url = schemas.StrSchema
            
            
            class client_money_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DESIGNATEDCLIENTFUND(cls):
                    return cls("designated-client-fund")
                
                @schemas.classproperty
                def DESIGNATEDCLIENTMONEY(cls):
                    return cls("designated-client-money")
                
                @schemas.classproperty
                def GENERALCLIENTMONEY(cls):
                    return cls("general-client-money")
            pooled_account_membership_updates_url = schemas.StrSchema
        
            @staticmethod
            def bank_addresses() -> typing.Type['BankAccountsListResponseAccountsItemBankAddresses']:
                return BankAccountsListResponseAccountsItemBankAddresses
            beneficiary_url = schemas.StrSchema
            
            
            class savings_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EASYACCESS(cls):
                    return cls("easy-access")
            __annotations__ = {
                "account-submissions-url": account_submissions_url,
                "account-restricted": account_restricted,
                "account-payments-url": account_payments_url,
                "account-admissions-url": account_admissions_url,
                "bank-product-type": bank_product_type,
                "display-name": display_name,
                "controller-url": controller_url,
                "pooled-funds": pooled_funds,
                "account-status": account_status,
                "owner-url": owner_url,
                "created-at": created_at,
                "close-account-url": close_account_url,
                "available-balance": available_balance,
                "account-transactions-url": account_transactions_url,
                "account-url": account_url,
                "account-balance": account_balance,
                "pooled-account-memberships-url": pooled_account_memberships_url,
                "client-money-type": client_money_type,
                "pooled-account-membership-updates-url": pooled_account_membership_updates_url,
                "bank-addresses": bank_addresses,
                "beneficiary-url": beneficiary_url,
                "savings-type": savings_type,
            }
    
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account-submissions-url"]) -> MetaOapg.properties.account_submissions_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account-restricted"]) -> MetaOapg.properties.account_restricted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account-payments-url"]) -> MetaOapg.properties.account_payments_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account-admissions-url"]) -> MetaOapg.properties.account_admissions_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bank-product-type"]) -> MetaOapg.properties.bank_product_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display-name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["controller-url"]) -> MetaOapg.properties.controller_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pooled-funds"]) -> MetaOapg.properties.pooled_funds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account-status"]) -> MetaOapg.properties.account_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner-url"]) -> MetaOapg.properties.owner_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created-at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["close-account-url"]) -> MetaOapg.properties.close_account_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["available-balance"]) -> 'BankAccountsListResponseAccountsItemAvailableBalance': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account-transactions-url"]) -> MetaOapg.properties.account_transactions_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account-url"]) -> MetaOapg.properties.account_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account-balance"]) -> 'BankAccountsListResponseAccountsItemAccountBalance': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pooled-account-memberships-url"]) -> MetaOapg.properties.pooled_account_memberships_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client-money-type"]) -> MetaOapg.properties.client_money_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pooled-account-membership-updates-url"]) -> MetaOapg.properties.pooled_account_membership_updates_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bank-addresses"]) -> 'BankAccountsListResponseAccountsItemBankAddresses': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beneficiary-url"]) -> MetaOapg.properties.beneficiary_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["savings-type"]) -> MetaOapg.properties.savings_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["account-submissions-url", "account-restricted", "account-payments-url", "account-admissions-url", "bank-product-type", "display-name", "controller-url", "pooled-funds", "account-status", "owner-url", "created-at", "close-account-url", "available-balance", "account-transactions-url", "account-url", "account-balance", "pooled-account-memberships-url", "client-money-type", "pooled-account-membership-updates-url", "bank-addresses", "beneficiary-url", "savings-type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account-submissions-url"]) -> MetaOapg.properties.account_submissions_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account-restricted"]) -> MetaOapg.properties.account_restricted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account-payments-url"]) -> MetaOapg.properties.account_payments_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account-admissions-url"]) -> MetaOapg.properties.account_admissions_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bank-product-type"]) -> MetaOapg.properties.bank_product_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display-name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["controller-url"]) -> MetaOapg.properties.controller_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pooled-funds"]) -> MetaOapg.properties.pooled_funds: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account-status"]) -> MetaOapg.properties.account_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner-url"]) -> MetaOapg.properties.owner_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created-at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["close-account-url"]) -> MetaOapg.properties.close_account_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["available-balance"]) -> 'BankAccountsListResponseAccountsItemAvailableBalance': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account-transactions-url"]) -> MetaOapg.properties.account_transactions_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account-url"]) -> MetaOapg.properties.account_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account-balance"]) -> 'BankAccountsListResponseAccountsItemAccountBalance': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pooled-account-memberships-url"]) -> typing.Union[MetaOapg.properties.pooled_account_memberships_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client-money-type"]) -> typing.Union[MetaOapg.properties.client_money_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pooled-account-membership-updates-url"]) -> typing.Union[MetaOapg.properties.pooled_account_membership_updates_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bank-addresses"]) -> typing.Union['BankAccountsListResponseAccountsItemBankAddresses', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beneficiary-url"]) -> typing.Union[MetaOapg.properties.beneficiary_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["savings-type"]) -> typing.Union[MetaOapg.properties.savings_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["account-submissions-url", "account-restricted", "account-payments-url", "account-admissions-url", "bank-product-type", "display-name", "controller-url", "pooled-funds", "account-status", "owner-url", "created-at", "close-account-url", "available-balance", "account-transactions-url", "account-url", "account-balance", "pooled-account-memberships-url", "client-money-type", "pooled-account-membership-updates-url", "bank-addresses", "beneficiary-url", "savings-type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BankAccountsListResponseAccountsItem':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from griffin_python_sdk.model.bank_accounts_list_response_accounts_item_account_balance import BankAccountsListResponseAccountsItemAccountBalance
from griffin_python_sdk.model.bank_accounts_list_response_accounts_item_available_balance import BankAccountsListResponseAccountsItemAvailableBalance
from griffin_python_sdk.model.bank_accounts_list_response_accounts_item_bank_addresses import BankAccountsListResponseAccountsItemBankAddresses
