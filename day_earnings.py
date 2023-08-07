import pandas as pd
from datetime import date, timedelta

def get_date_prompt(): #Asks the user for a date input, which can be a specific date, yesterday, today, or 'quit' to exit the application.
    today = date.today()
    while True:
        date_input = input("Enter the date (0 for input, 1 for yesterday, 2 for today, or 'quit' to exit): ").strip().lower()

        if date_input == "quit":
            return None
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
                        return input_date
                except ValueError:
                    print("Invalid input. Please enter a valid date in the format 'YYYY-MM'.")

        elif date_input == "1":
            yesterday = today - timedelta(days=1)
            return yesterday
        elif date_input == "2":
            return today
        else:
            print("Invalid input. Please enter 0, 1, 2, or 'quit'.")

def get_day_earnings(day_date): # Asks the user for earnings for a specific date.
    while True:
        try:
            day_earning = input(f"Enter earnings for {day_date.strftime('%Y-%m-%d')} (or 'done' to finish input): ")
            if day_earning.lower() == 'done':
                return None
            else:
                return float(day_earning)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish input.")

def generate_weekly_report(earnings_table): # Calculates the total earnings for each week based on the input data.
    weekly_report = {}

    for (year, month), data in earnings_table.items():
        for day, earnings in data:
            week_number = date(year, month, day).isocalendar()[1]
            key = (year, week_number)
            if key not in weekly_report:
                weekly_report[key] = 0
            weekly_report[key] += earnings

    return weekly_report

def generate_monthly_report(earnings_table): # Calculates the total earnings for each month based on the input data.
    monthly_report = {}

    for (year, month), data in earnings_table.items():
        key = (year, month)
        if key not in monthly_report:
            monthly_report[key] = 0
        for day, earnings in data:
            monthly_report[key] += earnings

    return monthly_report

def get_month_name(month_number): # Returns the name of the month given its number.
    return date(1900, month_number, 1).strftime('%B')

def export_to_excel(df): # Asks the user if they want to export the data to an Excel file and does so if requested.
    choice = input("Do you want to export the data to an Excel file? (yes/no): ").strip().lower()
    if choice in ('yes', 'y'):
        filename = input("Enter the Excel file name (e.g., 'earnings'): ").strip()
        filename += ".xlsx"  # Append the .xlsx extension to the filename
        df.to_excel(filename, index=False)
        print(f"Data successfully exported to '{filename}'.")
    else:
        print("Exiting the application.")

def main():
    earnings_table = {}  # Initialize the earnings_table dictionary

    while True:
        date_input = get_date_prompt()

        if date_input is None:
            break

        if date_input == date.today():
            print("Using current date from the system.")
        else:
            print(f"Using the date: {date_input}")

        if date_input == date.today() or date_input == date.today() - timedelta(days=1):
            # For today or yesterday, ask for daily earnings until today's date
            day_earning = get_day_earnings(date_input)
            while day_earning is not None:
                day = date_input.day
                year, month = date_input.year, date_input.month
                key = (year, month)
                if key not in earnings_table:
                    earnings_table[key] = []
                earnings_table[key].append((day, day_earning))
                date_input += timedelta(days=1)
                if date_input > date.today():
                    print("Cannot input earnings for future dates. Stopping at today's date.")
                    break
                day_earning = get_day_earnings(date_input)
        else:
            # For past months, ask for day-to-day earnings until the end of the month
            try:
                month_end = date(date_input.year, date_input.month, 1) + timedelta(days=31)
                current_date = date_input
                while current_date < month_end:
                    day_earning = get_day_earnings(current_date)
                    if day_earning is not None:
                        day = current_date.day
                        year, month = current_date.year, current_date.month
                        key = (year, month)
                        if key not in earnings_table:
                            earnings_table[key] = []
                        earnings_table[key].append((day, day_earning))
                    current_date += timedelta(days=1)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Convert the dictionary to a pandas DataFrame for better display and sorting
    df = pd.DataFrame(
        [(f"{year:04d}-{month:02d}-{day:02d}", earnings) for (year, month), data in earnings_table.items() for day, earnings in data],
        columns=["Date", "Earnings"]
    )

    # Sort the DataFrame by the Date column
    df.sort_values(by="Date", inplace=True)

    print("\nEarnings Table:")
    print(df)

    # Generate weekly report and display it
    weekly_report = generate_weekly_report(earnings_table)
    df_weekly = pd.DataFrame(
        [(f"{year:04d}-Week{week:02d}", earnings) for (year, week), earnings in weekly_report.items()],
        columns=["Week", "Earnings"]
    )

    print("\nWeekly Report:")
    print(df_weekly)

    # Generate monthly report and display it
    monthly_report = generate_monthly_report(earnings_table)
    df_monthly = pd.DataFrame(
        [(f"{year:04d}-{get_month_name(month)}", earnings) for (year, month), earnings in monthly_report.items()],
        columns=["Month", "Earnings"]
    )

    print("\nMonthly Report:")
    print(df_monthly)

    export_to_excel(df)

if __name__ == "__main__":
    main()
