# Overview

This repo contains JSON files specifying custom users suitable for testing Plaid integrations on Sandbox, to test complex or custom scenarios. These files are a starting place for testing -- you can also edit these files before adding them to Sandbox, in order to further customize the test data to your needs.

> [!TIP]
> Also check out Plaid's selection of [pre-populated Sandbox test users](https://plaid.com/docs/sandbox/test-credentials/). These users are easier to work with than custom Sandbox users and allow you to test some common scenarios that custom Sandbox users don't support, like dynamically updating data (Transactions), or micro-deposit flows (Auth).

# How to use these files

You can add these users to the Sandbox environment via the [Test Users page in the Plaid Dashboard](https://dashboard.plaid.com/developers/sandbox?tab=testUsers). For more details, see [Configuring the custom user account](https://plaid.com/docs/sandbox/user-custom/#configuring-the-custom-user-account) in the Plaid documentation.

## Using these files without the Dashboard

You don't need the Dashboard to use a custom user file -- you can create an Item directly via the API, which is useful for scripting, CI, or handing a file like these to an AI-assisted coding tool to set up test data programmatically. Call [`/sandbox/public_token/create`](https://plaid.com/docs/api/sandbox/#sandboxpublic_tokencreate) with:

- `options.override_username` set to the literal string `user_custom`
- `options.override_password` set to the **entire contents of the custom user file, JSON-stringified into a single string** (not passed as a nested JSON object)

For example, in Python:

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

Then exchange the returned `public_token` via [`/item/public_token/exchange`](https://plaid.com/docs/api/items/#itempublic_tokenexchange) for an `access_token` as usual. Use a non-OAuth institution, such as `ins_109508` (First Platypus Bank) -- see the warning below.

The dates in these test files are automatically updated daily such that the most recent date will be set to today, and then all other dates are adjusted proportionately. After loading these files into Sandbox, you may need to occasionally update them so that Income transactions and data are within the past 90 days, and transactions for other products are within the last 2 years. You can do this by re-fetching these files from Github, or running the `update_dates.py` script.

If you want to customize these files further, see the [Custom User configuration object schema](https://plaid.com/docs/sandbox/user-custom/#configuration-object-schema) for detailed documentation on available options and fields.

> [!WARNING]
> At OAuth institutions, certain less frequently used customized fields may be overridden by the default values after the Link flow has completed. If this occurs, retry the configuration using a non-OAuth institution.

# Contributing

We encourage contributions to this repo. Feel free to submit and add your own test users. Important: never contribute real user data, even if it has been anonymized, unless it is your own, personal data that you have the right to share (i.e., not data belonging to a customer of your service).
