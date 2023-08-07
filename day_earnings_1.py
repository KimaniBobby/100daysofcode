import pandas as pd
from datetime import date, timedelta
import sqlite3
import os

def get_date_prompt():
    today = date.today()
    while True:
        date_input = input("Enter the date (0 for input, 1 for yesterday, 2 for today, or 'quit' to exit): ").strip().lower()

        if date_input == "quit":
            return None, None
        elif date_input == "0":
            while True:
                try:
                    date_str = input("Enter the date (YYYY-MM): ")
                    year, month = map(int, date_str.split("-"))
                    input_date = date(year, month, 1)

                    # Ensure the date is not in the future
                    if input_date > today:
                        print("Invalid input. Date cannot be in the future.")
                    else:
                        print(f"Using the date: {input_date}")
                        update_current_month = input("Is this for the current month? (yes/no): ").strip().lower()
                        if update_current_month in ('yes', 'y'):
                            current_date = date.today()
                        else:
                            current_date = None
                        return input_date, current_date
                except ValueError:
                    print("Invalid input. Please enter a valid date in the format 'YYYY-MM'.")
        elif date_input == "1":
            yesterday = today - timedelta(days=1)
            print(f"Using the date: {yesterday}")
            update_current_month = input("Is this for the current month? (yes/no): ").strip().lower()
            if update_current_month in ('yes', 'y'):
                current_date = today
            else:
                current_date = None
            return yesterday, current_date
        elif date_input == "2":
            print(f"Using the date: {today}")
            return today, today  # Allow data entry only up to today's date
        else:
            print("Invalid input. Please enter 0, 1, 2, or 'quit'.")

def get_day_earnings(day_date, current_date):
    while True:
        try:
            day_earning = input(f"Enter earnings for {day_date.strftime('%Y-%m-%d')} (or 'done' to finish input): ")
            if day_earning.lower() == 'done':
                return None
            else:
                earnings = float(day_earning)
                if current_date and day_date > current_date:
                    print("Cannot input earnings for future dates. Please enter earnings only up to today's date.")
                elif earnings == 0:
                    print("Earnings cannot be zero. Please enter a valid non-zero number or 'done' to finish input.")
                else:
                    return earnings
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish input.")

def generate_weekly_report(earnings_table):
    weekly_report = {}

    for (year, month), data in earnings_table.items():
        for day, earnings in data:
            week_number = date(year, month, day).isocalendar()[1]
            key = (year, week_number)
            if key not in weekly_report:
                weekly_report[key] = 0
            weekly_report[key] += earnings

    return weekly_report

def generate_monthly_report(earnings_table):
    monthly_report = {}

    for (year, month), data in earnings_table.items():
        key = (year, month)
        if key not in monthly_report:
            monthly_report[key] = 0
        for day, earnings in data:
            monthly_report[key] += earnings

    return monthly_report

def get_month_name(month_number):
    return date(1900, month_number, 1).strftime('%B')

def main():
    earnings_table = {}  # Initialize the earnings_table dictionary

    # Prompt for the SQLite database file name
    db_file_name = input("Enter the SQLite database file name (without extension): ").strip()
    db_file_path = f"{db_file_name}.db"

    # Establish a connection to the SQLite database
    conn = sqlite3.connect(db_file_path)

    # Create the earnings table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS earnings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        earnings FLOAT NOT NULL
    );
    """
    conn.execute(create_table_query)

    # Read existing data from the database and populate the earnings_table dictionary
    query = "SELECT date, earnings FROM earnings;"
    df_from_db = pd.read_sql_query(query, conn)

    # Create the earnings_table dictionary from the fetched data
    for _, row in df_from_db.iterrows():
        earnings_date = pd.to_datetime(row["date"]).date()
        earnings_value = float(row["earnings"])
        year, month, day = earnings_date.year, earnings_date.month, earnings_date.day
        key = (year, month)
        if key not in earnings_table:
            earnings_table[key] = []
        earnings_table[key].append((day, earnings_value))

    while True:
        date_input, current_date = get_date_prompt()

        if date_input is None:
            break

        if date_input == date.today():
            print("Using current date from the system.")
            current_date = date.today()
        elif date_input == date.today() - timedelta(days=1):
            print("Using yesterday's date.")
            current_date = date.today()
        elif date_input == 0:
            # Handle custom date input (0) and reset date_input
            date_input = None
            while date_input is None:
                try:
                    date_str = input("Enter the date (YYYY-MM): ")
                    year, month = map(int, date_str.split("-"))
                    input_date = date(year, month, 1)

                    # Ensure the date is not in the future
                    if input_date > date.today():
                        print("Invalid input. Date cannot be in the future.")
                    else:
                        print(f"Using the date: {input_date}")
                        update_current_month = input("Is this for the current month? (yes/no): ").strip().lower()
                        if update_current_month in ('yes', 'y'):
                            current_date = date.today()
                        else:
                            current_date = None
                        date_input = input_date
                except ValueError:
                    print("Invalid input. Please enter a valid date in the format 'YYYY-MM'.")

        if date_input == date.today() or date_input == date.today() - timedelta(days=1):
            day_earning = get_day_earnings(date_input, current_date)
            while day_earning is not None:
                day = date_input.day
                year, month = date_input.year, date_input.month
                key = (year, month)
                if key not in earnings_table:
                    earnings_table[key] = []

                # Check if the date already exists in existing data, if so, skip adding
                if key in earnings_table and any(day == existing_day for existing_day, _ in earnings_table[key]):
                    print(f"Earnings for {date_input.strftime('%Y-%m-%d')} are already recorded. No need to append.")
                else:
                    earnings_table[key].append((day, day_earning))

                date_input += timedelta(days=1)
                if current_date and date_input > current_date:
                    print("Cannot input earnings for future dates. Stopping at today's date.")
                    break
                day_earning = get_day_earnings(date_input, current_date)
        else:
            try:
                month_end = date(date_input.year, date_input.month, 1) + timedelta(days=31)
                while date_input < month_end:
                    if current_date and date_input > current_date:
                        print("Cannot input earnings for future dates. Stopping at today's date.")
                        break

                    if date_input not in earnings_table:
                        day_earning = get_day_earnings(date_input, current_date)
                        if day_earning is not None:
                            day = date_input.day
                            year, month = date_input.year, date_input.month
                            key = (year, month)
                            if key not in earnings_table:
                                earnings_table[key] = []

                            # Check if the date already exists in existing data, if so, skip adding
                            if key in earnings_table and any(day == existing_day for existing_day, _ in earnings_table[key]):
                                print(f"Earnings for {date_input.strftime('%Y-%m-%d')} are already recorded. No need to append.")
                            else:
                                earnings_table[key].append((day, day_earning))

                    date_input += timedelta(days=1)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    df = pd.DataFrame(
        [(f"{year:04d}-{month:02d}-{day:02d}", earnings) for (year, month), data in earnings_table.items() for day, earnings in data],
        columns=["Date", "Earnings"]
    )

    df.sort_values(by="Date", inplace=True)

    print("\nEarnings Table:")
    print(df)

    # Export the updated data to the database (Append to the existing data)
    df.to_sql("earnings", conn, if_exists="append", index=False)

    # Generate weekly report
    query = """
        SELECT strftime('%Y', date) as year, strftime('%W', date) as week, SUM(earnings) as earnings
        FROM earnings GROUP BY year, week;
    """
    df_weekly_report = pd.read_sql_query(query, conn)

    print("\nWeekly Report:")
    print(df_weekly_report)

    # Generate monthly report
    query = """
        SELECT strftime('%Y', date) as year, strftime('%m', date) as month, SUM(earnings) as earnings
        FROM earnings GROUP BY year, month;
    """
    df_monthly_report = pd.read_sql_query(query, conn)
    conn.close()

    print("\nMonthly Report:")
    print(df_monthly_report)

if __name__ == "__main__":
    main()
