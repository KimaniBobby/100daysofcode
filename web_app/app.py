# app.py

from flask import Flask, render_template, request, jsonify
from datetime import date
import database  # Module to handle database operations
import helper_functions  # Module with helper functions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_earning', methods=['POST'])
def save_earning():
    try:
        date_input = request.form['date']
        earnings = float(request.form['earnings'])

        # Validate date format (YYYY-MM)
        if len(date_input) != 7 or date_input[4] != '-' or not date_input[:4].isdigit() or not date_input[5:].isdigit():
            return jsonify({'error': 'Invalid date format. Please use YYYY-MM.'}), 400

        # Validate earnings value
        if earnings <= 0:
            return jsonify({'error': 'Earnings must be a positive non-zero number.'}), 400

        # Save data to the database
        database.save_earning_to_db(date_input, earnings)

        return jsonify({'message': 'Earnings data saved successfully.'}), 200

    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide a valid date and earnings value.'}), 400

@app.route('/get_earnings_table')
def get_earnings_table():
    earnings_table = database.get_earnings_table()
    return jsonify(earnings_table), 200

@app.route('/generate_reports')
def generate_reports():
    try:
        earnings_table = database.get_earnings_table()
        weekly_report = helper_functions.generate_weekly_report(earnings_table)
        monthly_report = helper_functions.generate_monthly_report(earnings_table)

        return jsonify({
            'weekly_report': weekly_report,
            'monthly_report': monthly_report
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    database.create_tables()  # Create database tables if they don't exist
    app.run(debug=True)
