import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

# Dictionaries
landEquipment = {
    'Tent': 15,
    'Sleeping Bag': 8,
    'Backpack': 10,
    '2 Burner Stove': 10,
    'Lantern': 5,
    'Cook Pot Set': 5,
    'Water Cooler': 5,
    'Hammock': 8,
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
}




class RecreationCenterApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Recreation Center Equipment Rental")
        self.master.geometry("800x500")
        self.master.configure(bg="#367653")  # Set background color

        self.pagenum = 1
        self.page1()

    def page1(self):
        page = tk.Frame(self.master)
        page.grid()
        tk.Label(page, text='Date Selection').grid(row=0)
        tk.Button(page, text='Next Page', command=self.goto_page2).grid(row=5)

   
        tk.Label(page, text="Start Date:").grid(row=2, column=0, sticky=tk.W)
        tk.Entry(page, width=10).grid(row=2, column=1, sticky=tk.W)

        tk.Label(page, text="End Date:").grid(row=3, column=0, sticky=tk.W)
        tk.Entry(page, width=10).grid(row=3, column=1, sticky=tk.W)

        self.land_var = tk.BooleanVar()
        ttk.Checkbutton(page, text="Land Rentals", variable=self.land_var).grid(row=4, column=0, sticky=tk.W)
        
        self.water_var = tk.BooleanVar()
        ttk.Checkbutton(page, text="Water Rentals", variable=self.water_var).grid(row=4, column=1, sticky=tk.W)

    


    def page2(self):
        page = tk.Frame(self.master)
        page.grid()
        tk.Label(page, text='Land Rentals').grid(row=0)
        tk.Button(page, text='Back', command=self.goto_page1).grid(row=1)




    def goto_page1(self):
        if self.pagenum == 2:
            for widget in self.master.winfo_children():
                widget.destroy()
            self.pagenum = 1
            self.page1()

    def goto_page2(self):
        if self.pagenum == 1:
            for widget in self.master.winfo_children():
                widget.destroy()
            self.pagenum = 2
            self.page2()


if __name__ == '__main__':
    root = tk.Tk()
    app = RecreationCenterApplication(root)
    root.mainloop()