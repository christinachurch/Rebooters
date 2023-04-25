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
        self.dateSelection()

    def dateSelection(self):
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

    


    def landRental(self):
        page = tk.Frame(self.master)
        page.grid()
        tk.Label(page, text='Land Rentals').grid(row=0)
        tk.Button(page, text='Back', command=self.goto_page1).grid(row=1)

        # Tent
        tk.Label(page, text='Tent').grid(row=2, column=0, sticky=tk.W)
        self.tent_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.tent_var, values=[0,1,2,3,4,5]).grid(row=2, column=1, sticky=tk.W)
        tk.Label(page, text=self.tent_var.get()).grid(row=2, column=2, sticky=tk.W)

        # Sleeping Bag
        tk.Label(page, text='Sleeping Bag').grid(row=3, column=0, sticky=tk.W)
        self.sleepingbag_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.sleepingbag_var, values=[0,1,2,3,4,5]).grid(row=3, column=1, sticky=tk.W)
        tk.Label(page, text=self.sleepingbag_var.get()).grid(row=3, column=2, sticky=tk.W)

        # Backpack
        tk.Label(page, text='Backpack').grid(row=4, column=0, sticky=tk.W)
        self.backpack_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.backpack_var, values=[0,1,2,3,4,5]).grid(row=4, column=1, sticky=tk.W)
        tk.Label(page, text=self.backpack_var.get()).grid(row=4, column=2, sticky=tk.W)

        tk.Label(page, text='Accessories').grid(row=5, column=0, sticky=tk.W)

        # 2 Burner Stove
        tk.Label(page, text='2 Burner Stove').grid(row=6, column=0, sticky=tk.W)
        self.twoburnerstove_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.twoburnerstove_var, values=[0,1,2,3,4,5]).grid(row=6, column=1, sticky=tk.W)
        tk.Label(page, text=self.twoburnerstove_var.get()).grid(row=6, column=2, sticky=tk.W)

        # Lantern
        tk.Label(page, text='Lantern').grid(row=7, column=0, sticky=tk.W)
        self.lantern_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.lantern_var, values=[0,1,2,3,4,5]).grid(row=7, column=1, sticky=tk.W)
        tk.Label(page, text=self.lantern_var.get()).grid(row=7, column=2, sticky=tk.W)

        # Cook Pot Set
        tk.Label(page, text='Cook Pot Set').grid(row=8, column=0, sticky=tk.W)
        self.cookpotset_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.cookpotset_var, values=[0,1,2,3,4,5]).grid(row=8, column=1, sticky=tk.W)
        tk.Label(page, text=self.cookpotset_var.get()).grid(row=8, column=2, sticky=tk.W)

        # Water Cooler
        tk.Label(page, text='Water Cooler').grid(row=9, column=0, sticky=tk.W)
        self.watercooler_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.watercooler_var, values=[0,1,2,3,4,5]).grid(row=9, column=1, sticky=tk.W)
        tk.Label(page, text=self.watercooler_var.get()).grid(row=9, column=2, sticky=tk.W)

        # Hammock
        tk.Label(page, text='Hammock').grid(row=10, column=0, sticky=tk.W)
        self.hammock_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.hammock_var, values=[0,1,2,3,4,5]).grid(row=10, column=1, sticky=tk.W)
        tk.Label(page, text=self.hammock_var.get()).grid(row=10, column=2, sticky=tk.W)


    def waterRental(self):
        page = tk.Frame(self.master)
        page.grid()
        tk.Label(page, text='Water Rentals').grid(row=0)
        tk.Button(page, text='Back', command=self.goto_page1).grid(row=1)

        # Canoe
        tk.Label(page, text='Canoe').grid(row=2, column=0, sticky=tk.W)
        self.canoe_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.canoe_var, values=[0,1,2,3,4,5]).grid(row=2, column=1, sticky=tk.W)
        tk.Label(page, text=self.canoe_var.get()).grid(row=2, column=2, sticky=tk.W)

        # Kayak
        tk.Label(page, text='Kayak').grid(row=3, column=0, sticky=tk.W)
        self.kayak_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.kayak_var, values=[0,1,2,3,4,5]).grid(row=3, column=1, sticky=tk.W)
        tk.Label(page, text=self.kayak_var.get()).grid(row=3, column=2, sticky=tk.W)

        # Paddle Board
        tk.Label(page, text='Paddle Board').grid(row=4, column=0, sticky=tk.W)
        self.paddleboard_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.paddleboard_var, values=[0,1,2,3,4,5]).grid(row=4, column=1, sticky=tk.W)
        tk.Label(page, text=self.paddleboard_var.get()).grid(row=4, column=2, sticky=tk.W)

        tk.Label(page, text='Accessories').grid(row=5, column=0, sticky=tk.W)

        # PFD
        tk.Label(page, text='PFD').grid(row=6, column=0, sticky=tk.W)
        self.pfd_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.pfd_var, values=[0,1,2,3,4,5]).grid(row=6, column=1, sticky=tk.W)
        tk.Label(page, text=self.pfd_var.get()).grid(row=6, column=2, sticky=tk.W)

        # Paddles
        tk.Label(page, text='Paddles').grid(row=7, column=0, sticky=tk.W)
        self.paddles_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.paddles_var, values=[0,1,2,3,4,5]).grid(row=7, column=1, sticky=tk.W)
        tk.Label(page, text=self.paddles_var.get()).grid(row=7, column=2, sticky=tk.W)

        # Dry Bag
        tk.Label(page, text='Dry Bag').grid(row=8, column=0, sticky=tk.W)
        self.drybag_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.drybag_var, values=[0,1,2,3,4,5]).grid(row=8, column=1, sticky=tk.W)
        tk.Label(page, text=self.drybag_var.get()).grid(row=8, column=2, sticky=tk.W)

        # Dry Pack
        tk.Label(page, text='Dry Pack').grid(row=9, column=0, sticky=tk.W)
        self.drypack_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.drypack_var, values=[0,1,2,3,4,5]).grid(row=9, column=1, sticky=tk.W)
        tk.Label(page, text=self.drypack_var.get()).grid(row=9, column=2, sticky=tk.W)

    def goto_page1(self):
        if self.pagenum == 2 or self.pagenum == 3:
            for widget in self.master.winfo_children():
                widget.destroy()
            self.pagenum = 1
            self.dateSelection()

    def goto_page2(self):
        global land_var, water_var 
        print(self.land_var.get(), self.water_var.get())
        if self.land_var.get() == True:  
            if self.pagenum == 1:
                for widget in self.master.winfo_children():
                    widget.destroy()
                self.pagenum = 2
                self.landRental()
        elif self.water_var.get() == True:
            if self.pagenum == 1:
                for widget in self.master.winfo_children():
                    widget.destroy()
                self.pagenum = 3
                self.waterRental()
        


if __name__ == '__main__':
    root = tk.Tk()
    app = RecreationCenterApplication(root)
    root.mainloop()