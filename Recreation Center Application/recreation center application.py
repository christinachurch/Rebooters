import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

landEquipment = {
'2 Person Tent' : 15,
'4 Person Tent' : 20,
'6 Person Tent' : 25,
'8 Person Tent' : 30,
'Sleeping Bag': 8,
'Sleeping Pad': 5,
'Backpack': 10,
'Medium Stuff Sack': 3,
'Large Stuff Sack': 5,
'2 Burner Stove': 10,
'Cook Pot Set': 5,
'Lantern': 5,
'Cooler': 5,
'Ice Chest': 5,
'Canopy Tent': 20,
'Crazy Creek Chair': 5,
'Single Hammock': 8,
'Double Hammock': 10,
}

waterEquipment = {
    'Canoe': 25,
    'Kayak': 15,
    'Paddle Board': 20,
    'Helmet': 5,
    'PFD': 5,
    'Paddle': 5,
    'Dry Bag': 5,
    'Dry Pack': 10,
    'Ice Chest': 5,
}


class DateRangeSelector:
    def __init__(self, master):
        self.master = master
        self.master.title("Date Range Selector")
        self.master.geometry("300x250")
        self.master.configure(bg="#367653") 

        # Start Date Label
        self.start_label = ttk.Label(self.master, text="Start Date:")
        self.start_label.pack(pady=5)

        # Start Date Entry
        self.start_entry = ttk.Entry(self.master)
        self.start_entry.pack(pady=5)

        # End Date Label
        self.end_label = ttk.Label(self.master, text="End Date:")
        self.end_label.pack(pady=5)

        # End Date Entry
        self.end_entry = ttk.Entry(self.master)
        self.end_entry.pack(pady=5)

        # Land Rental Checkbox
        self.land_var = tk.BooleanVar()
        self.land_checkbox = ttk.Checkbutton(self.master, text="Land Rental", variable=self.land_var)
        self.land_checkbox.pack(pady=5)

        # Water Rental Checkbox
        self.water_var = tk.BooleanVar()
        self.water_checkbox = ttk.Checkbutton(self.master, text="Water Rental", variable=self.water_var)
        self.water_checkbox.pack(pady=5)

        # Submit Button
        self.submit_button = ttk.Button(self.master, text="Submit", command=self.submit)
        self.submit_button.pack(pady=10)

    def submit(self):
        start_date = self.start_entry.get()
        end_date = self.end_entry.get()
        land_rental = self.land_var.get()
        water_rental = self.water_var.get()

        # Convert input to datetime objects
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
            return

        # Check if start date is before end date
        if start_date > end_date:
            messagebox.showerror("Error", "Start date cannot be after end date.")
            return

        # Perform desired action with start_date, end_date, land_rental, and water_rental
        print("Start Date:", start_date)
        print("End Date:", end_date)
        print("Land Rental:", land_rental)
        print("Water Rental:", water_rental)

if __name__ == '__main__':
    root = tk.Tk()
    root.configure(bg="#367653")  # Set background color
    app = DateRangeSelector(root)
    root.mainloop()