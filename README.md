> [!WARNING]
> As of September 2026, the functionality in this repo is now offered via the in-Dashboard tool Sandbox Studio instead ([try it in the dashboard](https://dashboard.plaid.com/developers/sandbox) or [read the docs](https://plaid.com/docs/sandbox/studio/)). The users in this repo will still work, but for most use cases, Sandbox Studio is a better UI for creating custom Sandbox users.


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
