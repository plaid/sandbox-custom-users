# Overview

This repo contains JSON files specifying custom users suitable for testing Plaid integrations on Sandbox, to test complex or custom scenarios. These files are a starting place for testing -- you can also edit these files before adding them to Sandbox, in order to further customize the test data to your needs.

> [!TIP]
> Also check out Plaid's selection of [pre-populated Sandbox test users](https://plaid.com/docs/sandbox/test-credentials/). These users are easier to work with than custom Sandbox users and allow you to test some common scenarios that custom Sandbox users don't support, like dynamically updating data (Transactions), or micro-deposit flows (Auth).

# How to use these files

You can add these users to the Sandbox environment via the [Test Users page in the Plaid Dashboard](https://dashboard.plaid.com/developers/sandbox?tab=testUsers). For more details, see [Configuring the custom user account](https://plaid.com/docs/sandbox/user-custom/#configuring-the-custom-user-account) in the Plaid documentation.

The dates in these test files are automatically updated daily such that the most recent date will be set to today, and then all other dates are adjusted proportionately. After loading these files into Sandbox, you may need to occasionally updates them so that Income transactions and data are within the past 90 days, and transactions for other products are within the last 2 years. You can do this by re-fetching these files from Github, or running the `update_dates.py` script.

If you want to customize these files further, see the [Custom User configuration object schema](https://plaid.com/docs/sandbox/user-custom/#configuration-object-schema) for detailed documentation on available options and fields.

# Contributing

We encourage contributions to this repo. Feel free to submit and add your own test users. Important: never contribute real user data, even if it has been anonymized, unless it is your own, personal data that you have the right to share (i.e., not data belonging to a customer of your service).
