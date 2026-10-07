> [!NOTE]
> This repo stays up for developers who already build from these files, and the files keep working. For new work, use Sandbox Studio in the Dashboard ([open it](https://dashboard.plaid.com/developers/sandbox) or [read the docs](https://plaid.com/docs/sandbox/studio/)): every Item config in this repo is offered there as a template in the Create user dropdown, and the table below maps each file to its template. The six files under `income/document_income` are upload fixtures for Document Income rather than Item configs, so they live only here.

| File in this repo | Sandbox Studio template |
| --- | --- |
| `blank_template_custom_sandbox_user.json` | No template |
| `assets/assets_custom_user.json` | John Smith Assets (`custom_assets`) |
| `assets/assets_custom_user2.json` | John Smith Assets Plus (`custom_assets_multi_account`) |
| `assets/assets_credit_categories.json` | John Smith Categories (`custom_assets_credit_categories`) |
| `auth/auth_custom_user.json` | John Smith (`custom_auth`) |
| `auth/auth_canada_custom_user.json` | John Smith CA (`custom_auth_canada`) |
| `auth/auth_ireland_custom_user.json` | John Smith IE (`custom_auth_ireland`) |
| `auth/auth_uk_custom_user.json` | John Smith UK (`custom_auth_uk`) |
| `identity/identity_multiple_names_custom_user.json` | John Smith and Jane Doe (`custom_identity_multiple_names`) |
| `identity/joint_owner_identity_custom_user.json` | Jane Alana Smith (`custom_identity_joint_owner`) |
| `identity/leslie_knope_financial_account_matching.json` | Leslie Knope (`custom_financial_account_matching`) |
| `income/bank_income_basic.json` | George Smith (`custom_bank_income`) |
| `income/bank_income_custom_user_5_income_sources.json` | John Smith Five Sources (`custom_bank_income_five_sources`) |
| `income/bank_income_custom_user_6+_employers_in_90_days.json` | John Smith Six Employers (`custom_bank_income_many_employers`) |
| `income/bank_income_custom_user_random_income_over_90_days.json` | John Smith Irregular (`custom_bank_income_irregular`) |
| `income/payroll_income_custom_user.json` | Chip Hazard (`custom_income_payroll`) |
| `income/SMBCustomUser.json` | John Smith SMB (`custom_income_smb`) |
| `income/selfEmployedGiguser.json` | John Smith Gig (`custom_income_self_employed`) |
| `income/SSAuser.json` | John Smith SSA (`custom_income_social_security`) |
| `income/transactions+inflow_custom_user.json` | John Smith Inflow (`custom_income_inflow_model`) |
| `income/welderTestUser.json` | George Smith Welder (`custom_income_welder`) |
| `investments/brokerage_custom_user.json` | John Smith Cash (`custom_investments_brokerage`) |
| `liabilities/credit_card_custom_user.json` | John Smith Card (`custom_liabilities_credit_card`) |
| `liabilities/student_loan_custom_user.json` | Brady Williams (`custom_liabilities_student`) |
| `transactions/business_account.json` | Hooli LLC (`custom_transactions_business`) |
| `transactions/transactions_checking+savings_custom_user.json` | John Smith Savings (`custom_transactions_checking_savings`) |

# Overview

This repo contains JSON files specifying custom users suitable for testing Plaid integrations on Sandbox, to test complex or custom scenarios. These files are a starting place for testing -- you can also edit these files before adding them to Sandbox, in order to further customize the test data to your needs.

> [!TIP]
> Also check out Plaid's selection of [pre-populated Sandbox test users](https://plaid.com/docs/sandbox/test-credentials/). These users allow you to test some common scenarios that custom Sandbox users don't support, like dynamically updating data (Transactions), or micro-deposit flows (Auth).

# How to use these files

You can add these users to the Sandbox environment via the [Test Users page in the Plaid Dashboard](https://dashboard.plaid.com/developers/sandbox?tab=testUsers). For more details, see [Configuring the custom user account](https://plaid.com/docs/sandbox/user-custom/#configuring-the-custom-user-account) in the Plaid documentation.

To use these test users without the Dashboard, directly via the API, call [`/sandbox/public_token/create`](https://plaid.com/docs/api/sandbox/#sandboxpublic_tokencreate) with:

- `options.override_username` set to the literal string `user_custom`
- `options.override_password` set to the entire contents of the custom user file, JSON-stringified into a single string

For example:

```python
import json
import requests

with open("liabilities/credit_card_custom_user.json") as f:
    custom_user_config = json.load(f)

resp = requests.post(
    "https://sandbox.plaid.com/sandbox/public_token/create",
    json={
        "client_id": PLAID_CLIENT_ID,
        "secret": PLAID_SECRET,
        "institution_id": "ins_109508",
        "initial_products": ["liabilities"],
        "options": {
            "override_username": "user_custom",
            "override_password": json.dumps(custom_user_config),
        },
    },
)
public_token = resp.json()["public_token"]
```

Every config in this repo sets `roll_dates_forward: true`. When you create a Sandbox Item from one, Plaid shifts every date in the config so the most recent activity (transactions, pay days, holding price dates, loan payments) lands on the day the Item is created, keeping the spacing between dates. The files no longer need their dates rewritten to stay inside the Transactions and Income windows. Remove the flag if you want the dates used exactly as written. See [Customize Sandbox test users](https://plaid.com/docs/sandbox/user-custom/) for the field reference.

If you want to customize these files further, see the [Custom User configuration object schema](https://plaid.com/docs/sandbox/user-custom/#configuration-object-schema) for detailed documentation on available options and fields.

> [!WARNING]
> At OAuth institutions, certain less frequently used customized fields may be overridden by the default values after the Link flow has completed. If this occurs, retry the configuration using a non-OAuth institution.

# Contributing

We encourage contributions to this repo. Feel free to submit and add your own test users. Important: never contribute real user data, even if it has been anonymized, unless it is your own, personal data that you have the right to share (i.e., not data belonging to a customer of your service).
