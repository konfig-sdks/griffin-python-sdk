import typing_extensions

from griffin_python_sdk.apis.tags import TagValues
from griffin_python_sdk.apis.tags.payments_api import PaymentsApi
from griffin_python_sdk.apis.tags.webhooks_api import WebhooksApi
from griffin_python_sdk.apis.tags.bank_accounts_api import BankAccountsApi
from griffin_python_sdk.apis.tags.api_keys_api import APIKeysApi
from griffin_python_sdk.apis.tags.legal_persons_api import LegalPersonsApi
from griffin_python_sdk.apis.tags.payees_api import PayeesApi
from griffin_python_sdk.apis.tags.memberships_api import MembershipsApi
from griffin_python_sdk.apis.tags.roles_api import RolesApi
from griffin_python_sdk.apis.tags.verifications_api import VerificationsApi
from griffin_python_sdk.apis.tags.claims_api import ClaimsApi
from griffin_python_sdk.apis.tags.workflows_api import WorkflowsApi
from griffin_python_sdk.apis.tags.reliance_onboarding_api import RelianceOnboardingApi
from griffin_python_sdk.apis.tags.transactions_api import TransactionsApi
from griffin_python_sdk.apis.tags.pooled_account_membership_api import PooledAccountMembershipApi
from griffin_python_sdk.apis.tags.events_api import EventsApi
from griffin_python_sdk.apis.tags.decisions_api import DecisionsApi
from griffin_python_sdk.apis.tags.organizations_api import OrganizationsApi
from griffin_python_sdk.apis.tags.users_api import UsersApi
from griffin_python_sdk.apis.tags.invitations_api import InvitationsApi
from griffin_python_sdk.apis.tags.navigation_api import NavigationApi
from griffin_python_sdk.apis.tags.connectivity_api import ConnectivityApi
from griffin_python_sdk.apis.tags.companies_house_api import CompaniesHouseApi
from griffin_python_sdk.apis.tags.legal_person_history_api import LegalPersonHistoryApi
from griffin_python_sdk.apis.tags.getting_started_api import GettingStartedApi
from griffin_python_sdk.apis.tags.customer_verifications_api import CustomerVerificationsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PAYMENTS: PaymentsApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.BANK_ACCOUNTS: BankAccountsApi,
        TagValues.API_KEYS: APIKeysApi,
        TagValues.LEGAL_PERSONS: LegalPersonsApi,
        TagValues.PAYEES: PayeesApi,
        TagValues.MEMBERSHIPS: MembershipsApi,
        TagValues.ROLES: RolesApi,
        TagValues.VERIFICATIONS: VerificationsApi,
        TagValues.CLAIMS: ClaimsApi,
        TagValues.WORKFLOWS: WorkflowsApi,
        TagValues.RELIANCE_ONBOARDING: RelianceOnboardingApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.POOLED_ACCOUNT_MEMBERSHIP: PooledAccountMembershipApi,
        TagValues.EVENTS: EventsApi,
        TagValues.DECISIONS: DecisionsApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.USERS: UsersApi,
        TagValues.INVITATIONS: InvitationsApi,
        TagValues.NAVIGATION: NavigationApi,
        TagValues.CONNECTIVITY: ConnectivityApi,
        TagValues.COMPANIES_HOUSE: CompaniesHouseApi,
        TagValues.LEGAL_PERSON_HISTORY: LegalPersonHistoryApi,
        TagValues.GETTING_STARTED: GettingStartedApi,
        TagValues.CUSTOMER_VERIFICATIONS: CustomerVerificationsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PAYMENTS: PaymentsApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.BANK_ACCOUNTS: BankAccountsApi,
        TagValues.API_KEYS: APIKeysApi,
        TagValues.LEGAL_PERSONS: LegalPersonsApi,
        TagValues.PAYEES: PayeesApi,
        TagValues.MEMBERSHIPS: MembershipsApi,
        TagValues.ROLES: RolesApi,
        TagValues.VERIFICATIONS: VerificationsApi,
        TagValues.CLAIMS: ClaimsApi,
        TagValues.WORKFLOWS: WorkflowsApi,
        TagValues.RELIANCE_ONBOARDING: RelianceOnboardingApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.POOLED_ACCOUNT_MEMBERSHIP: PooledAccountMembershipApi,
        TagValues.EVENTS: EventsApi,
        TagValues.DECISIONS: DecisionsApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.USERS: UsersApi,
        TagValues.INVITATIONS: InvitationsApi,
        TagValues.NAVIGATION: NavigationApi,
        TagValues.CONNECTIVITY: ConnectivityApi,
        TagValues.COMPANIES_HOUSE: CompaniesHouseApi,
        TagValues.LEGAL_PERSON_HISTORY: LegalPersonHistoryApi,
        TagValues.GETTING_STARTED: GettingStartedApi,
        TagValues.CUSTOMER_VERIFICATIONS: CustomerVerificationsApi,
    }
)
