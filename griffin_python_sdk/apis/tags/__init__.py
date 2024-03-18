# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from griffin_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PAYMENTS = "Payments"
    WEBHOOKS = "Webhooks"
    BANK_ACCOUNTS = "Bank accounts"
    API_KEYS = "API keys"
    LEGAL_PERSONS = "Legal persons"
    PAYEES = "Payees"
    MEMBERSHIPS = "Memberships"
    ROLES = "Roles"
    VERIFICATIONS = "Verifications"
    CLAIMS = "Claims"
    WORKFLOWS = "Workflows"
    RELIANCE_ONBOARDING = "Reliance onboarding"
    TRANSACTIONS = "Transactions"
    POOLED_ACCOUNT_MEMBERSHIP = "Pooled account membership"
    EVENTS = "Events"
    DECISIONS = "Decisions"
    ORGANIZATIONS = "Organizations"
    USERS = "Users"
    INVITATIONS = "Invitations"
    NAVIGATION = "Navigation"
    CONNECTIVITY = "Connectivity"
    COMPANIES_HOUSE = "Companies House"
    LEGAL_PERSON_HISTORY = "Legal person history"
    GETTING_STARTED = "Getting started"
    CUSTOMER_VERIFICATIONS = "Customer verifications"
