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
        self.master.geometry("800x500")
        self.master.configure(bg="#367653")  # Set background color

        # Add Frame with background color
        self.frame = ttk.Frame(self.master, padding=(10, 10, 10, 0), style='my.TFrame')
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Start Date Label
        self.start_label = ttk.Label(self.frame, text="Start Date:")
        self.start_label.pack(pady=5)

        # Start Date Entry
        self.start_entry = ttk.Entry(self.frame)
        self.start_entry.pack(pady=5)

        # End Date Label
        self.end_label = ttk.Label(self.frame, text="End Date:")
        self.end_label.pack(pady=5)

        # End Date Entry
        self.end_entry = ttk.Entry(self.frame)
        self.end_entry.pack(pady=5)

        # Land Rental Checkbox
        self.land_var = tk.BooleanVar()
        self.land_checkbox = ttk.Checkbutton(self.frame, text="Land Rental", variable=self.land_var)
        self.land_checkbox.pack(pady=5)

        # Water Rental Checkbox
        self.water_var = tk.BooleanVar()
        self.water_checkbox = ttk.Checkbutton(self.frame, text="Water Rental", variable=self.water_var)
        self.water_checkbox.pack(pady=5)

        # Submit Button
        self.submit_button = ttk.Button(self.frame, text="Submit", command=self.submit)
        self.submit_button.pack(pady=10)

        # Style the frame
        style = ttk.Style()
        style.configure('my.TFrame', background='#367653')  # Set background color of frame

    def submit(self):
        start_date = self.start_entry.get()
        end_date = self.end_entry.get()
        land_rental = self.land_var.get()
        water_rental = self.water_var.get()

        # Convert input to datetime objects
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

            # Create a new page in a notebook
            new_page = ttk.Frame(self.master)
            new_page.pack(fill=tk.BOTH, expand=True)

            # Add a label to the new page

            if land_rental == True:
                label = ttk.Label(new_page, text="Land Rental")
                label.pack(pady=10)

                # Tent Label
                self.tent_label = ttk.Label(self.master, text="Tent:")
                self.tent_label.pack(pady=5)

                # Tent Dropdown Box
                self.tent_var = tk.StringVar()
                self.tent_dropdown = ttk.Combobox(self.master, values=[str(i) for i in range(10)], state="readonly", textvariable=self.tent_var)
                self.tent_dropdown.current(0)
                self.tent_dropdown.pack(pady=5)

                # Tent Output Box
                self.tent_output = ttk.Label(self.master, text="")
                self.tent_output.pack(pady=5)

                # Sleeping Bag Label
                self.sleeping_bag_label = ttk.Label(self.master, text="Sleeping Bag:")
                self.sleeping_bag_label.pack(pady=5)

                # Sleeping Bag Dropdown Box
                self.sleeping_bag_var = tk.StringVar()
                self.sleeping_bag_dropdown = ttk.Combobox(self.master, values=[str(i) for i in range(10)], state="readonly", textvariable=self.sleeping_bag_var)
                self.sleeping_bag_dropdown.current(0)
                self.sleeping_bag_dropdown.pack(pady=5)

                # Sleeping Bag Output Box
                self.sleeping_bag_output = ttk.Label(self.master, text="")
                self.sleeping_bag_output.pack(pady=5)

                # Backpack Label
                self.backpack_label = ttk.Label(self.master, text="Backpack:")
                self.backpack_label.pack(pady=5)

                # Backpack Dropdown Box
                self.backpack_var = tk.StringVar()
                self.backpack_dropdown = ttk.Combobox(self.master, values=[str(i) for i in range(10)], state="readonly", textvariable=self.backpack_var)
                self.backpack_dropdown.current(0)
                self.backpack_dropdown.pack(pady=5)

                # Backpack Output Box
                self.backpack_output = ttk.Label(self.master, text="")
                self.backpack_output.pack(pady=5)

                # Accessories Label
                self.accessories_label = ttk.Label(self.master, text="Accessories:")
                self.accessories_label.pack(pady=5)

                # 2 Burner Stove Label
                self.stove_label = ttk.Label(self.master, text="2 Burner Stove:")
                self.stove_label.pack(pady=5)

                # 2 Burner Stove Dropdown Box
                self.stove_var = tk.StringVar()
                self.stove_dropdown = ttk.Combobox(self.master, values=[str(i) for i in range(10)], state="readonly", textvariable=self.stove_var)
                self.stove_dropdown.current(0)
                self.stove_dropdown.pack(pady=5)

                # 2 Burner Stove Output Box
                self.stove_output = ttk.Label(self.master, text="")
                self.stove_output.pack(pady=5)

                # Cook Pot Set Label
                self.cook_pot_label = ttk.Label(self.master, text="Cook Pot Set:")
                self.cook_pot_label.pack(pady=5)

                # Cook Pot Set Dropdown Box
                self.cook_pot_var = tk.StringVar()
                self.cook_pot_dropdown = ttk.Combobox(self.master, values=[str(i) for i in range(10)], state="readonly", textvariable=self.cook_pot)


            elif water_rental == True & land_rental == False:
                label = ttk.Label(new_page, text="Water Rental")
                label.pack(pady=10)

            # Add a button to go back to the main page
            back_button = ttk.Button(new_page, text="Back", command=lambda: self.show_page(self.frame))
            back_button.pack()

            # Show the new page and hide the main page
            self.show_page(new_page)
            self.hide_page(self.frame)

        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please enter dates in the format: YYYY-MM-DD")

    def show_page(self, page):
        page.tkraise()

    def hide_page(self, page):
        page.pack_forget()

if __name__ == '__main__':
    root = tk.Tk()
    root.configure(bg="#367653")  # Set background color
    app = DateRangeSelector(root)
    root.mainloop()