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


class CompaniesHouseGetCompanyDetailsResponsePersonsWithSignificantControlItemNaturesOfControl(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "voting-rights-25-to-50-percent-limited-liability-partnership": "VOTINGRIGHTS25TO50PERCENTLIMITEDLIABILITYPARTNERSHIP",
                    "right-to-appoint-and-remove-members-limited-liability-partnership": "RIGHTTOAPPOINTANDREMOVEMEMBERSLIMITEDLIABILITYPARTNERSHIP",
                    "part-right-to-share-surplus-assets-75-to-100-percent-as-trust": "PARTRIGHTTOSHARESURPLUSASSETS75TO100PERCENTASTRUST",
                    "ownership-of-shares-more-than-25-percent-registered-overseas-entity": "OWNERSHIPOFSHARESMORETHAN25PERCENTREGISTEREDOVERSEASENTITY",
                    "part-right-to-share-surplus-assets-50-to-75-percent-as-trust": "PARTRIGHTTOSHARESURPLUSASSETS50TO75PERCENTASTRUST",
                    "significant-influence-or-control-as-firm-limited-liability-partnership": "SIGNIFICANTINFLUENCEORCONTROLASFIRMLIMITEDLIABILITYPARTNERSHIP",
                    "part-right-to-share-surplus-assets-25-to-50-percent-as-firm": "PARTRIGHTTOSHARESURPLUSASSETS25TO50PERCENTASFIRM",
                    "ownership-of-shares-25-to-50-percent-as-trust": "OWNERSHIPOFSHARES25TO50PERCENTASTRUST",
                    "ownership-of-shares-more-than-25-percent-as-firm-registered-overseas-entity": "OWNERSHIPOFSHARESMORETHAN25PERCENTASFIRMREGISTEREDOVERSEASENTITY",
                    "voting-rights-25-to-50-percent": "VOTINGRIGHTS25TO50PERCENT",
                    "voting-rights-25-to-50-percent-as-firm": "VOTINGRIGHTS25TO50PERCENTASFIRM",
                    "ownership-of-shares-more-than-25-percent-as-trust-registered-overseas-entity": "OWNERSHIPOFSHARESMORETHAN25PERCENTASTRUSTREGISTEREDOVERSEASENTITY",
                    "significant-influence-or-control": "SIGNIFICANTINFLUENCEORCONTROL",
                    "significant-influence-or-control-registered-overseas-entity": "SIGNIFICANTINFLUENCEORCONTROLREGISTEREDOVERSEASENTITY",
                    "part-right-to-share-surplus-assets-50-to-75-percent-as-firm": "PARTRIGHTTOSHARESURPLUSASSETS50TO75PERCENTASFIRM",
                    "voting-rights-50-to-75-percent": "VOTINGRIGHTS50TO75PERCENT",
                    "part-right-to-share-surplus-assets-25-to-50-percent": "PARTRIGHTTOSHARESURPLUSASSETS25TO50PERCENT",
                    "voting-rights-50-to-75-percent-as-trust": "VOTINGRIGHTS50TO75PERCENTASTRUST",
                    "right-to-share-surplus-assets-75-to-100-percent-as-firm-limited-liability-partnership": "RIGHTTOSHARESURPLUSASSETS75TO100PERCENTASFIRMLIMITEDLIABILITYPARTNERSHIP",
                    "right-to-appoint-and-remove-person-as-trust": "RIGHTTOAPPOINTANDREMOVEPERSONASTRUST",
                    "ownership-of-shares-50-to-75-percent-as-firm": "OWNERSHIPOFSHARES50TO75PERCENTASFIRM",
                    "voting-rights-50-to-75-percent-as-firm-limited-liability-partnership": "VOTINGRIGHTS50TO75PERCENTASFIRMLIMITEDLIABILITYPARTNERSHIP",
                    "voting-rights-25-to-50-percent-as-trust": "VOTINGRIGHTS25TO50PERCENTASTRUST",
                    "voting-rights-50-to-75-percent-as-trust-limited-liability-partnership": "VOTINGRIGHTS50TO75PERCENTASTRUSTLIMITEDLIABILITYPARTNERSHIP",
                    "voting-rights-75-to-100-percent": "VOTINGRIGHTS75TO100PERCENT",
                    "part-right-to-share-surplus-assets-75-to-100-percent-as-firm": "PARTRIGHTTOSHARESURPLUSASSETS75TO100PERCENTASFIRM",
                    "significant-influence-or-control-limited-liability-partnership": "SIGNIFICANTINFLUENCEORCONTROLLIMITEDLIABILITYPARTNERSHIP",
                    "right-to-share-surplus-assets-75-to-100-percent-limited-liability-partnership": "RIGHTTOSHARESURPLUSASSETS75TO100PERCENTLIMITEDLIABILITYPARTNERSHIP",
                    "right-to-appoint-and-remove-directors-as-firm": "RIGHTTOAPPOINTANDREMOVEDIRECTORSASFIRM",
                    "voting-rights-75-to-100-percent-as-trust": "VOTINGRIGHTS75TO100PERCENTASTRUST",
                    "voting-rights-25-to-50-percent-as-firm-limited-liability-partnership": "VOTINGRIGHTS25TO50PERCENTASFIRMLIMITEDLIABILITYPARTNERSHIP",
                    "right-to-appoint-and-remove-directors-as-firm-registered-overseas-entity": "RIGHTTOAPPOINTANDREMOVEDIRECTORSASFIRMREGISTEREDOVERSEASENTITY",
                    "right-to-share-surplus-assets-25-to-50-percent-as-firm-limited-liability-partnership": "RIGHTTOSHARESURPLUSASSETS25TO50PERCENTASFIRMLIMITEDLIABILITYPARTNERSHIP",
                    "ownership-of-shares-25-to-50-percent": "OWNERSHIPOFSHARES25TO50PERCENT",
                    "ownership-of-shares-75-to-100-percent-as-firm": "OWNERSHIPOFSHARES75TO100PERCENTASFIRM",
                    "significant-influence-or-control-as-firm": "SIGNIFICANTINFLUENCEORCONTROLASFIRM",
                    "right-to-appoint-and-remove-directors-as-trust": "RIGHTTOAPPOINTANDREMOVEDIRECTORSASTRUST",
                    "right-to-appoint-and-remove-person": "RIGHTTOAPPOINTANDREMOVEPERSON",
                    "significant-influence-or-control-as-trust-registered-overseas-entity": "SIGNIFICANTINFLUENCEORCONTROLASTRUSTREGISTEREDOVERSEASENTITY",
                    "voting-rights-more-than-25-percent-as-trust-registered-overseas-entity": "VOTINGRIGHTSMORETHAN25PERCENTASTRUSTREGISTEREDOVERSEASENTITY",
                    "right-to-appoint-and-remove-directors-as-trust-registered-overseas-entity": "RIGHTTOAPPOINTANDREMOVEDIRECTORSASTRUSTREGISTEREDOVERSEASENTITY",
                    "right-to-appoint-and-remove-members-as-firm-limited-liability-partnership": "RIGHTTOAPPOINTANDREMOVEMEMBERSASFIRMLIMITEDLIABILITYPARTNERSHIP",
                    "part-right-to-share-surplus-assets-75-to-100-percent": "PARTRIGHTTOSHARESURPLUSASSETS75TO100PERCENT",
                    "ownership-of-shares-25-to-50-percent-as-firm": "OWNERSHIPOFSHARES25TO50PERCENTASFIRM",
                    "right-to-share-surplus-assets-25-to-50-percent-as-trust-limited-liability-partnership": "RIGHTTOSHARESURPLUSASSETS25TO50PERCENTASTRUSTLIMITEDLIABILITYPARTNERSHIP",
                    "right-to-share-surplus-assets-50-to-75-percent-limited-liability-partnership": "RIGHTTOSHARESURPLUSASSETS50TO75PERCENTLIMITEDLIABILITYPARTNERSHIP",
                    "voting-rights-50-to-75-percent-as-firm": "VOTINGRIGHTS50TO75PERCENTASFIRM",
                    "part-right-to-share-surplus-assets-50-to-75-percent": "PARTRIGHTTOSHARESURPLUSASSETS50TO75PERCENT",
                    "right-to-appoint-and-remove-directors-registered-overseas-entity": "RIGHTTOAPPOINTANDREMOVEDIRECTORSREGISTEREDOVERSEASENTITY",
                    "significant-influence-or-control-as-trust": "SIGNIFICANTINFLUENCEORCONTROLASTRUST",
                    "right-to-share-surplus-assets-75-to-100-percent-as-trust-limited-liability-partnership": "RIGHTTOSHARESURPLUSASSETS75TO100PERCENTASTRUSTLIMITEDLIABILITYPARTNERSHIP",
                    "ownership-of-shares-50-to-75-percent-as-trust": "OWNERSHIPOFSHARES50TO75PERCENTASTRUST",
                    "right-to-share-surplus-assets-50-to-75-percent-as-firm-limited-liability-partnership": "RIGHTTOSHARESURPLUSASSETS50TO75PERCENTASFIRMLIMITEDLIABILITYPARTNERSHIP",
                    "voting-rights-more-than-25-percent-as-firm-registered-overseas-entity": "VOTINGRIGHTSMORETHAN25PERCENTASFIRMREGISTEREDOVERSEASENTITY",
                    "significant-influence-or-control-as-firm-registered-overseas-entity": "SIGNIFICANTINFLUENCEORCONTROLASFIRMREGISTEREDOVERSEASENTITY",
                    "ownership-of-shares-75-to-100-percent-as-trust": "OWNERSHIPOFSHARES75TO100PERCENTASTRUST",
                    "ownership-of-shares-50-to-75-percent": "OWNERSHIPOFSHARES50TO75PERCENT",
                    "right-to-share-surplus-assets-50-to-75-percent-as-trust-limited-liability-partnership": "RIGHTTOSHARESURPLUSASSETS50TO75PERCENTASTRUSTLIMITEDLIABILITYPARTNERSHIP",
                    "voting-rights-75-to-100-percent-limited-liability-partnership": "VOTINGRIGHTS75TO100PERCENTLIMITEDLIABILITYPARTNERSHIP",
                    "voting-rights-more-than-25-percent-registered-overseas-entity": "VOTINGRIGHTSMORETHAN25PERCENTREGISTEREDOVERSEASENTITY",
                    "right-to-appoint-and-remove-members-as-trust-limited-liability-partnership": "RIGHTTOAPPOINTANDREMOVEMEMBERSASTRUSTLIMITEDLIABILITYPARTNERSHIP",
                    "ownership-of-shares-75-to-100-percent": "OWNERSHIPOFSHARES75TO100PERCENT",
                    "part-right-to-share-surplus-assets-25-to-50-percent-as-trust": "PARTRIGHTTOSHARESURPLUSASSETS25TO50PERCENTASTRUST",
                    "voting-rights-75-to-100-percent-as-trust-limited-liability-partnership": "VOTINGRIGHTS75TO100PERCENTASTRUSTLIMITEDLIABILITYPARTNERSHIP",
                    "voting-rights-50-to-75-percent-limited-liability-partnership": "VOTINGRIGHTS50TO75PERCENTLIMITEDLIABILITYPARTNERSHIP",
                    "significant-influence-or-control-as-trust-limited-liability-partnership": "SIGNIFICANTINFLUENCEORCONTROLASTRUSTLIMITEDLIABILITYPARTNERSHIP",
                    "voting-rights-75-to-100-percent-as-firm-limited-liability-partnership": "VOTINGRIGHTS75TO100PERCENTASFIRMLIMITEDLIABILITYPARTNERSHIP",
                    "right-to-appoint-and-remove-person-as-firm": "RIGHTTOAPPOINTANDREMOVEPERSONASFIRM",
                    "right-to-appoint-and-remove-directors": "RIGHTTOAPPOINTANDREMOVEDIRECTORS",
                    "voting-rights-25-to-50-percent-as-trust-limited-liability-partnership": "VOTINGRIGHTS25TO50PERCENTASTRUSTLIMITEDLIABILITYPARTNERSHIP",
                    "voting-rights-75-to-100-percent-as-firm": "VOTINGRIGHTS75TO100PERCENTASFIRM",
                    "right-to-share-surplus-assets-25-to-50-percent-limited-liability-partnership": "RIGHTTOSHARESURPLUSASSETS25TO50PERCENTLIMITEDLIABILITYPARTNERSHIP",
                }
            
            @schemas.classproperty
            def VOTINGRIGHTS25TO50PERCENTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("voting-rights-25-to-50-percent-limited-liability-partnership")
            
            @schemas.classproperty
            def RIGHTTOAPPOINTANDREMOVEMEMBERSLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("right-to-appoint-and-remove-members-limited-liability-partnership")
            
            @schemas.classproperty
            def PARTRIGHTTOSHARESURPLUSASSETS75TO100PERCENTASTRUST(cls):
                return cls("part-right-to-share-surplus-assets-75-to-100-percent-as-trust")
            
            @schemas.classproperty
            def OWNERSHIPOFSHARESMORETHAN25PERCENTREGISTEREDOVERSEASENTITY(cls):
                return cls("ownership-of-shares-more-than-25-percent-registered-overseas-entity")
            
            @schemas.classproperty
            def PARTRIGHTTOSHARESURPLUSASSETS50TO75PERCENTASTRUST(cls):
                return cls("part-right-to-share-surplus-assets-50-to-75-percent-as-trust")
            
            @schemas.classproperty
            def SIGNIFICANTINFLUENCEORCONTROLASFIRMLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("significant-influence-or-control-as-firm-limited-liability-partnership")
            
            @schemas.classproperty
            def PARTRIGHTTOSHARESURPLUSASSETS25TO50PERCENTASFIRM(cls):
                return cls("part-right-to-share-surplus-assets-25-to-50-percent-as-firm")
            
            @schemas.classproperty
            def OWNERSHIPOFSHARES25TO50PERCENTASTRUST(cls):
                return cls("ownership-of-shares-25-to-50-percent-as-trust")
            
            @schemas.classproperty
            def OWNERSHIPOFSHARESMORETHAN25PERCENTASFIRMREGISTEREDOVERSEASENTITY(cls):
                return cls("ownership-of-shares-more-than-25-percent-as-firm-registered-overseas-entity")
            
            @schemas.classproperty
            def VOTINGRIGHTS25TO50PERCENT(cls):
                return cls("voting-rights-25-to-50-percent")
            
            @schemas.classproperty
            def VOTINGRIGHTS25TO50PERCENTASFIRM(cls):
                return cls("voting-rights-25-to-50-percent-as-firm")
            
            @schemas.classproperty
            def OWNERSHIPOFSHARESMORETHAN25PERCENTASTRUSTREGISTEREDOVERSEASENTITY(cls):
                return cls("ownership-of-shares-more-than-25-percent-as-trust-registered-overseas-entity")
            
            @schemas.classproperty
            def SIGNIFICANTINFLUENCEORCONTROL(cls):
                return cls("significant-influence-or-control")
            
            @schemas.classproperty
            def SIGNIFICANTINFLUENCEORCONTROLREGISTEREDOVERSEASENTITY(cls):
                return cls("significant-influence-or-control-registered-overseas-entity")
            
            @schemas.classproperty
            def PARTRIGHTTOSHARESURPLUSASSETS50TO75PERCENTASFIRM(cls):
                return cls("part-right-to-share-surplus-assets-50-to-75-percent-as-firm")
            
            @schemas.classproperty
            def VOTINGRIGHTS50TO75PERCENT(cls):
                return cls("voting-rights-50-to-75-percent")
            
            @schemas.classproperty
            def PARTRIGHTTOSHARESURPLUSASSETS25TO50PERCENT(cls):
                return cls("part-right-to-share-surplus-assets-25-to-50-percent")
            
            @schemas.classproperty
            def VOTINGRIGHTS50TO75PERCENTASTRUST(cls):
                return cls("voting-rights-50-to-75-percent-as-trust")
            
            @schemas.classproperty
            def RIGHTTOSHARESURPLUSASSETS75TO100PERCENTASFIRMLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("right-to-share-surplus-assets-75-to-100-percent-as-firm-limited-liability-partnership")
            
            @schemas.classproperty
            def RIGHTTOAPPOINTANDREMOVEPERSONASTRUST(cls):
                return cls("right-to-appoint-and-remove-person-as-trust")
            
            @schemas.classproperty
            def OWNERSHIPOFSHARES50TO75PERCENTASFIRM(cls):
                return cls("ownership-of-shares-50-to-75-percent-as-firm")
            
            @schemas.classproperty
            def VOTINGRIGHTS50TO75PERCENTASFIRMLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("voting-rights-50-to-75-percent-as-firm-limited-liability-partnership")
            
            @schemas.classproperty
            def VOTINGRIGHTS25TO50PERCENTASTRUST(cls):
                return cls("voting-rights-25-to-50-percent-as-trust")
            
            @schemas.classproperty
            def VOTINGRIGHTS50TO75PERCENTASTRUSTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("voting-rights-50-to-75-percent-as-trust-limited-liability-partnership")
            
            @schemas.classproperty
            def VOTINGRIGHTS75TO100PERCENT(cls):
                return cls("voting-rights-75-to-100-percent")
            
            @schemas.classproperty
            def PARTRIGHTTOSHARESURPLUSASSETS75TO100PERCENTASFIRM(cls):
                return cls("part-right-to-share-surplus-assets-75-to-100-percent-as-firm")
            
            @schemas.classproperty
            def SIGNIFICANTINFLUENCEORCONTROLLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("significant-influence-or-control-limited-liability-partnership")
            
            @schemas.classproperty
            def RIGHTTOSHARESURPLUSASSETS75TO100PERCENTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("right-to-share-surplus-assets-75-to-100-percent-limited-liability-partnership")
            
            @schemas.classproperty
            def RIGHTTOAPPOINTANDREMOVEDIRECTORSASFIRM(cls):
                return cls("right-to-appoint-and-remove-directors-as-firm")
            
            @schemas.classproperty
            def VOTINGRIGHTS75TO100PERCENTASTRUST(cls):
                return cls("voting-rights-75-to-100-percent-as-trust")
            
            @schemas.classproperty
            def VOTINGRIGHTS25TO50PERCENTASFIRMLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("voting-rights-25-to-50-percent-as-firm-limited-liability-partnership")
            
            @schemas.classproperty
            def RIGHTTOAPPOINTANDREMOVEDIRECTORSASFIRMREGISTEREDOVERSEASENTITY(cls):
                return cls("right-to-appoint-and-remove-directors-as-firm-registered-overseas-entity")
            
            @schemas.classproperty
            def RIGHTTOSHARESURPLUSASSETS25TO50PERCENTASFIRMLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("right-to-share-surplus-assets-25-to-50-percent-as-firm-limited-liability-partnership")
            
            @schemas.classproperty
            def OWNERSHIPOFSHARES25TO50PERCENT(cls):
                return cls("ownership-of-shares-25-to-50-percent")
            
            @schemas.classproperty
            def OWNERSHIPOFSHARES75TO100PERCENTASFIRM(cls):
                return cls("ownership-of-shares-75-to-100-percent-as-firm")
            
            @schemas.classproperty
            def SIGNIFICANTINFLUENCEORCONTROLASFIRM(cls):
                return cls("significant-influence-or-control-as-firm")
            
            @schemas.classproperty
            def RIGHTTOAPPOINTANDREMOVEDIRECTORSASTRUST(cls):
                return cls("right-to-appoint-and-remove-directors-as-trust")
            
            @schemas.classproperty
            def RIGHTTOAPPOINTANDREMOVEPERSON(cls):
                return cls("right-to-appoint-and-remove-person")
            
            @schemas.classproperty
            def SIGNIFICANTINFLUENCEORCONTROLASTRUSTREGISTEREDOVERSEASENTITY(cls):
                return cls("significant-influence-or-control-as-trust-registered-overseas-entity")
            
            @schemas.classproperty
            def VOTINGRIGHTSMORETHAN25PERCENTASTRUSTREGISTEREDOVERSEASENTITY(cls):
                return cls("voting-rights-more-than-25-percent-as-trust-registered-overseas-entity")
            
            @schemas.classproperty
            def RIGHTTOAPPOINTANDREMOVEDIRECTORSASTRUSTREGISTEREDOVERSEASENTITY(cls):
                return cls("right-to-appoint-and-remove-directors-as-trust-registered-overseas-entity")
            
            @schemas.classproperty
            def RIGHTTOAPPOINTANDREMOVEMEMBERSASFIRMLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("right-to-appoint-and-remove-members-as-firm-limited-liability-partnership")
            
            @schemas.classproperty
            def PARTRIGHTTOSHARESURPLUSASSETS75TO100PERCENT(cls):
                return cls("part-right-to-share-surplus-assets-75-to-100-percent")
            
            @schemas.classproperty
            def OWNERSHIPOFSHARES25TO50PERCENTASFIRM(cls):
                return cls("ownership-of-shares-25-to-50-percent-as-firm")
            
            @schemas.classproperty
            def RIGHTTOSHARESURPLUSASSETS25TO50PERCENTASTRUSTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("right-to-share-surplus-assets-25-to-50-percent-as-trust-limited-liability-partnership")
            
            @schemas.classproperty
            def RIGHTTOSHARESURPLUSASSETS50TO75PERCENTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("right-to-share-surplus-assets-50-to-75-percent-limited-liability-partnership")
            
            @schemas.classproperty
            def VOTINGRIGHTS50TO75PERCENTASFIRM(cls):
                return cls("voting-rights-50-to-75-percent-as-firm")
            
            @schemas.classproperty
            def PARTRIGHTTOSHARESURPLUSASSETS50TO75PERCENT(cls):
                return cls("part-right-to-share-surplus-assets-50-to-75-percent")
            
            @schemas.classproperty
            def RIGHTTOAPPOINTANDREMOVEDIRECTORSREGISTEREDOVERSEASENTITY(cls):
                return cls("right-to-appoint-and-remove-directors-registered-overseas-entity")
            
            @schemas.classproperty
            def SIGNIFICANTINFLUENCEORCONTROLASTRUST(cls):
                return cls("significant-influence-or-control-as-trust")
            
            @schemas.classproperty
            def RIGHTTOSHARESURPLUSASSETS75TO100PERCENTASTRUSTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("right-to-share-surplus-assets-75-to-100-percent-as-trust-limited-liability-partnership")
            
            @schemas.classproperty
            def OWNERSHIPOFSHARES50TO75PERCENTASTRUST(cls):
                return cls("ownership-of-shares-50-to-75-percent-as-trust")
            
            @schemas.classproperty
            def RIGHTTOSHARESURPLUSASSETS50TO75PERCENTASFIRMLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("right-to-share-surplus-assets-50-to-75-percent-as-firm-limited-liability-partnership")
            
            @schemas.classproperty
            def VOTINGRIGHTSMORETHAN25PERCENTASFIRMREGISTEREDOVERSEASENTITY(cls):
                return cls("voting-rights-more-than-25-percent-as-firm-registered-overseas-entity")
            
            @schemas.classproperty
            def SIGNIFICANTINFLUENCEORCONTROLASFIRMREGISTEREDOVERSEASENTITY(cls):
                return cls("significant-influence-or-control-as-firm-registered-overseas-entity")
            
            @schemas.classproperty
            def OWNERSHIPOFSHARES75TO100PERCENTASTRUST(cls):
                return cls("ownership-of-shares-75-to-100-percent-as-trust")
            
            @schemas.classproperty
            def OWNERSHIPOFSHARES50TO75PERCENT(cls):
                return cls("ownership-of-shares-50-to-75-percent")
            
            @schemas.classproperty
            def RIGHTTOSHARESURPLUSASSETS50TO75PERCENTASTRUSTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("right-to-share-surplus-assets-50-to-75-percent-as-trust-limited-liability-partnership")
            
            @schemas.classproperty
            def VOTINGRIGHTS75TO100PERCENTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("voting-rights-75-to-100-percent-limited-liability-partnership")
            
            @schemas.classproperty
            def VOTINGRIGHTSMORETHAN25PERCENTREGISTEREDOVERSEASENTITY(cls):
                return cls("voting-rights-more-than-25-percent-registered-overseas-entity")
            
            @schemas.classproperty
            def RIGHTTOAPPOINTANDREMOVEMEMBERSASTRUSTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("right-to-appoint-and-remove-members-as-trust-limited-liability-partnership")
            
            @schemas.classproperty
            def OWNERSHIPOFSHARES75TO100PERCENT(cls):
                return cls("ownership-of-shares-75-to-100-percent")
            
            @schemas.classproperty
            def PARTRIGHTTOSHARESURPLUSASSETS25TO50PERCENTASTRUST(cls):
                return cls("part-right-to-share-surplus-assets-25-to-50-percent-as-trust")
            
            @schemas.classproperty
            def VOTINGRIGHTS75TO100PERCENTASTRUSTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("voting-rights-75-to-100-percent-as-trust-limited-liability-partnership")
            
            @schemas.classproperty
            def VOTINGRIGHTS50TO75PERCENTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("voting-rights-50-to-75-percent-limited-liability-partnership")
            
            @schemas.classproperty
            def SIGNIFICANTINFLUENCEORCONTROLASTRUSTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("significant-influence-or-control-as-trust-limited-liability-partnership")
            
            @schemas.classproperty
            def VOTINGRIGHTS75TO100PERCENTASFIRMLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("voting-rights-75-to-100-percent-as-firm-limited-liability-partnership")
            
            @schemas.classproperty
            def RIGHTTOAPPOINTANDREMOVEPERSONASFIRM(cls):
                return cls("right-to-appoint-and-remove-person-as-firm")
            
            @schemas.classproperty
            def RIGHTTOAPPOINTANDREMOVEDIRECTORS(cls):
                return cls("right-to-appoint-and-remove-directors")
            
            @schemas.classproperty
            def VOTINGRIGHTS25TO50PERCENTASTRUSTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("voting-rights-25-to-50-percent-as-trust-limited-liability-partnership")
            
            @schemas.classproperty
            def VOTINGRIGHTS75TO100PERCENTASFIRM(cls):
                return cls("voting-rights-75-to-100-percent-as-firm")
            
            @schemas.classproperty
            def RIGHTTOSHARESURPLUSASSETS25TO50PERCENTLIMITEDLIABILITYPARTNERSHIP(cls):
                return cls("right-to-share-surplus-assets-25-to-50-percent-limited-liability-partnership")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CompaniesHouseGetCompanyDetailsResponsePersonsWithSignificantControlItemNaturesOfControl':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
