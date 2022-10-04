# Overview
This repo contains JSON files specifying custom users suitable for testing Plaid integrations on Sandbox, to test scenarios more complex than those provided by the basic `user_good` Sandbox test user. These files are a starting place for testing -- you can also edit these files before adding them to Sandbox, in order to further customize the test data to your needs. 

# How to use these files
To learn how to add this data to the Sandbox environment, see [Configuring the custom user account](https://plaid.com/docs/sandbox/user-custom/#configuring-the-custom-user-account) in the Plaid documentation.

Before loading the files into Sandbox, you may need to update the dates in the test files. For example, Income transactions and data should be updated to be within the past 90 days, and transactions for other products should be within the last 2 years. 
