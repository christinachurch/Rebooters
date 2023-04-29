from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import tkcalendar as tkc
from datetime import date



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



# creates the main application as a class
class RecreationCenterApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Recreation Center Equipment Rental")
        self.master.geometry("439x400")
        self.master.configure(bg="#367653")  # Set background color
        self.master.grid_rowconfigure(0, weight=1)

        self.pagenum = 1



        self.dateSelection()
    

# -------------------------Functions--------------------------------------------    
# Function to calcuate the final cost of the equipment.
    def calculateLandCost(self, tent, sleepingbag, backpack, twoburnerstove, lantern, cookpotset, hammock, watercooler):
        for i in landEquipment:
            if i == 'Tent':
                tentCost = tent * landEquipment[i]
            elif i == 'Sleeping Bag':
                sleepingbagCost = sleepingbag * landEquipment[i]
            elif i == 'Backpack':
                backpackCost = backpack * landEquipment[i]
            elif i == '2 Burner Stove':
                twoburnerstoveCost = twoburnerstove * landEquipment[i]
            elif i == 'Lantern':
                lanternCost = lantern * landEquipment[i]
            elif i == 'Cook Pot Set':
                cookpotsetCost = cookpotset * landEquipment[i]
            elif i == 'Water Cooler':
                watercoolerCost = watercooler * landEquipment[i]
            elif i == 'Hammock':
                hammockCost = hammock * landEquipment[i]
        totalLandCost = tentCost + sleepingbagCost + backpackCost + twoburnerstoveCost + lanternCost + cookpotsetCost + watercoolerCost + hammockCost
        print(totalLandCost)
        return tentCost, sleepingbagCost, backpackCost, twoburnerstoveCost, lanternCost, cookpotsetCost, watercoolerCost, hammockCost
    
    def calculateWaterCost(self, canoe, kayak, paddleboard, pfd, paddle, drybag, drypack):
        for i in waterEquipment:
            if i == 'Canoe':
                canoeCost = canoe * waterEquipment[i]
            elif i == 'Kayak':
                kayakCost = kayak * waterEquipment[i]
            elif i == 'Paddle Board':
                paddleboardCost = paddleboard * waterEquipment[i]
            elif i == 'PFD':
                pfdCost = pfd * waterEquipment[i]
            elif i == 'Paddle':
                paddleCost = paddle * waterEquipment[i]
            elif i == 'Dry Bag':
                drybagCost = drybag * waterEquipment[i]
            elif i == 'Dry Pack':
                drypackCost = drypack * waterEquipment[i]
        totalWaterCost = canoeCost + kayakCost + paddleboardCost + pfdCost + paddleCost + drybagCost + drypackCost
        print(totalWaterCost)
        return canoeCost, kayakCost, paddleboardCost, pfdCost, paddleCost, drybagCost, drypackCost

#-------------------------Pages--------------------------------------------
# Function creates the first page to select the date and type of rental.
    def dateSelection(self):
        page = tk.Frame(self.master, width=300, height=600, bg="#367653")
        page.grid()
        today = date.today()

        img = Image.open("Rec Logo.png")
        img = img.resize((100, 100), Image.LANCZOS)  # Resize the image
        img_tk = ImageTk.PhotoImage(img)
        logo_label = tk.Label(page, image=img_tk)
        logo_label.image = img_tk 
        logo_label.grid(row=0, column=3, sticky=tk.NE)

        tk.Label(page, text='Date Selection', font=('Arial', 16), fg='white', bg="#367653").grid(row=0,pady= 10)

        tk.Label(page, text="Start Date:", font=('Arial', 14), fg='white', bg="#367653").grid(row=2, column=0, pady= 10, sticky=tk.W)
        tkc.DateEntry(page, mindate = today, width=15).grid(row=2, column=1, pady= 10, sticky=tk.W)

        tk.Label(page, text="End Date:", font=('Arial', 14), fg='white', bg="#367653").grid(row=3, column=0,pady= 10, sticky=tk.W)
        self.endDate = tkc.DateEntry(page, mindate = today, width=15).grid(row=3, column=1, pady= 10, sticky=tk.W)

        self.land_var = tk.BooleanVar()
        ttk.Checkbutton(page, text="Land Rentals", variable=self.land_var).grid(row=7, column=0, pady= 20, sticky=tk.W)
        
        self.water_var = tk.BooleanVar()
        ttk.Checkbutton(page, text="Water Rentals", variable=self.water_var).grid(row=7, column=1, pady= 10, sticky=tk.W)
        tk.Button(page, text='Next Page', command=self.goto_page2).grid(row=9, pady= 10)

# Function creates the second page to select the equipment for land rentals.

    def landRental(self):
        global landEquipment
        page = tk.Frame(self.master, bg="#367653")
        page.grid()
        
        img = Image.open("Rec Logo.png")
        img = img.resize((100, 100), Image.LANCZOS)  # Resize the image
        img_tk = ImageTk.PhotoImage(img)
        logo_label = tk.Label(page, image=img_tk)
        logo_label.image = img_tk 
        logo_label.grid(row=0, column=3, sticky=tk.NE)

        tk.Label(page, text='Land Rentals', font=('Arial', 14, 'bold'), fg='white', bg="#367653").grid(row=0)
        tk.Button(page, text='Back', command=self.goto_page1).grid(row=11)
        tk.Button(page, text='Next Page', command=self.goto_page3).grid(row=11, column=1)
    
        # Tent
        tk.Label(page, text='Tent', font=('Arial', 14), fg='white', bg="#367653").grid(row=2, column=0, sticky=tk.W)
        self.tent_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.tent_var, values=[0,1,2,3,4,5]).grid(row=2, column=1, sticky=tk.W)
        tk.Label(page, text='$15', fg='white', bg="#367653").grid(row=2, column=2, sticky=tk.W)

        # Sleeping Bag
        tk.Label(page, text='Sleeping Bag', font=('Arial', 14), fg='white', bg="#367653").grid(row=3, column=0, sticky=tk.W)
        self.sleepingbag_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.sleepingbag_var, values=[0,1,2,3,4,5]).grid(row=3, column=1, sticky=tk.W)
        tk.Label(page, text='$8', fg='white', bg="#367653").grid(row=3, column=2, sticky=tk.W)

        # Backpack
        tk.Label(page, text='Backpack', font=('Arial', 14), fg='white', bg="#367653").grid(row=4, column=0, sticky=tk.W)
        self.backpack_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.backpack_var, values=[0,1,2,3,4,5]).grid(row=4, column=1, sticky=tk.W)
        tk.Label(page, text='$10', fg='white', bg="#367653").grid(row=4, column=2, sticky=tk.W)

        tk.Label(page, text='Accessories', font=('Arial', 14, 'bold'), fg='white', bg="#367653").grid(row=5, column=0, sticky=tk.W)

        # 2 Burner Stove
        tk.Label(page, text='2 Burner Stove', font=('Arial', 14), fg='white', bg="#367653").grid(row=6, column=0, sticky=tk.W)
        self.twoburnerstove_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.twoburnerstove_var, values=[0,1,2,3,4,5]).grid(row=6, column=1, sticky=tk.W)
        tk.Label(page, text='$10', fg='white', bg="#367653").grid(row=6, column=2, sticky=tk.W)

        # Lantern
        tk.Label(page, text='Lantern', font=('Arial', 14), fg='white', bg="#367653").grid(row=7, column=0, sticky=tk.W)
        self.lantern_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.lantern_var, values=[0,1,2,3,4,5]).grid(row=7, column=1, sticky=tk.W)
        tk.Label(page, text='$5', fg='white', bg="#367653").grid(row=7, column=2, sticky=tk.W)

        # Cook Pot Set
        tk.Label(page, text='Cook Pot Set', font=('Arial', 14), fg='white', bg="#367653").grid(row=8, column=0, sticky=tk.W)
        self.cookpotset_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.cookpotset_var, values=[0,1,2,3,4,5]).grid(row=8, column=1, sticky=tk.W)
        tk.Label(page, text='$5', fg='white', bg="#367653").grid(row=8, column=2, sticky=tk.W)

        # Water Cooler
        tk.Label(page, text='Water Cooler', font=('Arial', 14), fg='white', bg="#367653").grid(row=9, column=0, sticky=tk.W)
        self.watercooler_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.watercooler_var, values=[0,1,2,3,4,5]).grid(row=9, column=1, sticky=tk.W)
        tk.Label(page, text='$5', fg='white', bg="#367653").grid(row=9, column=2, sticky=tk.W)

        # Hammock
        tk.Label(page, text='Hammock', font=('Arial', 14), fg='white', bg="#367653").grid(row=10, column=0, sticky=tk.W)
        self.hammock_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.hammock_var, values=[0,1,2,3,4,5]).grid(row=10, column=1, sticky=tk.W)
        tk.Label(page, text='$8', fg='white', bg="#367653").grid(row=10, column=2, sticky=tk.W)

        self.calcLandtotal = lambda: self.calculateLandCost(self.tent_var.get(), self.sleepingbag_var.get(), self.backpack_var.get(), self.twoburnerstove_var.get(), self.lantern_var.get(), self.cookpotset_var.get(), self.watercooler_var.get(), self.hammock_var.get())
        tk.Button(page, text='Calculate', command=self.calcLandTotal).grid(row=11, column=2)


# Function that creates the water rental page
    def waterRental(self):
        page = tk.Frame(self.master, bg="#367653")
        page.grid()

        img = Image.open("Rec Logo.png")
        img = img.resize((100, 100), Image.LANCZOS)  # Resize the image
        img_tk = ImageTk.PhotoImage(img)
        logo_label = tk.Label(page, image=img_tk)
        logo_label.image = img_tk 
        logo_label.grid(row=0, column=3, sticky=tk.NE)

        tk.Label(page, text='Water Rentals', font=('Arial', 14, 'bold'), fg='white', bg="#367653").grid(row=0)
        tk.Button(page, text='Back', command=self.goto_page1).grid(row=11)
        tk.Button(page, text='Next Page', command=self.goto_page3).grid(row=11, column=1)

        # Canoe
        tk.Label(page, text='Canoe', font=('Arial', 14), fg='white', bg="#367653").grid(row=2, column=0, sticky=tk.W)
        self.canoe_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.canoe_var, values=[0,1,2,3,4,5]).grid(row=2, column=1, sticky=tk.W)
        tk.Label(page, text='$25', fg='white', bg="#367653").grid(row=2, column=2, sticky=tk.W)

        # Kayak
        tk.Label(page, text='Kayak', font=('Arial', 14), fg='white', bg="#367653").grid(row=3, column=0, sticky=tk.W)
        self.kayak_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.kayak_var, values=[0,1,2,3,4,5]).grid(row=3, column=1, sticky=tk.W)
        tk.Label(page, text='$15', fg='white', bg="#367653").grid(row=3, column=2, sticky=tk.W)

        # Paddle Board
        tk.Label(page, text='Paddle Board', font=('Arial', 14), fg='white', bg="#367653").grid(row=4, column=0, sticky=tk.W)
        self.paddleboard_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.paddleboard_var, values=[0,1,2,3,4,5]).grid(row=4, column=1, sticky=tk.W)
        tk.Label(page, text='$20', fg='white', bg="#367653").grid(row=4, column=2, sticky=tk.W)

        tk.Label(page, text='Accessories', font=('Arial', 14, 'bold'), fg='white', bg="#367653").grid(row=5, column=0, sticky=tk.W)

        # PFD
        tk.Label(page, text='PFD', font=('Arial', 14), fg='white', bg="#367653").grid(row=6, column=0, sticky=tk.W)
        self.pfd_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.pfd_var, values=[0,1,2,3,4,5]).grid(row=6, column=1, sticky=tk.W)
        tk.Label(page, text='$5', fg='white', bg="#367653").grid(row=6, column=2, sticky=tk.W)

        # Paddles
        tk.Label(page, text='Paddles', font=('Arial', 14), fg='white', bg="#367653").grid(row=7, column=0, sticky=tk.W)
        self.paddles_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.paddles_var, values=[0,1,2,3,4,5]).grid(row=7, column=1, sticky=tk.W)
        tk.Label(page, text='$5', fg='white', bg="#367653").grid(row=7, column=2, sticky=tk.W)

        # Dry Bag
        tk.Label(page, text='Dry Bag', font=('Arial', 14), fg='white', bg="#367653").grid(row=8, column=0, sticky=tk.W)
        self.drybag_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.drybag_var, values=[0,1,2,3,4,5]).grid(row=8, column=1, sticky=tk.W)
        tk.Label(page, text='$5', fg='white', bg="#367653").grid(row=8, column=2, sticky=tk.W)

        # Dry Pack
        tk.Label(page, text='Dry Pack', font=('Arial', 14), fg='white', bg="#367653").grid(row=9, column=0, sticky=tk.W)
        self.drypack_var = tk.IntVar()
        ttk.Combobox(page, textvariable=self.drypack_var, values=[0,1,2,3,4,5]).grid(row=9, column=1, sticky=tk.W)
        tk.Label(page, text='$10', fg='white', bg="#367653").grid(row=9, column=2, sticky=tk.W)
        
        self.calcWaterTotal = lambda : self.calculateWaterCost(self.canoe_var.get(), self.kayak_var.get(), self.paddleboard_var.get(), self.pfd_var.get(), self.paddles_var.get(), self.drybag_var.get(), self.drypack_var.get())
        tk.Button(page, text='Calculate', command=self.calcWaterTotal).grid(row=11, column=2, sticky=tk.W)

# Function that creates the transaction summary page
    def transactionSummaryPage(self):
        page = tk.Frame(self.master, bg="#367653")
        page.grid()

        img = Image.open("Rec Logo.png")
        img = img.resize((100, 100), Image.LANCZOS)  # Resize the image
        img_tk = ImageTk.PhotoImage(img)
        logo_label = tk.Label(page, image=img_tk)
        logo_label.image = img_tk 
        logo_label.grid(row=0, column=3, sticky=tk.NE)
                
        tk.Label(page, text='Transaction Summary', font=('Arial', 14, 'bold'), fg='white', bg="#367653").grid(row=0)
        tk.Button(page, text='Back', command=self.goto_page2).grid(row=11)
        tk.Label(page, text=f'Start Date: {self.startDate}').grid(row=11, column=1)
        tk.Label(page, text=f'End Date: {self.endDate}').grid(row=11, column=2)
        tk.Label(page, text=self.calcTotal)
        # tk.Button(page, text='Submit', command=self.goto_page4).grid(row=11, column=1)

    #-------------------------Next Page Functions-----------------------------------    
# Function that returns from the rental pages to page 1
    def goto_page1(self):
        if self.pagenum == 2 or self.pagenum == 3:
            for widget in self.master.winfo_children():
                widget.destroy()
            self.pagenum = 1
            self.dateSelection()
        if self.pagenum == 3 & self.land_var.get() == True:
            for widget in self.master.winfo_children():
                widget.destroy()
            self.pagenum = 2
            self.land_var()
# Function that moves from page 1 to land or water rental page
    def goto_page2(self):
        global land_var, water_var 
        print(self.land_var.get(), self.water_var.get())
        if self.land_var.get() == True:  
            if self.pagenum == 1 or self.pagenum == 4:
                for widget in self.master.winfo_children():
                    widget.destroy()
                self.pagenum = 2
                self.landRental()
        elif self.water_var.get() == True:
            if self.pagenum == 1 or self.pagenum == 4:
                for widget in self.master.winfo_children():
                    widget.destroy()
                self.pagenum = 3
                self.waterRental()
# Function that moves from land or water rental page to transaction summary page of the water rental page, if both land and water are selected
    def goto_page3(self):
        global land_var, water_var
        if self.land_var.get() & self.water_var.get()== True:
            if self.pagenum == 2:
                for widget in self.master.winfo_children():
                    widget.destroy()
                self.pagenum = 3
                self.waterRental()
            else:
                for widget in self.master.winfo_children():
                    widget.destroy()
                self.pagenum = 4
                self.transactionSummaryPage()
        else:
            for widget in self.master.winfo_children():
                widget.destroy()
            self.pagenum = 4
            self.transactionSummaryPage()
        
        

# Main Function
if __name__ == '__main__':
    root = tk.Tk()
    app = RecreationCenterApplication(root)
    root.mainloop()