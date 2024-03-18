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


class MembershipsListOrganizationMembershipsResponseMembershipsItemOrganization(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "available-roles",
            "organization-corporations-url",
            "organization-workflows-url",
            "organization-mode",
            "organization-events-url",
            "organization-legal-persons-url",
            "organization-bank-accounts-url",
            "organization-webhooks-url",
            "organization-live-access-url",
            "display-name",
            "organization-memberships-url",
            "organization-api-keys-url",
            "organization-invitations-url",
            "can-decide-on-verifications?",
            "organization-individuals-url",
            "own-legal-person-url",
            "organization-url",
        }
        
        class properties:
            own_legal_person_url = schemas.StrSchema
            
            
            class organization_mode(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "test-mode": "TESTMODE",
                        "live-mode": "LIVEMODE",
                    }
                
                @schemas.classproperty
                def TESTMODE(cls):
                    return cls("test-mode")
                
                @schemas.classproperty
                def LIVEMODE(cls):
                    return cls("live-mode")
            organization_memberships_url = schemas.StrSchema
            organization_invitations_url = schemas.StrSchema
            
            
            class display_name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    min_length = 1
            organization_api_keys_url = schemas.StrSchema
            organization_live_access_url = schemas.StrSchema
            organization_webhooks_url = schemas.StrSchema
            organization_workflows_url = schemas.StrSchema
            organization_bank_accounts_url = schemas.StrSchema
        
            @staticmethod
            def available_roles() -> typing.Type['MembershipsListOrganizationMembershipsResponseMembershipsItemOrganizationAvailableRoles']:
                return MembershipsListOrganizationMembershipsResponseMembershipsItemOrganizationAvailableRoles
            can_decide_on_verifications = schemas.BoolSchema
            organization_url = schemas.StrSchema
            organization_individuals_url = schemas.StrSchema
            organization_corporations_url = schemas.StrSchema
            organization_legal_persons_url = schemas.StrSchema
            organization_events_url = schemas.StrSchema
            organization_onboarding_applications_url = schemas.StrSchema
            __annotations__ = {
                "own-legal-person-url": own_legal_person_url,
                "organization-mode": organization_mode,
                "organization-memberships-url": organization_memberships_url,
                "organization-invitations-url": organization_invitations_url,
                "display-name": display_name,
                "organization-api-keys-url": organization_api_keys_url,
                "organization-live-access-url": organization_live_access_url,
                "organization-webhooks-url": organization_webhooks_url,
                "organization-workflows-url": organization_workflows_url,
                "organization-bank-accounts-url": organization_bank_accounts_url,
                "available-roles": available_roles,
                "can-decide-on-verifications?": can_decide_on_verifications,
                "organization-url": organization_url,
                "organization-individuals-url": organization_individuals_url,
                "organization-corporations-url": organization_corporations_url,
                "organization-legal-persons-url": organization_legal_persons_url,
                "organization-events-url": organization_events_url,
                "organization-onboarding-applications-url": organization_onboarding_applications_url,
            }
    
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["own-legal-person-url"]) -> MetaOapg.properties.own_legal_person_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-mode"]) -> MetaOapg.properties.organization_mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-memberships-url"]) -> MetaOapg.properties.organization_memberships_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-invitations-url"]) -> MetaOapg.properties.organization_invitations_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display-name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-api-keys-url"]) -> MetaOapg.properties.organization_api_keys_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-live-access-url"]) -> MetaOapg.properties.organization_live_access_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-webhooks-url"]) -> MetaOapg.properties.organization_webhooks_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-workflows-url"]) -> MetaOapg.properties.organization_workflows_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-bank-accounts-url"]) -> MetaOapg.properties.organization_bank_accounts_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["available-roles"]) -> 'MembershipsListOrganizationMembershipsResponseMembershipsItemOrganizationAvailableRoles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can-decide-on-verifications?"]) -> MetaOapg.properties.can_decide_on_verifications: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-url"]) -> MetaOapg.properties.organization_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-individuals-url"]) -> MetaOapg.properties.organization_individuals_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-corporations-url"]) -> MetaOapg.properties.organization_corporations_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-legal-persons-url"]) -> MetaOapg.properties.organization_legal_persons_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-events-url"]) -> MetaOapg.properties.organization_events_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization-onboarding-applications-url"]) -> MetaOapg.properties.organization_onboarding_applications_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["own-legal-person-url", "organization-mode", "organization-memberships-url", "organization-invitations-url", "display-name", "organization-api-keys-url", "organization-live-access-url", "organization-webhooks-url", "organization-workflows-url", "organization-bank-accounts-url", "available-roles", "can-decide-on-verifications?", "organization-url", "organization-individuals-url", "organization-corporations-url", "organization-legal-persons-url", "organization-events-url", "organization-onboarding-applications-url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["own-legal-person-url"]) -> MetaOapg.properties.own_legal_person_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-mode"]) -> MetaOapg.properties.organization_mode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-memberships-url"]) -> MetaOapg.properties.organization_memberships_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-invitations-url"]) -> MetaOapg.properties.organization_invitations_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display-name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-api-keys-url"]) -> MetaOapg.properties.organization_api_keys_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-live-access-url"]) -> MetaOapg.properties.organization_live_access_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-webhooks-url"]) -> MetaOapg.properties.organization_webhooks_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-workflows-url"]) -> MetaOapg.properties.organization_workflows_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-bank-accounts-url"]) -> MetaOapg.properties.organization_bank_accounts_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["available-roles"]) -> 'MembershipsListOrganizationMembershipsResponseMembershipsItemOrganizationAvailableRoles': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can-decide-on-verifications?"]) -> MetaOapg.properties.can_decide_on_verifications: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-url"]) -> MetaOapg.properties.organization_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-individuals-url"]) -> MetaOapg.properties.organization_individuals_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-corporations-url"]) -> MetaOapg.properties.organization_corporations_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-legal-persons-url"]) -> MetaOapg.properties.organization_legal_persons_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-events-url"]) -> MetaOapg.properties.organization_events_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization-onboarding-applications-url"]) -> typing.Union[MetaOapg.properties.organization_onboarding_applications_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["own-legal-person-url", "organization-mode", "organization-memberships-url", "organization-invitations-url", "display-name", "organization-api-keys-url", "organization-live-access-url", "organization-webhooks-url", "organization-workflows-url", "organization-bank-accounts-url", "available-roles", "can-decide-on-verifications?", "organization-url", "organization-individuals-url", "organization-corporations-url", "organization-legal-persons-url", "organization-events-url", "organization-onboarding-applications-url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MembershipsListOrganizationMembershipsResponseMembershipsItemOrganization':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from griffin_python_sdk.model.memberships_list_organization_memberships_response_memberships_item_organization_available_roles import MembershipsListOrganizationMembershipsResponseMembershipsItemOrganizationAvailableRoles
