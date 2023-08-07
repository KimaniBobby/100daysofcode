# helper_functions.py

from datetime import datetime, timedelta

def generate_weekly_report(earnings_table):
    weekly_report = {}

    for row in earnings_table:
        date_input = datetime.strptime(row['date'], '%Y-%m-%d')
        week_number = date_input.isocalendar()[1]
        year = date_input.year
        key = (year, week_number)
        earnings = float(row['earnings'])

        if key not in weekly_report:
            weekly_report[key] = 0

        weekly_report[key] += earnings

    return [{'year': year, 'week': week, 'earnings': earnings} for (year, week), earnings in weekly_report.items()]

def generate_monthly_report(earnings_table):
    monthly_report = {}

    for row in earnings_table:
        date_input = datetime.strptime(row['date'], '%Y-%m-%d')
        year, month = date_input.year, date_input.month
        key = (year, month)
        earnings = float(row['earnings'])

        if key not in monthly_report:
            monthly_report[key] = 0

        monthly_report[key] += earnings

    return [{'year': year, 'month': month, 'earnings': earnings} for (year, month), earnings in monthly_report.items()]
