<div align="left">

[![Visit Griffin](./header.png)](https://griffin.com)

# Griffin<a id="griffin"></a>

## Introduction<a id="introduction"></a>

The Griffin API is based on [REST](https://en.wikipedia.org/wiki/Representational_state_transfer).
It has resource-oriented URLs, accepts [JSON](https://www.json.org/json-en.html)-encoded request bodies, returns [JSON](https://www.json.org/json-en.html)-encoded responses, and uses standard HTTP response verbs and response codes.

Our API deviates from strict RESTful principles if it makes sense to do so, such as when we enforce tighter access controls around certain operations.
For example, when closing a bank account: rather than send a PATCH request to the [bank account](http://docs.griffin.com) resource to update it's status to `\"closed\"`, we provide a dedicated account closure resource.

Anyone can [create an account](https://app.griffin.com/register) with Griffin and try out out API in [sandbox mode](http://docs.griffin.com).

New to Griffin? Check out our [getting started guide](http://docs.griffin.com).

## Navigation<a id="navigation"></a>

Our API is designed to be navigated programmatically. When you request any resource, you will find the URLs for related resources in the response body.

The API is structured as a tree with your [organization](http://docs.griffin.com) at the top. Everything that you own will be a sub-resource of your organization.

To bootstrap the navigation process, request the [index](http://docs.griffin.com) endpoint: the response will contain your `organization-url`.

For a walkthrough, see our [getting started guide](http://docs.griffin.com).

## Pagination<a id="pagination"></a>

Our list APIs support pagination (e.g. [list bank accounts](http://docs.griffin.com) and [list payments](http://docs.griffin.com)).
By default, a list API returns up to 25 results. If there are more results available, the response payload will include links to the previous/next pages.

### Change page size<a id="change-page-size"></a>

You can request a different number of results (between 1 and 200, inclusive) by using the `page[size]` query parameter:

```
GET /v0/organizations/:id/bank/accounts?page[size]=100
```

### Navigating between pages<a id="navigating-between-pages"></a>

List responses will include a `links` object with `prev` and `next` attributes, as shown below.
Perform a GET request to the value of the attribute to fetch the previous/next page of results.

```
{
  \"accounts\": [
    // ...
  ],
  \"links\": {
    \"prev\": \"/v0/organizations/og.IG9yZ2FuaXphdGlvbi1pZA/bank/accounts?page[before]=djE6WxSPxfYUTnCU9XtWzj9gGA\",
    \"next\": \"/v0/organizations/og.IG9yZ2FuaXphdGlvbi1pZA/bank/accounts?page[after]=djE6aw79PXZySUOL16LD8HRJ3A\"
  }
}

```
If there is no previous or next page available, the value of the attribute will be  null.

Any other query parameters included in the initial request will also be included in the response payload's links.
If you want to change parameters (see [filtering and sorting](http://docs.griffin.com)), request the first page and follow the links from there.

## Filtering and sorting<a id="filtering-and-sorting"></a>

### Sort results<a id="sort-results"></a>

By default, resources will be listed in descending order, usually based on the `created-at` attribute.
You can change the sorting behaviour of a list of results by using the `sort` query parameter.

For example, to list bank accounts in ascending order (oldest first):

```
GET /v0/organizations/:id/bank/accounts?sort=created-at
```

To _explicitly_ sort in descending order (newest first), prefix the sort attribute with `-`:

```
GET /v0/organizations/:id/bank/accounts?sort=-created-at
```

### Filter results<a id="filter-results"></a>

Some list APIs allow you to filter the results.
Filters are expressed as nested data structures encoded into query parameters.
For example, you can list bank accounts that are in either the `opening` or `open` state with:

```
GET /v0/organizations/:id/bank/accounts?filter[account-status][in][]=opening&filter[account-status][in][]=open
```

Similarly, you can list legal persons with a specific `application-status`:

```
GET /v0/organizations/:id/legal-persons?filter[application-status][eq]=accepted
```

### Include resources<a id="include-resources"></a>

Some list APIs allow you to include associated resources in the response, reducing the number of requests needed to fetch related data.
For instance, when listing bank accounts, you can include each bank account's beneficiary legal person by using the `include` query parameter:

```
GET /v0/organizations/:id/bank/accounts?include=beneficiary
```

The response returns the usual list of bank accounts, but it will also have an `included` object with a `legal-persons` attribute:

```
{
  \"accounts\": [
    // ...
  ],
  \"links\": {
    // ...
  }
  \"included\": {
    \"legal-persons\": [
      // ...
    ]
  }
}
```

Check the documentation for each list API to see all options for sorting and filtering

## Versioning<a id="versioning"></a>

The Griffin API is versioned via a prefix in the URL.
The current version is v0.
An example endpoint is: https://api.griffin.com/v0/index.

We will not break your integration with a particular version for as long as we support that version.
If we release a new version, you will have 12 months to upgrade to it.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`griffin.api_keys.create_key`](#griffinapi_keyscreate_key)
  * [`griffin.api_keys.get_key_details`](#griffinapi_keysget_key_details)
  * [`griffin.api_keys.list_active_keys`](#griffinapi_keyslist_active_keys)
  * [`griffin.api_keys.list_active_keys_0`](#griffinapi_keyslist_active_keys_0)
  * [`griffin.api_keys.remove_api_key`](#griffinapi_keysremove_api_key)
  * [`griffin.bank_accounts.close_account`](#griffinbank_accountsclose_account)
  * [`griffin.bank_accounts.create_new_account`](#griffinbank_accountscreate_new_account)
  * [`griffin.bank_accounts.get_account`](#griffinbank_accountsget_account)
  * [`griffin.bank_accounts.list`](#griffinbank_accountslist)
  * [`griffin.bank_accounts.update_bank_account`](#griffinbank_accountsupdate_bank_account)
  * [`griffin.claims.create_new_claim`](#griffinclaimscreate_new_claim)
  * [`griffin.claims.get_all_claims`](#griffinclaimsget_all_claims)
  * [`griffin.companies_house.get_company_details`](#griffincompanies_houseget_company_details)
  * [`griffin.connectivity.check_connection`](#griffinconnectivitycheck_connection)
  * [`griffin.decisions.create_decision`](#griffindecisionscreate_decision)
  * [`griffin.decisions.list_for_legal_person`](#griffindecisionslist_for_legal_person)
  * [`griffin.events.get_all_organization_events`](#griffineventsget_all_organization_events)
  * [`griffin.events.get_event`](#griffineventsget_event)
  * [`griffin.invitations.send_email`](#griffininvitationssend_email)
  * [`griffin.legal_person_history.list_events`](#griffinlegal_person_historylist_events)
  * [`griffin.legal_persons.create_new_legal_person`](#griffinlegal_personscreate_new_legal_person)
  * [`griffin.legal_persons.get_legal_person`](#griffinlegal_personsget_legal_person)
  * [`griffin.legal_persons.list_legal_persons`](#griffinlegal_personslist_legal_persons)
  * [`griffin.legal_persons.update_legal_person`](#griffinlegal_personsupdate_legal_person)
  * [`griffin.memberships.get_membership_info`](#griffinmembershipsget_membership_info)
  * [`griffin.memberships.list_organization_memberships`](#griffinmembershipslist_organization_memberships)
  * [`griffin.memberships.list_user_memberships`](#griffinmembershipslist_user_memberships)
  * [`griffin.memberships.remove_member`](#griffinmembershipsremove_member)
  * [`griffin.navigation.global_paths_fetch`](#griffinnavigationglobal_paths_fetch)
  * [`griffin.organizations.get_details`](#griffinorganizationsget_details)
  * [`griffin.payees.get_details`](#griffinpayeesget_details)
  * [`griffin.payees.list_legal_person_payees`](#griffinpayeeslist_legal_person_payees)
  * [`griffin.payees.register_new_payee`](#griffinpayeesregister_new_payee)
  * [`griffin.payees.update_payee`](#griffinpayeesupdate_payee)
  * [`griffin.payments.create_request`](#griffinpaymentscreate_request)
  * [`griffin.payments.get_admission`](#griffinpaymentsget_admission)
  * [`griffin.payments.get_bank_account_payments`](#griffinpaymentsget_bank_account_payments)
  * [`griffin.payments.get_details`](#griffinpaymentsget_details)
  * [`griffin.payments.get_submission`](#griffinpaymentsget_submission)
  * [`griffin.payments.list_admissions`](#griffinpaymentslist_admissions)
  * [`griffin.payments.list_bank_account_admissions`](#griffinpaymentslist_bank_account_admissions)
  * [`griffin.payments.list_submissions`](#griffinpaymentslist_submissions)
  * [`griffin.payments.list_submissions_0`](#griffinpaymentslist_submissions_0)
  * [`griffin.payments.submit_payment_submission`](#griffinpaymentssubmit_payment_submission)
  * [`griffin.pooled_account_membership.list_legal_persons`](#griffinpooled_account_membershiplist_legal_persons)
  * [`griffin.pooled_account_membership.manage_legal_persons`](#griffinpooled_account_membershipmanage_legal_persons)
  * [`griffin.reliance_onboarding.create_application`](#griffinreliance_onboardingcreate_application)
  * [`griffin.reliance_onboarding.get_application`](#griffinreliance_onboardingget_application)
  * [`griffin.roles.assign_membership_roles`](#griffinrolesassign_membership_roles)
  * [`griffin.roles.get_membership_roles`](#griffinrolesget_membership_roles)
  * [`griffin.roles.get_role`](#griffinrolesget_role)
  * [`griffin.roles.list_all_roles`](#griffinroleslist_all_roles)
  * [`griffin.transactions.get_transaction_by_id`](#griffintransactionsget_transaction_by_id)
  * [`griffin.transactions.list_balance_changes`](#griffintransactionslist_balance_changes)
  * [`griffin.users.get_user_resource`](#griffinusersget_user_resource)
  * [`griffin.verifications.get_verification`](#griffinverificationsget_verification)
  * [`griffin.verifications.initiate_verification`](#griffinverificationsinitiate_verification)
  * [`griffin.verifications.list_for_legal_person`](#griffinverificationslist_for_legal_person)
  * [`griffin.webhooks.activate_action`](#griffinwebhooksactivate_action)
  * [`griffin.webhooks.create_webhook`](#griffinwebhookscreate_webhook)
  * [`griffin.webhooks.deactivate_action`](#griffinwebhooksdeactivate_action)
  * [`griffin.webhooks.delete_webhook`](#griffinwebhooksdelete_webhook)
  * [`griffin.webhooks.get_all`](#griffinwebhooksget_all)
  * [`griffin.webhooks.get_latest_test_status`](#griffinwebhooksget_latest_test_status)
  * [`griffin.webhooks.get_webhook`](#griffinwebhooksget_webhook)
  * [`griffin.webhooks.send_test_event`](#griffinwebhookssend_test_event)
  * [`griffin.webhooks.update_webhook`](#griffinwebhooksupdate_webhook)
  * [`griffin.workflows.get_workflow`](#griffinworkflowsget_workflow)
  * [`griffin.workflows.list_organization_workflows`](#griffinworkflowslist_organization_workflows)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Griffin&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from griffin_python_sdk import Griffin, ApiException

griffin = Griffin(
    api_key_auth="YOUR_API_KEY",
)

try:
    # Create API Key
    create_key_response = griffin.api_keys.create_key(
        api_key_name=None,
        organization_id="organization-id_example",
    )
    print(create_key_response)
except ApiException as e:
    print("Exception when calling APIKeysApi.create_key: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from griffin_python_sdk import Griffin, ApiException

griffin = Griffin(
    api_key_auth="YOUR_API_KEY",
)


async def main():
    try:
        # Create API Key
        create_key_response = await griffin.api_keys.acreate_key(
            api_key_name=None,
            organization_id="organization-id_example",
        )
        print(create_key_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi.create_key: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from griffin_python_sdk import Griffin, ApiException

griffin = Griffin(
    api_key_auth="YOUR_API_KEY",
)

try:
    # Create API Key
    create_key_response = griffin.api_keys.raw.create_key(
        api_key_name=None,
        organization_id="organization-id_example",
    )
    pprint(create_key_response.body)
    pprint(create_key_response.body["api_key_url"])
    pprint(create_key_response.body["api_key_name"])
    pprint(create_key_response.body["api_key_live"])
    pprint(create_key_response.body["organization_url"])
    pprint(create_key_response.body["user_url"])
    pprint(create_key_response.body["created_at"])
    pprint(create_key_response.body["api_key_secret"])
    pprint(create_key_response.headers)
    pprint(create_key_response.status)
    pprint(create_key_response.round_trip_time)
except ApiException as e:
    print("Exception when calling APIKeysApi.create_key: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `griffin.api_keys.create_key`<a id="griffinapi_keyscreate_key"></a>

Create a new API key. This is the only time `api-key-secret` is shown.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_key_response = griffin.api_keys.create_key(
    api_key_name=None,
    organization_id="organization-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key_name: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./griffin_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="api_key_name-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

The name of the API Key. Cannot contain whitespace.

##### organization_id: `str`<a id="organization_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApiKeysCreateKeyRequest`](./griffin_python_sdk/type/api_keys_create_key_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApiKeysCreateKeyResponse`](./griffin_python_sdk/pydantic/api_keys_create_key_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/api-keys` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.api_keys.get_key_details`<a id="griffinapi_keysget_key_details"></a>

Returns the API key without `api-key-secret`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_key_details_response = griffin.api_keys.get_key_details(
    api_key_id="api-key-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key_id: `str`<a id="api_key_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApiKeysGetKeyDetailsResponse`](./griffin_python_sdk/pydantic/api_keys_get_key_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/api-keys/{api-key-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.api_keys.list_active_keys`<a id="griffinapi_keyslist_active_keys"></a>

List all active API keys in your organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_active_keys_response = griffin.api_keys.list_active_keys(
    organization_id="organization-id_example",
    sort="-created-at",
    page_size=1,
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_id: `str`<a id="organization_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`ApiKeysListActiveKeysResponse`](./griffin_python_sdk/pydantic/api_keys_list_active_keys_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/api-keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.api_keys.list_active_keys_0`<a id="griffinapi_keyslist_active_keys_0"></a>

List all your active API keys.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_active_keys_0_response = griffin.api_keys.list_active_keys_0(
    user_id="user-id_example",
    sort="-created-at",
    page_size=1,
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`ApiKeysListActiveKeys200Response`](./griffin_python_sdk/pydantic/api_keys_list_active_keys200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/users/{user-id}/api-keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.api_keys.remove_api_key`<a id="griffinapi_keysremove_api_key"></a>

Deletes the API Key. This operation cannot be undone.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
griffin.api_keys.remove_api_key(
    api_key_id="api-key-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key_id: `str`<a id="api_key_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/api-keys/{api-key-id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.bank_accounts.close_account`<a id="griffinbank_accountsclose_account"></a>

Close a bank account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
close_account_response = griffin.bank_accounts.close_account(
    bank_account_id="bank-account-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bank_account_id: `str`<a id="bank_account_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BankAccountsCloseAccountResponse`](./griffin_python_sdk/pydantic/bank_accounts_close_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/bank/accounts/{bank-account-id}/actions/close` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.bank_accounts.create_new_account`<a id="griffinbank_accountscreate_new_account"></a>

Open a new bank account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_account_response = griffin.bank_accounts.create_new_account(
    bank_product_type="operational-account",
    organization_id="organization-id_example",
    owner_url="/v0/legal-persons/lp.IGxlZ2FsLXBlcnNvbi1pZA",
    savings_type="easy-access",
    display_name="a",
    client_money_type="designated-client-fund",
    pooled_funds="false",
    beneficiary_url="/v0/legal-persons/lp.IGxlZ2FsLXBlcnNvbi1pZA",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bank_product_type: `str`<a id="bank_product_type-str"></a>

##### organization_id: `str`<a id="organization_id-str"></a>

##### owner_url: `str`<a id="owner_url-str"></a>

Link to the [legal person](http://docs.griffin.com) that represents the [owner](http://docs.griffin.com) of the account.

##### savings_type: `str`<a id="savings_type-str"></a>

Specifies the type of savings account.

##### display_name: `str`<a id="display_name-str"></a>

A human readable label for an entity

##### client_money_type: `str`<a id="client_money_type-str"></a>

Specifies the type of client money account.

##### pooled_funds: `str`<a id="pooled_funds-str"></a>

##### beneficiary_url: `str`<a id="beneficiary_url-str"></a>

Link to the [legal person](http://docs.griffin.com) that represents the [beneficiary](http://docs.griffin.com) of the account.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BankAccountsCreateNewAccountRequest`](./griffin_python_sdk/type/bank_accounts_create_new_account_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BankAccountsCreateNewAccountResponse`](./griffin_python_sdk/pydantic/bank_accounts_create_new_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/bank/accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.bank_accounts.get_account`<a id="griffinbank_accountsget_account"></a>

Fetch a bank account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_account_response = griffin.bank_accounts.get_account(
    bank_account_id="bank-account-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bank_account_id: `str`<a id="bank_account_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BankAccountsGetAccountResponse`](./griffin_python_sdk/pydantic/bank_accounts_get_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/bank/accounts/{bank-account-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.bank_accounts.list`<a id="griffinbank_accountslist"></a>

Yields a list of all bank accounts under the control of this Organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = griffin.bank_accounts.list(
    organization_id="organization-id_example",
    filter_beneficiary_eq="/v0/legal-persons/lp.IGxlZ2FsLXBlcnNvbi1pZA",
    filter_owner_eq="/v0/legal-persons/lp.IGxlZ2FsLXBlcnNvbi1pZA",
    page_size=1,
    include=["string_example"],
    filter_account_status_in_=["string_example"],
    sort="-created-at",
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    filter_account_restricted_in_=True,
    filter_pooled_funds_eq=True,
    filter_bank_product_type_in_=["string_example"],
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_id: `str`<a id="organization_id-str"></a>

##### filter_beneficiary_eq: `str`<a id="filter_beneficiary_eq-str"></a>

Link to the [legal person](http://docs.griffin.com) that represents the [beneficiary](http://docs.griffin.com) of the account.

##### filter_owner_eq: `str`<a id="filter_owner_eq-str"></a>

Link to the [legal person](http://docs.griffin.com) that represents the [owner](http://docs.griffin.com) of the account.

##### page_size: `int`<a id="page_size-int"></a>

##### include: List[`str`]<a id="include-liststr"></a>

For each bank account returned, include its owner and/or beneficiary in the response under the `included.legal-persons` attribute.

##### filter_account_status_in_: List[`str`]<a id="filter_account_status_in_-liststr"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### filter_account_restricted_in_: `bool`<a id="filter_account_restricted_in_-bool"></a>

Specifies whether the bank account has restrictions applied by Griffin.

##### filter_pooled_funds_eq: `bool`<a id="filter_pooled_funds_eq-bool"></a>

Specifies whether the bank account holds funds belonging to multiple beneficiaries.

##### filter_bank_product_type_in_: List[`str`]<a id="filter_bank_product_type_in_-liststr"></a>

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`BankAccountsListResponse`](./griffin_python_sdk/pydantic/bank_accounts_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/bank/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.bank_accounts.update_bank_account`<a id="griffinbank_accountsupdate_bank_account"></a>

Update a bank account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_bank_account_response = griffin.bank_accounts.update_bank_account(
    display_name="a",
    bank_account_id="bank-account-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### display_name: `str`<a id="display_name-str"></a>

A human readable label for an entity

##### bank_account_id: `str`<a id="bank_account_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BankAccountsUpdateBankAccountRequest`](./griffin_python_sdk/type/bank_accounts_update_bank_account_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BankAccountsUpdateBankAccountResponse`](./griffin_python_sdk/pydantic/bank_accounts_update_bank_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/bank/accounts/{bank-account-id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.claims.create_new_claim`<a id="griffinclaimscreate_new_claim"></a>

Creates a new claim about a Legal Person.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_claim_response = griffin.claims.create_new_claim(
    claim_type="tax-identification-number",
    legal_person_id="legal-person-id_example",
    mobile_number=None,
    date_of_birth="1970-01-01",
    given_name="string_example",
    surname="string_example",
    middle_name="string_example",
    trading_name="string_example",
    trading_address={},
    email_address=None,
    city="string_example",
    building_name="string_example",
    street_name="string_example",
    entity_name="string_example",
    postal_code="NW16XE",
    corporation_type="private-limited-guarant-nsc-limited-exemption",
    telephone_number=None,
    building_number="string_example",
    country_code=None,
    date_of_incorporation="1970-01-01",
    entity_registration_number="a",
    income={
        "currency": "GBP",
        "value": "1000.00",
    },
    initial_deposit={
        "currency": "GBP",
        "value": "1000.00",
    },
    international_payments_countries=[None],
    legal_person_url="/v0/legal-persons/lp.IGxlZ2FsLXBlcnNvbi1pZA",
    ownership_percent="12.34",
    companies_house_url="https://api.company-information.service.gov.uk/company/00000001/appointments/AbcDEFGhI1JKLmnO2PQ3sTUv4WX",
    senior_manager=True,
    tax_residency=None,
    uk_regulatory_permissions=["string_example"],
    business_description="a",
    individual_sources_of_funds=["string_example"],
    business_address={},
    occupation="software-engineer",
    industry_of_occupation="information-technology",
    employment_status="employed",
    annual_turnover={
        "currency": "GBP",
        "value": "1000.00",
    },
    purposes_of_account=["string_example"],
    sic_codes=["4807288800152802179809"],
    international_operations_countries=[None],
    sources_of_funds=["string_example"],
    reliance_verification_methods=["string_example"],
    reliance_verification_standard="jmlsg",
    business_name="string_example",
    individual_purposes_of_account=["string_example"],
    nationality=None,
    social_media="a",
    website_url="string_example",
    tax_identification_number="a",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### claim_type: `str`<a id="claim_type-str"></a>

##### legal_person_id: `str`<a id="legal_person_id-str"></a>

##### mobile_number: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./griffin_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="mobile_number-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### date_of_birth: `date`<a id="date_of_birth-date"></a>

ISO 8601 formatted date.

##### given_name: `str`<a id="given_name-str"></a>

##### surname: `str`<a id="surname-str"></a>

##### middle_name: `str`<a id="middle_name-str"></a>

##### trading_name: `str`<a id="trading_name-str"></a>

##### trading_address: [`Union[Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]], Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]], Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`](./griffin_python_sdk/type/typing_union_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="trading_address-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-dictstr-unionbool-date-datetime-dict-float-int-list-str-none-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_union_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### email_address: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./griffin_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="email_address-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### city: `str`<a id="city-str"></a>

##### building_name: `str`<a id="building_name-str"></a>

##### street_name: `str`<a id="street_name-str"></a>

##### entity_name: `str`<a id="entity_name-str"></a>

##### postal_code: `str`<a id="postal_code-str"></a>

##### corporation_type: `str`<a id="corporation_type-str"></a>

##### telephone_number: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./griffin_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="telephone_number-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### building_number: `str`<a id="building_number-str"></a>

##### country_code: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./griffin_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="country_code-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

ISO 3166-1 alpha-2 two-letter country code.

##### date_of_incorporation: `date`<a id="date_of_incorporation-date"></a>

ISO 8601 formatted date.

##### entity_registration_number: `str`<a id="entity_registration_number-str"></a>

The entity number assigned by the local register. For UK companies that's the Companies House company number.

##### income: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./griffin_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="income-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### initial_deposit: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./griffin_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="initial_deposit-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### international_payments_countries: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./griffin_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="international_payments_countries-listunionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### legal_person_url: `str`<a id="legal_person_url-str"></a>

A contextual link to the [legal person](http://docs.griffin.com).

##### ownership_percent: `str`<a id="ownership_percent-str"></a>

The percentage ownership the legal person has of the corporation.

##### companies_house_url: `str`<a id="companies_house_url-str"></a>

The URL of the entity in Companies House

##### senior_manager: `bool`<a id="senior_manager-bool"></a>

##### tax_residency: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./griffin_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="tax_residency-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

ISO 3166-1 alpha-2 two-letter country code.

##### uk_regulatory_permissions: List[`str`]<a id="uk_regulatory_permissions-liststr"></a>

##### business_description: `str`<a id="business_description-str"></a>

##### individual_sources_of_funds: List[`str`]<a id="individual_sources_of_funds-liststr"></a>

##### business_address: [`Union[Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]], Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]], Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`](./griffin_python_sdk/type/typing_union_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="business_address-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-dictstr-unionbool-date-datetime-dict-float-int-list-str-none-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_union_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none_typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### occupation: `str`<a id="occupation-str"></a>

Must be selected according to industry of occupation:  | industry of occupation | occupation | | ---------------------- | ---------- | | `marketing-advertising-and-pr` | `marketer` | |  | `fundraising-and-research` | |  | `sales-manager` | |  | `pr` | | `sales` | `sales` | |  | `customer-service` | |  | `exporter` | |  | `market-researcher` | |  | `importer` | |  | `buyer` | | `law` | `advocate` | |  | `solicitor` | |  | `judge` | |  | `clerk` | |  | `conveyancer` | |  | `barrister` | |  | `paralegal` | | `hospitality-and-events-management` | `butcher` | |  | `bar-manager` | |  | `caterer` | |  | `events-manager-or-organiser` | |  | `barista` | |  | `bartender` | |  | `restaurant-worker` | |  | `restaurant-owner` | |  | `chef` | |  | `fishmonger` | |  | `hotel-worker` | |  | `take-away-shop` | | `personal-care-and-lifestyle` | `nail-technician` | |  | `hairdresser` | |  | `salon-owner` | |  | `nutritionist` | |  | `aesthetician` | |  | `salon-manager` | |  | `sex-worker` | | `creative-arts-and-design` | `disc-jockey` | |  | `creative-director` | |  | `dancer` | |  | `illustrator` | |  | `graphic-designer` | |  | `interpreter-or-translator` | |  | `jewellery-designer` | |  | `tattoo-artist-or-piercer` | |  | `sound-engineer` | |  | `design-engineer` | |  | `set-and-production-designer` | |  | `fashion-stylist` | |  | `artist` | |  | `costumer` | |  | `musician` | |  | `adult-film-actor` | |  | `product-designer` | |  | `writer` | |  | `editor` | |  | `photographer` | |  | `choreographer` | |  | `copywriter` | |  | `clothing-designer` | |  | `film-director-or-producer-or-editor` | |  | `theatre-manager` | |  | `media-and-broadcasting` | |  | `actor` | | `information-technology` | `web-designer` | |  | `software-engineer` | |  | `hardware-engineer` | |  | `software-tester` | | `environment-and-agriculture` | `street-cleaner` | |  | `racehorse-trainer` | |  | `scrap-metal-dealer` | |  | `farmer` | |  | `public-health-inspection` | |  | `environmental-health-officer` | |  | `forest-manager` | |  | `conservation-worker` | |  | `food-inspector` | |  | `florist` | |  | `refuse-disposal` | | `media-and-internet` | `social-media-influencer` | |  | `printer` | |  | `journalist` | |  | `blogger` | |  | `publisher` | |  | `adult-content-creator` | |  | `editor` | | `healthcare` | `optician` | |  | `chief-medical-officer` | |  | `doctor-or-surgeon` | |  | `veterinary-nurse` | |  | `massage-therapist` | |  | `health-manager` | |  | `psychiatrist-or-therapist-or-psychologist` | |  | `veterinarian` | |  | `dietician` | |  | `physiotherapist` | |  | `nurse` | |  | `paramedic` | |  | `sports-therapist` | |  | `dentist` | |  | `speech-and-language-therapist` | |  | `alternative-and-complementary-medicine-practitioner` | | `property-and-construction` | `handyperson` | |  | `construction-worker` | |  | `architect` | |  | `landlord` | |  | `electrician` | |  | `builder` | |  | `carpenter` | |  | `plasterer` | |  | `building-services-manager` | |  | `joiner` | |  | `landscaper-or-groundsperson` | |  | `structural-engineer` | |  | `bricklayer` | |  | `plumber` | |  | `painter` | |  | `facilities-manager` | |  | `property-manager` | |  | `letting-agent` | |  | `construction-manager` | |  | `roofer` | |  | `surveyor` | |  | `estate-agent` | |  | `site-engineer` | | `public-services-and-administration` | `civil-servant` | |  | `policy-adviser` | |  | `politician` | | `law-enforcement-and-security` | `customs-officer` | |  | `police-officer` | |  | `probation-office` | |  | `forensic-psychologist` | |  | `firefighter` | |  | `security-guard` | |  | `prison-services-professional` | |  | `crime-analyst` | | `engineering-and-manufacturing` | `apparel-and-fashion-professional` | |  | `avionics` | |  | `civil-engineer` | |  | `mechanical-engineer` | |  | `aviation-and-mechanical-technician` | |  | `metal-worker` | |  | `electrical-engineer` | |  | `industrial-engineer` | |  | `metal-and-steel-worker` | |  | `glass-and-glazing-professional` | |  | `precision-instrument-worker` | |  | `manufacturing-operations` | |  | `quality-professional` | |  | `chemical-engineer` | | `energy-and-utilities` | `boilerman` | |  | `sewage-works-plant-operator` | |  | `quarry-manager` | |  | `water-and-energy-engineer` | |  | `electricity-supplier-plant-operator` | |  | `electricity-supplier-installation-engineer` | |  | `miner` | |  | `drilling-engineer` | |  | `water-treatment-controller` | | `recruitment-and-hr` | `careers-adviser` | |  | `talent-manager` | |  | `recruiter` | |  | `people-operations` | | `teacher-training-and-education` | `lecturer-or-professor` | |  | `teacher` | |  | `dance-teacher` | |  | `librarian` | |  | `teaching-assistant` | |  | `school-inspector` | |  | `curator` | |  | `conservator` | |  | `special-needs-coordinator` | |  | `education-officer` | |  | `archivist` | |  | `educational-establishment-administrator` | |  | `driving-instructor` | |  | `nanny-or-au-pair-or-child-minder` | | `leisure-sport-and-tourism` | `airport-worker` | |  | `pilot-or-flight-attendant` | |  | `professional-athlete` | |  | `travel-agency-owner` | |  | `personal-trainer` | | `business-consulting-and-management` | `entrepreneur` | |  | `compliance-manager` | |  | `management-consultant` | |  | `project-manager` | |  | `office-manager` | |  | `product-manager` | |  | `personal-assistant-or-secretary` | | `charity-and-not-for-profit-organizations` | `fundraiser-or-development-officer` | |  | `senior-management` | |  | `advocacy-officer-or-policy-analyst-or-campaign-manager` | | `transport-and-logistics` | `warehouse-worker` | |  | `taxi-driver` | |  | `transport-manager` | |  | `supply-chain-manager` | |  | `long-haul-trucker` | |  | `warehouse-manager` | |  | `bus-driver` | |  | `delivery-person` | | `science-and-pharmaceuticals` | `scientist` | |  | `researcher` | |  | `technician` | |  | `chemist` | |  | `pharmacy-manager` | |  | `pharmacist` | |  | `pharmaceutical-manufacturer` | | `social-care` | `drugs-and-alcohol-counsellor` | |  | `psychiatric-social-worker` | |  | `social-services-manager` | |  | `care-manager` | |  | `day-centre-manager` | |  | `childrens-guardian` | |  | `social-worker` | |  | `youth-worker` | |  | `foster-carer` | |  | `rehabilitation-officer` | |  | `nursing-home-owner` | |  | `welfare-services-counsellor` | | `accountancy-banking-and-finance` | `stockbroker` | |  | `finance-director` | |  | `stock-trader` | |  | `debt-advisor` | |  | `book-keeper` | |  | `chief-financial-officer` | |  | `tax-advisor` | |  | `investment-advisor` | |  | `accountant` | |  | `mortgage-advisor` | |  | `auditor` | |  | `hedge-fund-manager` | |  | `foreign-exchange-dealer` | |  | `banker` | |  | `financial-advisor` | |  | `relationship-manager` | |  | `insurance-manager` | | `retail-and-wholesale` | `wholesale-manager` | |  | `shop-owner` | |  | `retail-trade-manager` | |  | `betting-shop-manager` | |  | `newsagent` | |  | `shopkeeper` | |  | `antiques-dealer` | |  | `betting-shop-owner` | |  | `fashion-retailer` | |  | `purchaser` | |  | `car-dealer` | | `social-and-humanities-scientists` | `geographer` | |  | `epidemiologist` | |  | `archaeologist` | |  | `criminologist` | |  | `social-scientist` | |  | `political-scientist` | |  | `historian` | |  | `anthropologist` | 

##### industry_of_occupation: `str`<a id="industry_of_occupation-str"></a>

##### employment_status: `str`<a id="employment_status-str"></a>

##### annual_turnover: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./griffin_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="annual_turnover-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### purposes_of_account: List[`str`]<a id="purposes_of_account-liststr"></a>

##### sic_codes: List[`str`]<a id="sic_codes-liststr"></a>

##### international_operations_countries: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./griffin_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="international_operations_countries-listunionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### sources_of_funds: List[`str`]<a id="sources_of_funds-liststr"></a>

##### reliance_verification_methods: List[`str`]<a id="reliance_verification_methods-liststr"></a>

##### reliance_verification_standard: `str`<a id="reliance_verification_standard-str"></a>

##### business_name: `str`<a id="business_name-str"></a>

##### individual_purposes_of_account: List[`str`]<a id="individual_purposes_of_account-liststr"></a>

##### nationality: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./griffin_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="nationality-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

ISO 3166-1 alpha-2 two-letter country code.

##### social_media: `str`<a id="social_media-str"></a>

##### website_url: `str`<a id="website_url-str"></a>

##### tax_identification_number: `str`<a id="tax_identification_number-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ClaimsCreateNewClaimRequest`](./griffin_python_sdk/type/claims_create_new_claim_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ClaimsCreateNewClaimResponse`](./griffin_python_sdk/pydantic/claims_create_new_claim_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/legal-persons/{legal-person-id}/claims` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.claims.get_all_claims`<a id="griffinclaimsget_all_claims"></a>

Yields a list of all current claims about this Legal Person.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_claims_response = griffin.claims.get_all_claims(
    legal_person_id="legal-person-id_example",
    sort="-created-at",
    page_size=1,
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_person_id: `str`<a id="legal_person_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`ClaimsGetAllClaimsResponse`](./griffin_python_sdk/pydantic/claims_get_all_claims_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/legal-persons/{legal-person-id}/claims` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.companies_house.get_company_details`<a id="griffincompanies_houseget_company_details"></a>

Lookup Companies House company by company number. Includes information about the company, its directors, and persons with significant control.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_details_response = griffin.companies_house.get_company_details(
    company_number="10842931",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_number: `str`<a id="company_number-str"></a>

UK Companies House company number

#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesHouseGetCompanyDetailsResponse`](./griffin_python_sdk/pydantic/companies_house_get_company_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/companies-house/companies/{company-number}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.connectivity.check_connection`<a id="griffinconnectivitycheck_connection"></a>

Check your connection to the Griffin API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
griffin.connectivity.check_connection()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/ping` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.decisions.create_decision`<a id="griffindecisionscreate_decision"></a>

Creates a decision against the legal person.

The provided verification must have a `verification-status` of `checks-complete`, otherwise a 422 is served.

When a decision is successfully created, the legal person's `application-status` is updated accordingly.

Multiple decisions may be made against the same legal person.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_decision_response = griffin.decisions.create_decision(
    verification_url="/v0/verifications/vn.IHZlcmlmaWNhdGlvbi1pZA",
    decision_outcome="accepted",
    decision_notes="string_example",
    legal_person_id="legal-person-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### verification_url: `str`<a id="verification_url-str"></a>

A link to the [verification](http://docs.griffin.com).

##### decision_outcome: `str`<a id="decision_outcome-str"></a>

##### decision_notes: `str`<a id="decision_notes-str"></a>

Free-text field to explain the reasons behind the decision.

##### legal_person_id: `str`<a id="legal_person_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DecisionsCreateDecisionRequest`](./griffin_python_sdk/type/decisions_create_decision_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DecisionsCreateDecisionResponse`](./griffin_python_sdk/pydantic/decisions_create_decision_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/legal-persons/{legal-person-id}/decisions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.decisions.list_for_legal_person`<a id="griffindecisionslist_for_legal_person"></a>

Lists all decisions for the given legal-person.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_legal_person_response = griffin.decisions.list_for_legal_person(
    legal_person_id="legal-person-id_example",
    sort="-created-at",
    page_size=1,
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_person_id: `str`<a id="legal_person_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`DecisionsListForLegalPersonResponse`](./griffin_python_sdk/pydantic/decisions_list_for_legal_person_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/legal-persons/{legal-person-id}/decisions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.events.get_all_organization_events`<a id="griffineventsget_all_organization_events"></a>

List all events for an organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_organization_events_response = griffin.events.get_all_organization_events(
    organization_id="organization-id_example",
    sort="-created-at",
    page_size=1,
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    filter_event_type_eq="decision-created",
    filter_created_at_lte="1970-01-01T00:00:00.00Z",
    filter_created_at_lt="1970-01-01T00:00:00.00Z",
    filter_created_at_gte="1970-01-01T00:00:00.00Z",
    filter_created_at_gt="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_id: `str`<a id="organization_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### filter_event_type_eq: `str`<a id="filter_event_type_eq-str"></a>

The type of webhook event. Usually has the form {resource}-{operation}, e.g. payment-updated

##### filter_created_at_lte: `datetime`<a id="filter_created_at_lte-datetime"></a>

Return only events with a created-at less than or equal to the given timestamp.

##### filter_created_at_lt: `datetime`<a id="filter_created_at_lt-datetime"></a>

Return only events with a created-at less than the given timestamp.

##### filter_created_at_gte: `datetime`<a id="filter_created_at_gte-datetime"></a>

Return only events with a created-at greater than or equal to the given timestamp.

##### filter_created_at_gt: `datetime`<a id="filter_created_at_gt-datetime"></a>

Return only events with a created-at greater than the given timestamp.

#### 🔄 Return<a id="🔄-return"></a>

[`EventsGetAllOrganizationEventsResponse`](./griffin_python_sdk/pydantic/events_get_all_organization_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.events.get_event`<a id="griffineventsget_event"></a>

Get an event

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_response = griffin.events.get_event(
    event_id="event-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_id: `str`<a id="event_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EventsGetEventResponse`](./griffin_python_sdk/pydantic/events_get_event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/events/{event-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.invitations.send_email`<a id="griffininvitationssend_email"></a>

`POST` creates a new invitation to the organization.

Sends an email invitation to join the `organization` to the specified `email-address`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
griffin.invitations.send_email(
    email_address=None,
    organization_id="organization-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email_address: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./griffin_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="email_address-unionbool-date-datetime-dict-float-int-list-str-nonegriffin_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### organization_id: `str`<a id="organization_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InvitationsSendEmailRequest`](./griffin_python_sdk/type/invitations_send_email_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/invitations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.legal_person_history.list_events`<a id="griffinlegal_person_historylist_events"></a>

Lists history of events for the given legal person.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_events_response = griffin.legal_person_history.list_events(
    legal_person_id="legal-person-id_example",
    page_size=1,
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_person_id: `str`<a id="legal_person_id-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`LegalPersonHistoryListEventsResponse`](./griffin_python_sdk/pydantic/legal_person_history_list_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/legal-persons/{legal-person-id}/history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.legal_persons.create_new_legal_person`<a id="griffinlegal_personscreate_new_legal_person"></a>

Creates a new Legal Person. A collection of [Claims](http://docs.griffin.com) may be provided.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_legal_person_response = griffin.legal_persons.create_new_legal_person(
    display_name="a",
    legal_person_type="individual",
    organization_id="organization-id_example",
    claims=[{}],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### display_name: `str`<a id="display_name-str"></a>

A human readable label for an entity

##### legal_person_type: `str`<a id="legal_person_type-str"></a>

Specifies if the legal person is an `individual` or a `corporation`.

##### organization_id: `str`<a id="organization_id-str"></a>

##### claims: [`LegalPersonsCreateNewLegalPersonRequestClaims`](./griffin_python_sdk/type/legal_persons_create_new_legal_person_request_claims.py)<a id="claims-legalpersonscreatenewlegalpersonrequestclaimsgriffin_python_sdktypelegal_persons_create_new_legal_person_request_claimspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LegalPersonsCreateNewLegalPersonRequest`](./griffin_python_sdk/type/legal_persons_create_new_legal_person_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LegalPersonsCreateNewLegalPersonResponse`](./griffin_python_sdk/pydantic/legal_persons_create_new_legal_person_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/legal-persons` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.legal_persons.get_legal_person`<a id="griffinlegal_personsget_legal_person"></a>

Yields the legal-person.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_legal_person_response = griffin.legal_persons.get_legal_person(
    legal_person_id="legal-person-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_person_id: `str`<a id="legal_person_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`LegalPersonsGetLegalPersonResponse`](./griffin_python_sdk/pydantic/legal_persons_get_legal_person_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/legal-persons/{legal-person-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.legal_persons.list_legal_persons`<a id="griffinlegal_personslist_legal_persons"></a>

Returns a paginated list of all legal persons for the given organization.

By default, results are sorted descending by `created-at` (newest first). To sort ascending by `created-at`, provide a `?sort=created-at` query parameter. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_legal_persons_response = griffin.legal_persons.list_legal_persons(
    organization_id="organization-id_example",
    sort="-status-changed-at",
    include=["string_example"],
    filter_application_status_eq="referred",
    filter_has_=["string_example"],
    page_size=1,
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_id: `str`<a id="organization_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### include: List[`str`]<a id="include-liststr"></a>

For each legal person returned, include its latest verification (if one exists), and/or its latest risk rating (if one exists) in the response under the `included` attribute.

##### filter_application_status_eq: `str`<a id="filter_application_status_eq-str"></a>

Return only legal persons with the given application-status.

##### filter_has_: List[`str`]<a id="filter_has_-liststr"></a>

Return only legal persons with the given attributes.

##### page_size: `int`<a id="page_size-int"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`LegalPersonsListLegalPersonsResponse`](./griffin_python_sdk/pydantic/legal_persons_list_legal_persons_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/legal-persons` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.legal_persons.update_legal_person`<a id="griffinlegal_personsupdate_legal_person"></a>

Updates the legal-person.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_legal_person_response = griffin.legal_persons.update_legal_person(
    display_name="a",
    legal_person_id="legal-person-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### display_name: `str`<a id="display_name-str"></a>

A human readable label for an entity

##### legal_person_id: `str`<a id="legal_person_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LegalPersonsUpdateLegalPersonRequest`](./griffin_python_sdk/type/legal_persons_update_legal_person_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LegalPersonsUpdateLegalPersonResponse`](./griffin_python_sdk/pydantic/legal_persons_update_legal_person_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/legal-persons/{legal-person-id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.memberships.get_membership_info`<a id="griffinmembershipsget_membership_info"></a>

Returns the [user's](http://docs.griffin.com) [membership](http://docs.griffin.com) information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_membership_info_response = griffin.memberships.get_membership_info(
    membership_id="membership-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### membership_id: `str`<a id="membership_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MembershipsGetMembershipInfoResponse`](./griffin_python_sdk/pydantic/memberships_get_membership_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/memberships/{membership-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.memberships.list_organization_memberships`<a id="griffinmembershipslist_organization_memberships"></a>

Returns this [organization's](http://docs.griffin.com) [memberships](http://docs.griffin.com).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_organization_memberships_response = (
    griffin.memberships.list_organization_memberships(
        organization_id="organization-id_example",
        sort="-created-at",
        page_size=1,
        page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
        page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_id: `str`<a id="organization_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`MembershipsListOrganizationMembershipsResponse`](./griffin_python_sdk/pydantic/memberships_list_organization_memberships_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.memberships.list_user_memberships`<a id="griffinmembershipslist_user_memberships"></a>

Returns this [user's](http://docs.griffin.com) [memberships](http://docs.griffin.com).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_memberships_response = griffin.memberships.list_user_memberships(
    user_id="user-id_example",
    sort="-created-at",
    page_size=1,
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`MembershipsListUserMembershipsResponse`](./griffin_python_sdk/pydantic/memberships_list_user_memberships_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/users/{user-id}/memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.memberships.remove_member`<a id="griffinmembershipsremove_member"></a>

Removes a [user](http://docs.griffin.com) from an [organization](http://docs.griffin.com).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
griffin.memberships.remove_member(
    membership_id="membership-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### membership_id: `str`<a id="membership_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/memberships/{membership-id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.navigation.global_paths_fetch`<a id="griffinnavigationglobal_paths_fetch"></a>

Contains various global URL paths. Follow `api-key-url` to discover your `organization-url`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
global_paths_fetch_response = griffin.navigation.global_paths_fetch()
```

#### 🔄 Return<a id="🔄-return"></a>

[`NavigationGlobalPathsFetchResponse`](./griffin_python_sdk/pydantic/navigation_global_paths_fetch_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/index` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.organizations.get_details`<a id="griffinorganizationsget_details"></a>

Yields the organization details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = griffin.organizations.get_details(
    organization_id="organization-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_id: `str`<a id="organization_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsGetDetailsResponse`](./griffin_python_sdk/pydantic/organizations_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payees.get_details`<a id="griffinpayeesget_details"></a>

Yields payee details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = griffin.payees.get_details(
    payee_id="payee-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payee_id: `str`<a id="payee_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PayeesGetDetailsResponse`](./griffin_python_sdk/pydantic/payees_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/payees/{payee-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payees.list_legal_person_payees`<a id="griffinpayeeslist_legal_person_payees"></a>

Lists payees belonging to the legal person.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_legal_person_payees_response = griffin.payees.list_legal_person_payees(
    legal_person_id="legal-person-id_example",
    sort="-created-at",
    page_size=1,
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_person_id: `str`<a id="legal_person_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`PayeesListLegalPersonPayeesResponse`](./griffin_python_sdk/pydantic/payees_list_legal_person_payees_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/legal-persons/{legal-person-id}/bank/payees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payees.register_new_payee`<a id="griffinpayeesregister_new_payee"></a>

Registers a new payee for the customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
register_new_payee_response = griffin.payees.register_new_payee(
    account_holder="a",
    account_number="12345678",
    bank_id="123456",
    legal_person_id="legal-person-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_holder: `str`<a id="account_holder-str"></a>

The name of the [account holder](http://docs.griffin.com).

##### account_number: `str`<a id="account_number-str"></a>

Must be a UK BBAN.

##### bank_id: `str`<a id="bank_id-str"></a>

Must be a UK Sort Code.

##### legal_person_id: `str`<a id="legal_person_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayeesRegisterNewPayeeRequest`](./griffin_python_sdk/type/payees_register_new_payee_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayeesRegisterNewPayeeResponse`](./griffin_python_sdk/pydantic/payees_register_new_payee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/legal-persons/{legal-person-id}/bank/payees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payees.update_payee`<a id="griffinpayeesupdate_payee"></a>

Updates an existing payee.

A payee can be deactivated by updating the `payee-status` of an active payee to `deactivated`. Any attempt to create or submit a payment to a deactivated payee will fail.

A 422 is served when attempting to deactivate an already-deactivated payee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_payee_response = griffin.payees.update_payee(
    payee_status="deactivated",
    payee_id="payee-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payee_status: `str`<a id="payee_status-str"></a>

##### payee_id: `str`<a id="payee_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayeesUpdatePayeeRequest`](./griffin_python_sdk/type/payees_update_payee_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayeesUpdatePayeeResponse`](./griffin_python_sdk/pydantic/payees_update_payee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/payees/{payee-id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payments.create_request`<a id="griffinpaymentscreate_request"></a>

Registers a new payment request for the bank account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_request_response = griffin.payments.create_request(
    creditor={},
    payment_amount={
        "currency": "GBP",
        "value": "1000.00",
    },
    bank_account_id="bank-account-id_example",
    payment_reference="test reference",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### creditor: [`PaymentsCreateRequestRequestCreditor`](./griffin_python_sdk/type/payments_create_request_request_creditor.py)<a id="creditor-paymentscreaterequestrequestcreditorgriffin_python_sdktypepayments_create_request_request_creditorpy"></a>


##### payment_amount: [`PaymentsCreateRequestRequestPaymentAmount`](./griffin_python_sdk/type/payments_create_request_request_payment_amount.py)<a id="payment_amount-paymentscreaterequestrequestpaymentamountgriffin_python_sdktypepayments_create_request_request_payment_amountpy"></a>


##### bank_account_id: `str`<a id="bank_account_id-str"></a>

##### payment_reference: `str`<a id="payment_reference-str"></a>

Free-text field to help identify and categorise payments.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentsCreateRequestRequest`](./griffin_python_sdk/type/payments_create_request_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsCreateRequestResponse`](./griffin_python_sdk/pydantic/payments_create_request_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/bank/accounts/{bank-account-id}/payments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payments.get_admission`<a id="griffinpaymentsget_admission"></a>

Yields an admission.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_admission_response = griffin.payments.get_admission(
    admission_id="admission-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### admission_id: `str`<a id="admission_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsGetAdmissionResponse`](./griffin_python_sdk/pydantic/payments_get_admission_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/admissions/{admission-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payments.get_bank_account_payments`<a id="griffinpaymentsget_bank_account_payments"></a>

Lists payments made from a bank account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bank_account_payments_response = griffin.payments.get_bank_account_payments(
    bank_account_id="bank-account-id_example",
    sort="-created-at",
    page_size=1,
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    filter_created_at_lte="1970-01-01T00:00:00.00Z",
    filter_created_at_lt="1970-01-01T00:00:00.00Z",
    filter_created_at_gte="1970-01-01T00:00:00.00Z",
    filter_created_at_gt="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bank_account_id: `str`<a id="bank_account_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### filter_created_at_lte: `datetime`<a id="filter_created_at_lte-datetime"></a>

Return only resources with a created-at less than or equal to the given timestamp.

##### filter_created_at_lt: `datetime`<a id="filter_created_at_lt-datetime"></a>

Return only resources with a created-at less than the given timestamp.

##### filter_created_at_gte: `datetime`<a id="filter_created_at_gte-datetime"></a>

Return only resources with a created-at greater than or equal to the given timestamp.

##### filter_created_at_gt: `datetime`<a id="filter_created_at_gt-datetime"></a>

Return only resources with a created-at greater than the given timestamp.

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsGetBankAccountPaymentsResponse`](./griffin_python_sdk/pydantic/payments_get_bank_account_payments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/bank/accounts/{bank-account-id}/payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payments.get_details`<a id="griffinpaymentsget_details"></a>

Yields payment details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = griffin.payments.get_details(
    payment_id="payment-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_id: `str`<a id="payment_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsGetDetailsResponse`](./griffin_python_sdk/pydantic/payments_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/payments/{payment-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payments.get_submission`<a id="griffinpaymentsget_submission"></a>

Yields a submission.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_submission_response = griffin.payments.get_submission(
    submission_id="submission-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### submission_id: `str`<a id="submission_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsGetSubmissionResponse`](./griffin_python_sdk/pydantic/payments_get_submission_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/submissions/{submission-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payments.list_admissions`<a id="griffinpaymentslist_admissions"></a>

Lists admissions for a payment. A payment may have at most one admission.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_admissions_response = griffin.payments.list_admissions(
    payment_id="payment-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_id: `str`<a id="payment_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsListAdmissionsResponse`](./griffin_python_sdk/pydantic/payments_list_admissions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/payments/{payment-id}/admissions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payments.list_bank_account_admissions`<a id="griffinpaymentslist_bank_account_admissions"></a>

Lists admissions targeting a bank account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_bank_account_admissions_response = griffin.payments.list_bank_account_admissions(
    bank_account_id="bank-account-id_example",
    sort="-created-at",
    page_size=1,
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    filter_created_at_lte="1970-01-01T00:00:00.00Z",
    filter_created_at_lt="1970-01-01T00:00:00.00Z",
    filter_created_at_gte="1970-01-01T00:00:00.00Z",
    filter_created_at_gt="1970-01-01T00:00:00.00Z",
    filter_admission_status_in=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bank_account_id: `str`<a id="bank_account_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### filter_created_at_lte: `datetime`<a id="filter_created_at_lte-datetime"></a>

Return only resources with a created-at less than or equal to the given timestamp.

##### filter_created_at_lt: `datetime`<a id="filter_created_at_lt-datetime"></a>

Return only resources with a created-at less than the given timestamp.

##### filter_created_at_gte: `datetime`<a id="filter_created_at_gte-datetime"></a>

Return only resources with a created-at greater than or equal to the given timestamp.

##### filter_created_at_gt: `datetime`<a id="filter_created_at_gt-datetime"></a>

Return only resources with a created-at greater than the given timestamp.

##### filter_admission_status_in: List[`str`]<a id="filter_admission_status_in-liststr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsListBankAccountAdmissionsResponse`](./griffin_python_sdk/pydantic/payments_list_bank_account_admissions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/bank/accounts/{bank-account-id}/admissions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payments.list_submissions`<a id="griffinpaymentslist_submissions"></a>

Lists submissions originating from a bank account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_submissions_response = griffin.payments.list_submissions(
    bank_account_id="bank-account-id_example",
    sort="-created-at",
    page_size=1,
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    filter_submission_status_in=["string_example"],
    filter_created_at_lte="1970-01-01T00:00:00.00Z",
    filter_created_at_lt="1970-01-01T00:00:00.00Z",
    filter_created_at_gte="1970-01-01T00:00:00.00Z",
    filter_created_at_gt="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bank_account_id: `str`<a id="bank_account_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### filter_submission_status_in: List[`str`]<a id="filter_submission_status_in-liststr"></a>

##### filter_created_at_lte: `datetime`<a id="filter_created_at_lte-datetime"></a>

Return only resources with a created-at less than or equal to the given timestamp.

##### filter_created_at_lt: `datetime`<a id="filter_created_at_lt-datetime"></a>

Return only resources with a created-at less than the given timestamp.

##### filter_created_at_gte: `datetime`<a id="filter_created_at_gte-datetime"></a>

Return only resources with a created-at greater than or equal to the given timestamp.

##### filter_created_at_gt: `datetime`<a id="filter_created_at_gt-datetime"></a>

Return only resources with a created-at greater than the given timestamp.

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsListSubmissionsResponse`](./griffin_python_sdk/pydantic/payments_list_submissions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/bank/accounts/{bank-account-id}/submissions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payments.list_submissions_0`<a id="griffinpaymentslist_submissions_0"></a>

Lists submissions for a payment. The presence of a submission means that the payment has been submitted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_submissions_0_response = griffin.payments.list_submissions_0(
    payment_id="payment-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_id: `str`<a id="payment_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsListSubmissions200Response`](./griffin_python_sdk/pydantic/payments_list_submissions200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/payments/{payment-id}/submissions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.payments.submit_payment_submission`<a id="griffinpaymentssubmit_payment_submission"></a>

Submits a previously created payment for execution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_payment_submission_response = griffin.payments.submit_payment_submission(
    payment_id="payment-id_example",
    payment_scheme="fps",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_id: `str`<a id="payment_id-str"></a>

##### payment_scheme: `str`<a id="payment_scheme-str"></a>

Specifies the scheme over which a payment is executed.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentsSubmitPaymentSubmissionRequest`](./griffin_python_sdk/type/payments_submit_payment_submission_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsSubmitPaymentSubmissionResponse`](./griffin_python_sdk/pydantic/payments_submit_payment_submission_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/payments/{payment-id}/submissions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.pooled_account_membership.list_legal_persons`<a id="griffinpooled_account_membershiplist_legal_persons"></a>

List legal persons in a pooled account membership

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_legal_persons_response = griffin.pooled_account_membership.list_legal_persons(
    bank_account_id="bank-account-id_example",
    include=["string_example"],
    page_size=1,
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bank_account_id: `str`<a id="bank_account_id-str"></a>

##### include: List[`str`]<a id="include-liststr"></a>

For each member returned, include its legal person details, latest verification (if one exists), and/or latest risk rating (if one exists) in the response under the `included` attribute.

##### page_size: `int`<a id="page_size-int"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`PooledAccountMembershipListLegalPersonsResponse`](./griffin_python_sdk/pydantic/pooled_account_membership_list_legal_persons_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/bank/accounts/{bank-account-id}/membership` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.pooled_account_membership.manage_legal_persons`<a id="griffinpooled_account_membershipmanage_legal_persons"></a>

Add and update the legal persons in a pooled account membership. Limited to 2000 legal persons per operation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
manage_legal_persons_response = griffin.pooled_account_membership.manage_legal_persons(
    additions=["string_example"],
    deletions=["string_example"],
    bank_account_id="bank-account-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### additions: [`PooledAccountMembershipManageLegalPersonsRequestAdditions`](./griffin_python_sdk/type/pooled_account_membership_manage_legal_persons_request_additions.py)<a id="additions-pooledaccountmembershipmanagelegalpersonsrequestadditionsgriffin_python_sdktypepooled_account_membership_manage_legal_persons_request_additionspy"></a>

##### deletions: [`PooledAccountMembershipManageLegalPersonsRequestDeletions`](./griffin_python_sdk/type/pooled_account_membership_manage_legal_persons_request_deletions.py)<a id="deletions-pooledaccountmembershipmanagelegalpersonsrequestdeletionsgriffin_python_sdktypepooled_account_membership_manage_legal_persons_request_deletionspy"></a>

##### bank_account_id: `str`<a id="bank_account_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PooledAccountMembershipManageLegalPersonsRequest`](./griffin_python_sdk/type/pooled_account_membership_manage_legal_persons_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PooledAccountMembershipManageLegalPersonsResponse`](./griffin_python_sdk/pydantic/pooled_account_membership_manage_legal_persons_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/bank/accounts/{bank-account-id}/membership-updates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.reliance_onboarding.create_application`<a id="griffinreliance_onboardingcreate_application"></a>

Create an onboarding application and submit it for processing.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_application_response = griffin.reliance_onboarding.create_application(
    workflow_url="/v0/workflows/wf.ICAgICB3b3JrZmxvdy1pZA",
    subject_profile={
        "display_name": "display_name_example",
        "claims": [{}],
    },
    organization_id="organization-id_example",
    related_profiles=[
        {
            "display_name": "display_name_example",
            "subject_association": {},
            "claims": [{}],
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workflow_url: `str`<a id="workflow_url-str"></a>

A link to the [workflow](http://docs.griffin.com).

##### subject_profile: [`RelianceOnboardingCreateApplicationRequestSubjectProfile`](./griffin_python_sdk/type/reliance_onboarding_create_application_request_subject_profile.py)<a id="subject_profile-relianceonboardingcreateapplicationrequestsubjectprofilegriffin_python_sdktypereliance_onboarding_create_application_request_subject_profilepy"></a>


##### organization_id: `str`<a id="organization_id-str"></a>

##### related_profiles: [`RelianceOnboardingCreateApplicationRequestRelatedProfiles`](./griffin_python_sdk/type/reliance_onboarding_create_application_request_related_profiles.py)<a id="related_profiles-relianceonboardingcreateapplicationrequestrelatedprofilesgriffin_python_sdktypereliance_onboarding_create_application_request_related_profilespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RelianceOnboardingCreateApplicationRequest`](./griffin_python_sdk/type/reliance_onboarding_create_application_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RelianceOnboardingCreateApplicationResponse`](./griffin_python_sdk/pydantic/reliance_onboarding_create_application_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/onboarding/applications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.reliance_onboarding.get_application`<a id="griffinreliance_onboardingget_application"></a>

Fetch an onboarding application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_application_response = griffin.reliance_onboarding.get_application(
    onboarding_application_id="onboarding-application-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### onboarding_application_id: `str`<a id="onboarding_application_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RelianceOnboardingGetApplicationResponse`](./griffin_python_sdk/pydantic/reliance_onboarding_get_application_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/onboarding/applications/{onboarding-application-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.roles.assign_membership_roles`<a id="griffinrolesassign_membership_roles"></a>

Assigns [roles](http://docs.griffin.com) to the [membership](http://docs.griffin.com).

A 422 is served if you provide a role that is not in the [Organisations](http://docs.griffin.com) `"available-roles"`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_membership_roles_response = griffin.roles.assign_membership_roles(
    role_urls=["string_example"],
    membership_id="membership-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### role_urls: [`RolesAssignMembershipRolesRequestRoleUrls`](./griffin_python_sdk/type/roles_assign_membership_roles_request_role_urls.py)<a id="role_urls-rolesassignmembershiprolesrequestroleurlsgriffin_python_sdktyperoles_assign_membership_roles_request_role_urlspy"></a>

##### membership_id: `str`<a id="membership_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RolesAssignMembershipRolesRequest`](./griffin_python_sdk/type/roles_assign_membership_roles_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RolesAssignMembershipRolesResponse`](./griffin_python_sdk/pydantic/roles_assign_membership_roles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/memberships/{membership-id}/roles` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.roles.get_membership_roles`<a id="griffinrolesget_membership_roles"></a>

Returns the [roles](http://docs.griffin.com) assigned to this [membership](http://docs.griffin.com).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_membership_roles_response = griffin.roles.get_membership_roles(
    membership_id="membership-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### membership_id: `str`<a id="membership_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RolesGetMembershipRolesResponse`](./griffin_python_sdk/pydantic/roles_get_membership_roles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/memberships/{membership-id}/roles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.roles.get_role`<a id="griffinrolesget_role"></a>

Yields the Role resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_role_response = griffin.roles.get_role(
    role_id="role-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### role_id: `str`<a id="role_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RolesGetRoleResponse`](./griffin_python_sdk/pydantic/roles_get_role_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/roles/{role-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.roles.list_all_roles`<a id="griffinroleslist_all_roles"></a>

Yields a list of all Role resources.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_roles_response = griffin.roles.list_all_roles()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RolesListAllRolesResponse`](./griffin_python_sdk/pydantic/roles_list_all_roles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/roles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.transactions.get_transaction_by_id`<a id="griffintransactionsget_transaction_by_id"></a>

Yields a bank account transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_transaction_by_id_response = griffin.transactions.get_transaction_by_id(
    transaction_id="transaction-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction_id: `str`<a id="transaction_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionsGetTransactionByIdResponse`](./griffin_python_sdk/pydantic/transactions_get_transaction_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/bank/transactions/{transaction-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.transactions.list_balance_changes`<a id="griffintransactionslist_balance_changes"></a>

Lists balance changes on a bank account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_balance_changes_response = griffin.transactions.list_balance_changes(
    bank_account_id="bank-account-id_example",
    sort="-created-at",
    page_size=1,
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    include="payment",
    filter_post_datetime_lte="1970-01-01T00:00:00.00Z",
    filter_post_datetime_lt="1970-01-01T00:00:00.00Z",
    filter_post_datetime_gte="1970-01-01T00:00:00.00Z",
    filter_post_datetime_gt="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bank_account_id: `str`<a id="bank_account_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### include: `str`<a id="include-str"></a>

For each transaction returned, include its payment (if one exists) in the response under the `included` attribute.

##### filter_post_datetime_lte: `datetime`<a id="filter_post_datetime_lte-datetime"></a>

Return only resources with a created-at less than or equal to the given timestamp.

##### filter_post_datetime_lt: `datetime`<a id="filter_post_datetime_lt-datetime"></a>

Return only resources with a created-at less than the given timestamp.

##### filter_post_datetime_gte: `datetime`<a id="filter_post_datetime_gte-datetime"></a>

Return only resources with a created-at greater than or equal to the given timestamp.

##### filter_post_datetime_gt: `datetime`<a id="filter_post_datetime_gt-datetime"></a>

Return only resources with a created-at greater than the given timestamp.

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionsListBalanceChangesResponse`](./griffin_python_sdk/pydantic/transactions_list_balance_changes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/bank/accounts/{bank-account-id}/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.users.get_user_resource`<a id="griffinusersget_user_resource"></a>

Get the User resource for the current user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_resource_response = griffin.users.get_user_resource(
    user_id="user-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetUserResourceResponse`](./griffin_python_sdk/pydantic/users_get_user_resource_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/users/{user-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.verifications.get_verification`<a id="griffinverificationsget_verification"></a>

Fetch the verification.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_verification_response = griffin.verifications.get_verification(
    verification_id="verification-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### verification_id: `str`<a id="verification_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`VerificationsGetVerificationResponse`](./griffin_python_sdk/pydantic/verifications_get_verification_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/verifications/{verification-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.verifications.initiate_verification`<a id="griffinverificationsinitiate_verification"></a>

Initiates verification of the subject legal person.

The request body must include a `workflow-url` to determine checks to be
performed by the verification. The workflow specified determines which claims
must exist for the subject legal person, as identified in the request URL, and any
associated legal persons (i.e. directors and people with significant control of a
corporation).

These claims can be found in the `required-claim-types` field on a [Workflow](http://docs.griffin.com).

---

Once a verification is created, the system will perform checks on the claim details.
The status of check processing is indicated by the `verification-status` in the response body.
Initially it will be `pending`, and will transition through `in-progress` to a final status of `checks-complete`.

A `verification-status` of `failed` indicates something went wrong during check processing.
You can initiate another verification to retry the check processing.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
initiate_verification_response = griffin.verifications.initiate_verification(
    workflow_url="/v0/workflows/wf.ICAgICB3b3JrZmxvdy1pZA",
    legal_person_id="legal-person-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workflow_url: `str`<a id="workflow_url-str"></a>

A link to the [workflow](http://docs.griffin.com).

##### legal_person_id: `str`<a id="legal_person_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VerificationsInitiateVerificationRequest`](./griffin_python_sdk/type/verifications_initiate_verification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VerificationsInitiateVerificationResponse`](./griffin_python_sdk/pydantic/verifications_initiate_verification_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/legal-persons/{legal-person-id}/verifications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.verifications.list_for_legal_person`<a id="griffinverificationslist_for_legal_person"></a>

List verifications for the given legal person.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_legal_person_response = griffin.verifications.list_for_legal_person(
    legal_person_id="legal-person-id_example",
    sort="-created-at",
    page_size=1,
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_person_id: `str`<a id="legal_person_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`VerificationsListForLegalPersonResponse`](./griffin_python_sdk/pydantic/verifications_list_for_legal_person_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/legal-persons/{legal-person-id}/verifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.webhooks.activate_action`<a id="griffinwebhooksactivate_action"></a>

Activate a webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_action_response = griffin.webhooks.activate_action(
    webhook_id="webhook-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksActivateActionResponse`](./griffin_python_sdk/pydantic/webhooks_activate_action_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/webhooks/{webhook-id}/actions/activate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.webhooks.create_webhook`<a id="griffinwebhookscreate_webhook"></a>

Create a webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_webhook_response = griffin.webhooks.create_webhook(
    webhook_destination_url="https://example.com/griffin/webhook/",
    organization_id="organization-id_example",
    webhook_description="Griffin API webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_destination_url: `str`<a id="webhook_destination_url-str"></a>

The callback URL of the webhook

##### organization_id: `str`<a id="organization_id-str"></a>

##### webhook_description: `str`<a id="webhook_description-str"></a>

A description of the webhook

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksCreateWebhookRequest`](./griffin_python_sdk/type/webhooks_create_webhook_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksCreateWebhookResponse`](./griffin_python_sdk/pydantic/webhooks_create_webhook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.webhooks.deactivate_action`<a id="griffinwebhooksdeactivate_action"></a>

Deactivate a webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deactivate_action_response = griffin.webhooks.deactivate_action(
    webhook_id="webhook-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksDeactivateActionResponse`](./griffin_python_sdk/pydantic/webhooks_deactivate_action_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/webhooks/{webhook-id}/actions/deactivate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.webhooks.delete_webhook`<a id="griffinwebhooksdelete_webhook"></a>

Delete a webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
griffin.webhooks.delete_webhook(
    webhook_id="webhook-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/webhooks/{webhook-id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.webhooks.get_all`<a id="griffinwebhooksget_all"></a>

Get all webhooks for the organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = griffin.webhooks.get_all(
    organization_id="organization-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_id: `str`<a id="organization_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksGetAllResponse`](./griffin_python_sdk/pydantic/webhooks_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.webhooks.get_latest_test_status`<a id="griffinwebhooksget_latest_test_status"></a>

Get the status of the latest test event

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_latest_test_status_response = griffin.webhooks.get_latest_test_status(
    webhook_id="webhook-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksGetLatestTestStatusResponse`](./griffin_python_sdk/pydantic/webhooks_get_latest_test_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/webhooks/{webhook-id}/actions/test` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.webhooks.get_webhook`<a id="griffinwebhooksget_webhook"></a>

Fetch a webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_webhook_response = griffin.webhooks.get_webhook(
    webhook_id="webhook-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksGetWebhookResponse`](./griffin_python_sdk/pydantic/webhooks_get_webhook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/webhooks/{webhook-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.webhooks.send_test_event`<a id="griffinwebhookssend_test_event"></a>

Send a test event to the webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_test_event_response = griffin.webhooks.send_test_event(
    webhook_id="webhook-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksSendTestEventResponse`](./griffin_python_sdk/pydantic/webhooks_send_test_event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/webhooks/{webhook-id}/actions/test` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.webhooks.update_webhook`<a id="griffinwebhooksupdate_webhook"></a>

Update a webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_webhook_response = griffin.webhooks.update_webhook(
    webhook_id="webhook-id_example",
    webhook_description="Griffin API webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

##### webhook_description: `str`<a id="webhook_description-str"></a>

A description of the webhook

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksUpdateWebhookRequest`](./griffin_python_sdk/type/webhooks_update_webhook_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksUpdateWebhookResponse`](./griffin_python_sdk/pydantic/webhooks_update_webhook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/webhooks/{webhook-id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.workflows.get_workflow`<a id="griffinworkflowsget_workflow"></a>

Fetch the workflow.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_workflow_response = griffin.workflows.get_workflow(
    workflow_id="workflow-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workflow_id: `str`<a id="workflow_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowsGetWorkflowResponse`](./griffin_python_sdk/pydantic/workflows_get_workflow_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/workflows/{workflow-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `griffin.workflows.list_organization_workflows`<a id="griffinworkflowslist_organization_workflows"></a>

Lists workflows for use when creating a [verification](http://docs.griffin.com).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_organization_workflows_response = griffin.workflows.list_organization_workflows(
    organization_id="organization-id_example",
    sort="-created-at",
    page_size=1,
    page_after="djE6NL0DfDTSUk67KJKCi-L5Zg",
    page_before="djE6NL0DfDTSUk67KJKCi-L5Zg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_id: `str`<a id="organization_id-str"></a>

##### sort: `str`<a id="sort-str"></a>

##### page_size: `int`<a id="page_size-int"></a>

##### page_after: `str`<a id="page_after-str"></a>

A base64 encoded opaque string returned in paginated responses.

##### page_before: `str`<a id="page_before-str"></a>

A base64 encoded opaque string returned in paginated responses.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowsListOrganizationWorkflowsResponse`](./griffin_python_sdk/pydantic/workflows_list_organization_workflows_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v0/organizations/{organization-id}/workflows` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
