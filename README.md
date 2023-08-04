# Overview
This repo contains JSON files specifying custom users suitable for testing Plaid integrations on Sandbox, to test scenarios more complex than those provided by the basic `user_good` / `pass_good` Sandbox test user. These files are a starting place for testing -- you can also edit these files before adding them to Sandbox, in order to further customize the test data to your needs. 

# How to use these files
You can add these users to the Sandbox environment via the [Test Users page in the Plaid Dashboard](https://dashboard.plaid.com/developers/sandbox?tab=testUsers). For more details, see [Configuring the custom user account](https://plaid.com/docs/sandbox/user-custom/#configuring-the-custom-user-account) in the Plaid documentation.

Before loading the files into Sandbox, you may need to update the dates in the test files. For example, Income transactions and data should be updated to be within the past 90 days, and transactions for other products should be within the last 2 years. 

If you want to customize these files further, see the [Custom User configuration object schema](https://plaid.com/docs/sandbox/user-custom/#configuration-object-schema) for detailed documentation on available options and fields.

# Contributing
We encourage contributions to this repo. Feel free to submit and add your own test users. Important: never contribute real user data, even if it has been anonymized, unless it is your own, personal data that you have the right to share (i.e., not data belonging to a customer of your service). 
