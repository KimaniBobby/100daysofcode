import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import date, timedelta

class EarningsTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Earnings Tracker App")

        self.earnings_table = {}
        self.df = None
        self.df_weekly = None
        self.df_monthly = None

        self.create_widgets()

    def create_widgets(self):
        # Create date input frame
        date_frame = tk.Frame(self.root)
        date_frame.pack(padx=10, pady=10)

        self.date_input = tk.IntVar()
        self.date_input.set(2)  # Default value for Today

        self.radio_today = tk.Radiobutton(date_frame, text="Today", variable=self.date_input, value=2, command=self.get_date_prompt)
        self.radio_today.pack(side=tk.LEFT)

        self.radio_yesterday = tk.Radiobutton(date_frame, text="Yesterday", variable=self.date_input, value=1, command=self.get_date_prompt)
        self.radio_yesterday.pack(side=tk.LEFT)

        self.radio_custom = tk.Radiobutton(date_frame, text="Custom Date (YYYY-MM)", variable=self.date_input, value=0, command=self.get_date_prompt)
        self.radio_custom.pack(side=tk.LEFT)

        self.date_entry = tk.Entry(date_frame, state=tk.DISABLED)
        self.date_entry.pack(side=tk.LEFT)

        # Create earnings input frame
        self.earnings_entry_frame = tk.Frame(self.root)
        self.earnings_entry_frame.pack(padx=10, pady=10)

        self.earnings_prompt_label = tk.Label(self.earnings_entry_frame, text="Enter earnings:")
        self.earnings_prompt_label.pack(side=tk.LEFT)

        self.earnings_input = tk.StringVar()
        self.earnings_entry = tk.Entry(self.earnings_entry_frame, textvariable=self.earnings_input)
        self.earnings_entry.pack(side=tk.LEFT)

        self.earnings_submit_button = tk.Button(self.earnings_entry_frame, text="Submit", command=self.get_day_earnings)
        self.earnings_submit_button.pack(side=tk.LEFT)

        # Create earnings table frame
        table_frame = tk.Frame(self.root)
        table_frame.pack(padx=10, pady=10)

        self.earnings_table_label = tk.Label(table_frame, text="Earnings Table:")
        self.earnings_table_label.pack()

        self.earnings_table_text = tk.Text(table_frame, height=10, width=40)
        self.earnings_table_text.pack()

        # Create export button
        export_button = tk.Button(self.root, text="Export to Excel", command=self.export_to_excel)
        export_button.pack(pady=10)

    def get_date_prompt(self):
        date_input = self.date_input.get()

        if date_input == 0:  # Custom Date option selected
            self.date_entry.config(state=tk.NORMAL)
            self.date_entry.delete(0, tk.END)
            self.date_entry.focus()
        else:  # Today or Yesterday option selected
            self.date_entry.delete(0, tk.END)
            self.date_entry.config(state=tk.DISABLED)
            date_selected = date.today() if date_input == 2 else date.today() - timedelta(days=1)
            self.update_earnings_table(date_selected)

    def get_day_earnings(self):
        if self.date_input.get() == 0:
            # If Custom Date option is selected, get the date from the entry box
            try:
                date_str = self.date_entry.get().strip()
                year, month = map(int, date_str.split("-"))
                date_input = date(year, month, 1)

                # Ensure the date is not in the future
                if date_input > date.today():
                    messagebox.showerror("Invalid input", "Date cannot be in the future.")
                    return
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid date in the format 'YYYY-MM'.")
                return
        else:
            # Today or Yesterday option selected
            date_input = date.today() if self.date_input.get() == 2 else date.today() - timedelta(days=1)

        if date_input > date.today():
            messagebox.showinfo("Info", "Cannot input earnings for future dates. Stopping at today's date.")
            return

        day_earning = self.earnings_input.get().strip()
        if day_earning.lower() == 'done':
            self.get_day_earnings_done(date_input)
        else:
            try:
                day_earning = float(day_earning)
                day = date_input.day
                year, month = date_input.year, date_input.month
                key = (year, month)
                if key not in self.earnings_table:
                    self.earnings_table[key] = []
                self.earnings_table[key].append((day, day_earning))
                self.earnings_input.set("")
                self.update_earnings_table(date_input + timedelta(days=1))
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid number or 'done' to finish input.")

    def get_day_earnings_done(self, date_input):
        self.update_earnings_table(date_input + timedelta(days=1))

    def update_earnings_table(self, date_input):
        if date_input == date.today() or date_input == date.today() - timedelta(days=1):
            while True:
                if date_input > date.today():
                    messagebox.showinfo("Info", "Cannot input earnings for future dates. Stopping at today's date.")
                    break
                day_earning = self.get_day_earnings_prompt(date_input)
                if day_earning is not None:
                    day = date_input.day
                    year, month = date_input.year, date_input.month
                    key = (year, month)
                    if key not in self.earnings_table:
                        self.earnings_table[key] = []
                    self.earnings_table[key].append((day, day_earning))
                else:
                    break
                date_input += timedelta(days=1)
        else:
            try:
                month_end = date(date_input.year, date_input.month, 1) + timedelta(days=31)
                current_date = date_input
                while current_date < month_end:
                    day_earning = self.get_day_earnings_prompt(current_date)
                    if day_earning is not None:
                        day = current_date.day
                        year, month = current_date.year, current_date.month
                        key = (year, month)
                        if key not in self.earnings_table:
                            self.earnings_table[key] = []
                        self.earnings_table[key].append((day, day_earning))
                    else:
                        break
                    current_date += timedelta(days=1)
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid number.")

        # Convert the dictionary to a pandas DataFrame for better display and sorting
        self.df = pd.DataFrame(
            [(f"{year:04d}-{month:02d}-{day:02d}", earnings) for (year, month), data in self.earnings_table.items() for day, earnings in data],
            columns=["Date", "Earnings"]
        )

        # Sort the DataFrame by the Date column
        self.df.sort_values(by="Date", inplace=True)

        # Display the earnings table in the GUI
        self.earnings_table_text.delete(1.0, tk.END)
        self.earnings_table_text.insert(tk.END, self.df.to_string(index=False))

        # Calculate and display the number of days
        num_days = len(self.df)
        self.earnings_table_label.config(text=f"Earnings Table (Total Days: {num_days})")

        # Generate weekly report and display it
        self.generate_weekly_report()
        self.df_weekly = pd.DataFrame(
            [(f"{year:04d}-Week{week:02d}", earnings) for (year, week), earnings in self.weekly_report.items()],
            columns=["Week", "Earnings"]
        )
        self.df_weekly.sort_values(by="Week", inplace=True)

        # Generate monthly report and display it
        self.generate_monthly_report()
        self.df_monthly = pd.DataFrame(
            [(f"{year:04d}-{self.get_month_name(month)}", earnings) for (year, month), earnings in self.monthly_report.items()],
            columns=["Month", "Earnings"]
        )
        self.df_monthly.sort_values(by="Month", inplace=True)

    def get_day_earnings_prompt(self, day_date):
        self.earnings_input.set("")  # Clear the previous input
        self.earnings_prompt_label.config(text=f"Enter earnings for {day_date.strftime('%Y-%m-%d')}:")
        self.earnings_entry_frame.pack()

    def generate_weekly_report(self):
        # Generate weekly report and display it
        self.weekly_report = {}
        for (year, month), data in self.earnings_table.items():
            for day, earnings in data:
                week_number = date(year, month, day).isocalendar()[1]
                key = (year, week_number)
                if key not in self.weekly_report:
                    self.weekly_report[key] = 0
                self.weekly_report[key] += earnings

    def generate_monthly_report(self):
        # Generate monthly report and display it
        self.monthly_report = {}
        for (year, month), data in self.earnings_table.items():
            key = (year, month)
            if key not in self.monthly_report:
                self.monthly_report[key] = 0
            for day, earnings in data:
                self.monthly_report[key] += earnings

    def get_month_name(self, month_number):
        return date(1900, month_number, 1).strftime('%B')

    def export_to_excel(self):
        if not self.df:
            messagebox.showwarning("No Data", "No data available to export.")
            return

        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if not filename:
            return

        try:
            self.generate_weekly_report()
            self.generate_monthly_report()

            with pd.ExcelWriter(filename) as writer:
                self.df.to_excel(writer, sheet_name="Daily Earnings", index=False)
                self.df_weekly.to_excel(writer, sheet_name="Weekly Earnings", index=False)
                self.df_monthly.to_excel(writer, sheet_name="Monthly Earnings", index=False)

            messagebox.showinfo("Export Success", f"Data successfully exported to '{filename}'.")
        except Exception as e:
            messagebox.showerror("Export Error", f"An error occurred while exporting data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EarningsTrackerApp(root)
    root.mainloop()
