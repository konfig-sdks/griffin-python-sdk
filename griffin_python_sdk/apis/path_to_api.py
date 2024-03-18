import typing_extensions

from griffin_python_sdk.paths import PathValues
from griffin_python_sdk.apis.paths.v0_index import V0Index
from griffin_python_sdk.apis.paths.v0_ping import V0Ping
from griffin_python_sdk.apis.paths.v0_admissions_admission_id import V0AdmissionsAdmissionId
from griffin_python_sdk.apis.paths.v0_api_keys_api_key_id import V0ApiKeysApiKeyId
from griffin_python_sdk.apis.paths.v0_bank_accounts_bank_account_id import V0BankAccountsBankAccountId
from griffin_python_sdk.apis.paths.v0_bank_accounts_bank_account_id_actions_close import V0BankAccountsBankAccountIdActionsClose
from griffin_python_sdk.apis.paths.v0_bank_accounts_bank_account_id_admissions import V0BankAccountsBankAccountIdAdmissions
from griffin_python_sdk.apis.paths.v0_bank_accounts_bank_account_id_membership import V0BankAccountsBankAccountIdMembership
from griffin_python_sdk.apis.paths.v0_bank_accounts_bank_account_id_membership_updates import V0BankAccountsBankAccountIdMembershipUpdates
from griffin_python_sdk.apis.paths.v0_bank_accounts_bank_account_id_payments import V0BankAccountsBankAccountIdPayments
from griffin_python_sdk.apis.paths.v0_bank_accounts_bank_account_id_submissions import V0BankAccountsBankAccountIdSubmissions
from griffin_python_sdk.apis.paths.v0_bank_accounts_bank_account_id_transactions import V0BankAccountsBankAccountIdTransactions
from griffin_python_sdk.apis.paths.v0_bank_transactions_transaction_id import V0BankTransactionsTransactionId
from griffin_python_sdk.apis.paths.v0_companies_house_companies_company_number import V0CompaniesHouseCompaniesCompanyNumber
from griffin_python_sdk.apis.paths.v0_events_event_id import V0EventsEventId
from griffin_python_sdk.apis.paths.v0_legal_persons_legal_person_id import V0LegalPersonsLegalPersonId
from griffin_python_sdk.apis.paths.v0_legal_persons_legal_person_id_bank_payees import V0LegalPersonsLegalPersonIdBankPayees
from griffin_python_sdk.apis.paths.v0_legal_persons_legal_person_id_claims import V0LegalPersonsLegalPersonIdClaims
from griffin_python_sdk.apis.paths.v0_legal_persons_legal_person_id_decisions import V0LegalPersonsLegalPersonIdDecisions
from griffin_python_sdk.apis.paths.v0_legal_persons_legal_person_id_history import V0LegalPersonsLegalPersonIdHistory
from griffin_python_sdk.apis.paths.v0_legal_persons_legal_person_id_verifications import V0LegalPersonsLegalPersonIdVerifications
from griffin_python_sdk.apis.paths.v0_memberships_membership_id import V0MembershipsMembershipId
from griffin_python_sdk.apis.paths.v0_memberships_membership_id_roles import V0MembershipsMembershipIdRoles
from griffin_python_sdk.apis.paths.v0_onboarding_applications_onboarding_application_id import V0OnboardingApplicationsOnboardingApplicationId
from griffin_python_sdk.apis.paths.v0_organizations_organization_id import V0OrganizationsOrganizationId
from griffin_python_sdk.apis.paths.v0_organizations_organization_id_api_keys import V0OrganizationsOrganizationIdApiKeys
from griffin_python_sdk.apis.paths.v0_organizations_organization_id_bank_accounts import V0OrganizationsOrganizationIdBankAccounts
from griffin_python_sdk.apis.paths.v0_organizations_organization_id_events import V0OrganizationsOrganizationIdEvents
from griffin_python_sdk.apis.paths.v0_organizations_organization_id_invitations import V0OrganizationsOrganizationIdInvitations
from griffin_python_sdk.apis.paths.v0_organizations_organization_id_legal_persons import V0OrganizationsOrganizationIdLegalPersons
from griffin_python_sdk.apis.paths.v0_organizations_organization_id_memberships import V0OrganizationsOrganizationIdMemberships
from griffin_python_sdk.apis.paths.v0_organizations_organization_id_onboarding_applications import V0OrganizationsOrganizationIdOnboardingApplications
from griffin_python_sdk.apis.paths.v0_organizations_organization_id_webhooks import V0OrganizationsOrganizationIdWebhooks
from griffin_python_sdk.apis.paths.v0_organizations_organization_id_workflows import V0OrganizationsOrganizationIdWorkflows
from griffin_python_sdk.apis.paths.v0_payees_payee_id import V0PayeesPayeeId
from griffin_python_sdk.apis.paths.v0_payments_payment_id import V0PaymentsPaymentId
from griffin_python_sdk.apis.paths.v0_payments_payment_id_admissions import V0PaymentsPaymentIdAdmissions
from griffin_python_sdk.apis.paths.v0_payments_payment_id_submissions import V0PaymentsPaymentIdSubmissions
from griffin_python_sdk.apis.paths.v0_roles import V0Roles
from griffin_python_sdk.apis.paths.v0_roles_role_id import V0RolesRoleId
from griffin_python_sdk.apis.paths.v0_submissions_submission_id import V0SubmissionsSubmissionId
from griffin_python_sdk.apis.paths.v0_users_user_id import V0UsersUserId
from griffin_python_sdk.apis.paths.v0_users_user_id_api_keys import V0UsersUserIdApiKeys
from griffin_python_sdk.apis.paths.v0_users_user_id_memberships import V0UsersUserIdMemberships
from griffin_python_sdk.apis.paths.v0_verifications_verification_id import V0VerificationsVerificationId
from griffin_python_sdk.apis.paths.v0_webhooks_webhook_id import V0WebhooksWebhookId
from griffin_python_sdk.apis.paths.v0_webhooks_webhook_id_actions_activate import V0WebhooksWebhookIdActionsActivate
from griffin_python_sdk.apis.paths.v0_webhooks_webhook_id_actions_deactivate import V0WebhooksWebhookIdActionsDeactivate
from griffin_python_sdk.apis.paths.v0_webhooks_webhook_id_actions_test import V0WebhooksWebhookIdActionsTest
from griffin_python_sdk.apis.paths.v0_workflows_workflow_id import V0WorkflowsWorkflowId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V0_INDEX: V0Index,
        PathValues.V0_PING: V0Ping,
        PathValues.V0_ADMISSIONS_ADMISSIONID: V0AdmissionsAdmissionId,
        PathValues.V0_APIKEYS_APIKEYID: V0ApiKeysApiKeyId,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID: V0BankAccountsBankAccountId,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_ACTIONS_CLOSE: V0BankAccountsBankAccountIdActionsClose,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_ADMISSIONS: V0BankAccountsBankAccountIdAdmissions,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_MEMBERSHIP: V0BankAccountsBankAccountIdMembership,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_MEMBERSHIPUPDATES: V0BankAccountsBankAccountIdMembershipUpdates,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_PAYMENTS: V0BankAccountsBankAccountIdPayments,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_SUBMISSIONS: V0BankAccountsBankAccountIdSubmissions,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_TRANSACTIONS: V0BankAccountsBankAccountIdTransactions,
        PathValues.V0_BANK_TRANSACTIONS_TRANSACTIONID: V0BankTransactionsTransactionId,
        PathValues.V0_COMPANIESHOUSE_COMPANIES_COMPANYNUMBER: V0CompaniesHouseCompaniesCompanyNumber,
        PathValues.V0_EVENTS_EVENTID: V0EventsEventId,
        PathValues.V0_LEGALPERSONS_LEGALPERSONID: V0LegalPersonsLegalPersonId,
        PathValues.V0_LEGALPERSONS_LEGALPERSONID_BANK_PAYEES: V0LegalPersonsLegalPersonIdBankPayees,
        PathValues.V0_LEGALPERSONS_LEGALPERSONID_CLAIMS: V0LegalPersonsLegalPersonIdClaims,
        PathValues.V0_LEGALPERSONS_LEGALPERSONID_DECISIONS: V0LegalPersonsLegalPersonIdDecisions,
        PathValues.V0_LEGALPERSONS_LEGALPERSONID_HISTORY: V0LegalPersonsLegalPersonIdHistory,
        PathValues.V0_LEGALPERSONS_LEGALPERSONID_VERIFICATIONS: V0LegalPersonsLegalPersonIdVerifications,
        PathValues.V0_MEMBERSHIPS_MEMBERSHIPID: V0MembershipsMembershipId,
        PathValues.V0_MEMBERSHIPS_MEMBERSHIPID_ROLES: V0MembershipsMembershipIdRoles,
        PathValues.V0_ONBOARDING_APPLICATIONS_ONBOARDINGAPPLICATIONID: V0OnboardingApplicationsOnboardingApplicationId,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID: V0OrganizationsOrganizationId,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_APIKEYS: V0OrganizationsOrganizationIdApiKeys,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_BANK_ACCOUNTS: V0OrganizationsOrganizationIdBankAccounts,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_EVENTS: V0OrganizationsOrganizationIdEvents,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_INVITATIONS: V0OrganizationsOrganizationIdInvitations,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_LEGALPERSONS: V0OrganizationsOrganizationIdLegalPersons,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_MEMBERSHIPS: V0OrganizationsOrganizationIdMemberships,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_ONBOARDING_APPLICATIONS: V0OrganizationsOrganizationIdOnboardingApplications,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_WEBHOOKS: V0OrganizationsOrganizationIdWebhooks,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_WORKFLOWS: V0OrganizationsOrganizationIdWorkflows,
        PathValues.V0_PAYEES_PAYEEID: V0PayeesPayeeId,
        PathValues.V0_PAYMENTS_PAYMENTID: V0PaymentsPaymentId,
        PathValues.V0_PAYMENTS_PAYMENTID_ADMISSIONS: V0PaymentsPaymentIdAdmissions,
        PathValues.V0_PAYMENTS_PAYMENTID_SUBMISSIONS: V0PaymentsPaymentIdSubmissions,
        PathValues.V0_ROLES: V0Roles,
        PathValues.V0_ROLES_ROLEID: V0RolesRoleId,
        PathValues.V0_SUBMISSIONS_SUBMISSIONID: V0SubmissionsSubmissionId,
        PathValues.V0_USERS_USERID: V0UsersUserId,
        PathValues.V0_USERS_USERID_APIKEYS: V0UsersUserIdApiKeys,
        PathValues.V0_USERS_USERID_MEMBERSHIPS: V0UsersUserIdMemberships,
        PathValues.V0_VERIFICATIONS_VERIFICATIONID: V0VerificationsVerificationId,
        PathValues.V0_WEBHOOKS_WEBHOOKID: V0WebhooksWebhookId,
        PathValues.V0_WEBHOOKS_WEBHOOKID_ACTIONS_ACTIVATE: V0WebhooksWebhookIdActionsActivate,
        PathValues.V0_WEBHOOKS_WEBHOOKID_ACTIONS_DEACTIVATE: V0WebhooksWebhookIdActionsDeactivate,
        PathValues.V0_WEBHOOKS_WEBHOOKID_ACTIONS_TEST: V0WebhooksWebhookIdActionsTest,
        PathValues.V0_WORKFLOWS_WORKFLOWID: V0WorkflowsWorkflowId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V0_INDEX: V0Index,
        PathValues.V0_PING: V0Ping,
        PathValues.V0_ADMISSIONS_ADMISSIONID: V0AdmissionsAdmissionId,
        PathValues.V0_APIKEYS_APIKEYID: V0ApiKeysApiKeyId,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID: V0BankAccountsBankAccountId,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_ACTIONS_CLOSE: V0BankAccountsBankAccountIdActionsClose,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_ADMISSIONS: V0BankAccountsBankAccountIdAdmissions,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_MEMBERSHIP: V0BankAccountsBankAccountIdMembership,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_MEMBERSHIPUPDATES: V0BankAccountsBankAccountIdMembershipUpdates,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_PAYMENTS: V0BankAccountsBankAccountIdPayments,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_SUBMISSIONS: V0BankAccountsBankAccountIdSubmissions,
        PathValues.V0_BANK_ACCOUNTS_BANKACCOUNTID_TRANSACTIONS: V0BankAccountsBankAccountIdTransactions,
        PathValues.V0_BANK_TRANSACTIONS_TRANSACTIONID: V0BankTransactionsTransactionId,
        PathValues.V0_COMPANIESHOUSE_COMPANIES_COMPANYNUMBER: V0CompaniesHouseCompaniesCompanyNumber,
        PathValues.V0_EVENTS_EVENTID: V0EventsEventId,
        PathValues.V0_LEGALPERSONS_LEGALPERSONID: V0LegalPersonsLegalPersonId,
        PathValues.V0_LEGALPERSONS_LEGALPERSONID_BANK_PAYEES: V0LegalPersonsLegalPersonIdBankPayees,
        PathValues.V0_LEGALPERSONS_LEGALPERSONID_CLAIMS: V0LegalPersonsLegalPersonIdClaims,
        PathValues.V0_LEGALPERSONS_LEGALPERSONID_DECISIONS: V0LegalPersonsLegalPersonIdDecisions,
        PathValues.V0_LEGALPERSONS_LEGALPERSONID_HISTORY: V0LegalPersonsLegalPersonIdHistory,
        PathValues.V0_LEGALPERSONS_LEGALPERSONID_VERIFICATIONS: V0LegalPersonsLegalPersonIdVerifications,
        PathValues.V0_MEMBERSHIPS_MEMBERSHIPID: V0MembershipsMembershipId,
        PathValues.V0_MEMBERSHIPS_MEMBERSHIPID_ROLES: V0MembershipsMembershipIdRoles,
        PathValues.V0_ONBOARDING_APPLICATIONS_ONBOARDINGAPPLICATIONID: V0OnboardingApplicationsOnboardingApplicationId,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID: V0OrganizationsOrganizationId,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_APIKEYS: V0OrganizationsOrganizationIdApiKeys,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_BANK_ACCOUNTS: V0OrganizationsOrganizationIdBankAccounts,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_EVENTS: V0OrganizationsOrganizationIdEvents,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_INVITATIONS: V0OrganizationsOrganizationIdInvitations,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_LEGALPERSONS: V0OrganizationsOrganizationIdLegalPersons,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_MEMBERSHIPS: V0OrganizationsOrganizationIdMemberships,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_ONBOARDING_APPLICATIONS: V0OrganizationsOrganizationIdOnboardingApplications,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_WEBHOOKS: V0OrganizationsOrganizationIdWebhooks,
        PathValues.V0_ORGANIZATIONS_ORGANIZATIONID_WORKFLOWS: V0OrganizationsOrganizationIdWorkflows,
        PathValues.V0_PAYEES_PAYEEID: V0PayeesPayeeId,
        PathValues.V0_PAYMENTS_PAYMENTID: V0PaymentsPaymentId,
        PathValues.V0_PAYMENTS_PAYMENTID_ADMISSIONS: V0PaymentsPaymentIdAdmissions,
        PathValues.V0_PAYMENTS_PAYMENTID_SUBMISSIONS: V0PaymentsPaymentIdSubmissions,
        PathValues.V0_ROLES: V0Roles,
        PathValues.V0_ROLES_ROLEID: V0RolesRoleId,
        PathValues.V0_SUBMISSIONS_SUBMISSIONID: V0SubmissionsSubmissionId,
        PathValues.V0_USERS_USERID: V0UsersUserId,
        PathValues.V0_USERS_USERID_APIKEYS: V0UsersUserIdApiKeys,
        PathValues.V0_USERS_USERID_MEMBERSHIPS: V0UsersUserIdMemberships,
        PathValues.V0_VERIFICATIONS_VERIFICATIONID: V0VerificationsVerificationId,
        PathValues.V0_WEBHOOKS_WEBHOOKID: V0WebhooksWebhookId,
        PathValues.V0_WEBHOOKS_WEBHOOKID_ACTIONS_ACTIVATE: V0WebhooksWebhookIdActionsActivate,
        PathValues.V0_WEBHOOKS_WEBHOOKID_ACTIONS_DEACTIVATE: V0WebhooksWebhookIdActionsDeactivate,
        PathValues.V0_WEBHOOKS_WEBHOOKID_ACTIONS_TEST: V0WebhooksWebhookIdActionsTest,
        PathValues.V0_WORKFLOWS_WORKFLOWID: V0WorkflowsWorkflowId,
    }
)
