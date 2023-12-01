"""
A script that updates the JSON data for our sandbox assets user so that their 
most recent transactions are dated to today's date and work backwards from there.

Currently hard-coded to just look at the assets users, but assuming 
this works, we can look at making it more general purpose
"""

import json
from datetime import datetime


# Function to calculate the new date
def scale_date(old_date_str, base_date, target_date):
    """
    Given a date string, a base date, and a target date, scale the date string
    to a new date that is the same distance from the target date as the base date
    """
    old_date = datetime.strptime(old_date_str, "%Y-%m-%d")
    delta = base_date - old_date
    new_date = target_date - delta
    return new_date.strftime("%Y-%m-%d")


def find_most_recent_date(original_data):
    """
    Given the JSON data, find the most recent date from the list of transactions
    """
    most_recent_date = datetime.min
    for account in original_data.get("override_accounts", []):
        for transaction in account.get("transactions", []):
            for date_field in ["date_posted", "date_transacted"]:
                date_str = transaction.get(date_field)
                if date_str:
                    date = datetime.strptime(date_str, "%Y-%m-%d")
                    if date > most_recent_date:
                        most_recent_date = date
    return most_recent_date


sandbox_user_files = ["assets/assets_custom_user.json",
                      "assets/assets_custom_user2.json",
                      "income/bank_income_custom_user_5_income_sources.json",
                      "income/bank_income_custom_user_6+_employers_in_90_days.json",
                      "income/bank_income_custom_user_random_income_over_90_days.json",
                      "income/payrollUser.json",
                      "income/selfEmployedGiguser.json",
                      "income/SMBCustomUser.json",
                      "income/SSAUser.json",
                      "income/transactions+inflow_custom_user.json",
                      "income/welderTestUser.json",
                      "transactions/business_account.json",
                      "transactions/transactions_checking+savings_custom_user.json",

                      ]
# Iterate through each filename in the array
for user_file in sandbox_user_files:

    try:
        with open(user_file, "r", encoding="utf-8") as file:
            json_data = json.load(file)

        # Determine the most recent date from the JSON data
        most_recent_date = find_most_recent_date(json_data)
        today_date = datetime.now()

        # Iterate over each account and transaction to update the dates
        # Using .get() to avoid KeyError
        for account in json_data.get("override_accounts", []):
            # Using .get() to avoid KeyError
            transactions = account.get("transactions")
            if transactions:  # Check if transactions is not None or empty
                for transaction in transactions:
                    if "date_posted" in transaction:
                        transaction["date_posted"] = scale_date(
                            transaction["date_posted"], most_recent_date, today_date
                        )
                    if "date_transacted" in transaction:
                        transaction["date_transacted"] = scale_date(
                            transaction["date_transacted"], most_recent_date, today_date
                        )

        # Write the updated JSON data to a file
        with open(user_file, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=4)

    except FileNotFoundError:
        print(f"File {user_file} not found")
        continue
    except json.JSONDecodeError:
        print(f"File {user_file} is not valid JSON")
        continue
    except KeyError:
        print(f"File {user_file} is missing a required key")
        continue
    except Exception as e:
        print(f"An error occurred while processing {user_file}: {e}")
        continue
