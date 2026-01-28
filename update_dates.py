"""
A script that updates the JSON data for our sandbox assets user so that their 
most recent transactions are dated to today's date and work backwards from there.

Currently hard-coded to just look at the assets users, but assuming 
this works, we can look at making it more general purpose
"""

import json
from datetime import datetime


DATE_KEYS_TO_MODIFY = [
    "date_posted",
    "date_transacted",
    "start_date",
    "end_date",
    "pay_day",
    "institution_price_as_of",
    "date",
]

# Function to calculate the new date


def scale_date(old_date_str, base_date, target_date):
    """
    Given a date string, a base date, and a target date, scale the date string
    to a new date that is the same distance from the target date as the base date
    """
    try:
        old_date = datetime.strptime(old_date_str, "%Y-%m-%d")
        delta = base_date - old_date
        new_date = target_date - delta
        return new_date.strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        print(f"Yikes! Found a bad date string: {old_date_str}")
        return old_date_str


def find_most_recent_date(data, most_recent_date=datetime.min):
    """
    Given the JSON data, find the most recent date from any part of the structure.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            # Add other date keys if needed
            if key in DATE_KEYS_TO_MODIFY:
                try:
                    date = datetime.strptime(value, "%Y-%m-%d")
                    if date > most_recent_date:
                        most_recent_date = date
                except (ValueError, TypeError):
                    print(f"Yikes! Found a bad date string: {value} in {key}")
                    # In case the value is not a valid date string or is not a string
                    pass
            else:
                most_recent_date = find_most_recent_date(value, most_recent_date)
    elif isinstance(data, list):
        for item in data:
            most_recent_date = find_most_recent_date(item, most_recent_date)

    return most_recent_date


sandbox_user_files = [
    "assets/assets_credit_categories.json",
    "assets/assets_custom_user.json",
    "assets/assets_custom_user2.json",
    "income/bank_income_basic.json",
    "income/bank_income_custom_user_5_income_sources.json",
    "income/bank_income_custom_user_6+_employers_in_90_days.json",
    "income/bank_income_custom_user_random_income_over_90_days.json",
    "income/payroll_income_custom_user.json",
    "income/selfEmployedGiguser.json",
    "income/SMBCustomUser.json",
    "income/SSAuser.json",
    "income/transactions+inflow_custom_user.json",
    "income/document_income/paystub_and_risk_signals.json",
    "income/welderTestUser.json",
    "investments/brokerage_custom_user.json",
    "transactions/business_account.json",
    "transactions/transactions_checking+savings_custom_user.json",
    "user_rich.json",
    "user_poor.json",
]


def update_dates(data, most_recent_date, today_date):
    if isinstance(data, dict):
        for key, value in data.items():
            # Add other date keys if needed
            if key in DATE_KEYS_TO_MODIFY:
                data[key] = scale_date(value, most_recent_date, today_date)
            else:
                update_dates(value, most_recent_date, today_date)
    elif isinstance(data, list):
        for item in data:
            update_dates(item, most_recent_date, today_date)


# Iterate through each filename in the array
for user_file in sandbox_user_files:
    try:
        with open(user_file, "r", encoding="utf-8") as file:
            json_data = json.load(file)

        most_recent_date = find_most_recent_date(json_data)
        today_date = datetime.now()

        # Update all dates in the JSON data
        update_dates(json_data, most_recent_date, today_date)

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
