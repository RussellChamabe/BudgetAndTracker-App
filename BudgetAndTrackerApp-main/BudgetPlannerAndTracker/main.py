
import tkinter as tk    # graphical interface
from tkinter import messagebox 
import pandas as pd

# tries to search if the users currently has a files called records.csv,
# if not, the program makes a temporary dataframe to help store data
try:
    df = pd.read_csv('./records.csv')
except Exception as e:
    # Creating a dictionary
    data = {
        "Date": [],
        "Description": [],
        "Amount": [],
        "Type": [],
    }

    # Creating a dataframe that creates a visualisation of the dictionary data
    df = pd.DataFrame(data)


# The class MUST be outside the try/except block
# Otherwise, if records.csv exists, the class never gets created

class BudgetTrackerApp:
    def __init__(self, root):
        # essentially saying ""this" root = root(from the function parameter)
        # and we use title to fetch the title function "
        self.root = root
        self.root.title("Budget Tracker")
        self.root.grid_columnconfigure(1, weight=1)


        # Labels and entries for each inputs from our dictionary above

        # Date
        self.label_date = tk.Label(root, text="Date (YY-MM-DD):")
        self.label_date.grid(row=0, column=0)
        self.entry_date = tk.Entry(root)
        self.entry_date.grid(row=0, column=1)

        # Description
        self.label_description = tk.Label(root, text="Description:")
        self.label_description.grid(row=1, column=0)
        self.entry_description = tk.Entry(root)
        self.entry_description.grid(row=1, column=1)

        # Amount
        self.label_amount = tk.Label(root, text="Amount:")
        self.label_amount.grid(row=2, column=0)
        self.entry_amount = tk.Entry(root)
        self.entry_amount.grid(row=2, column=1)

        # Type
        self.label_type = tk.Label(root, text="Type(Income/Expense):")
        self.label_type.grid(row=3, column=0)
        self.entry_type = tk.Entry(root)
        self.entry_type.grid(row=3, column=1)

        # Buttons
        self.button_add = tk.Button(
            root,
            text="Enter Information",
            command=self.add_entry
        )
        self.button_add.grid(row=4, column=0, columnspan=2)

        self.button_view = tk.Button(
            root,
            text="View Entries",
            command=self.view_entries
        )
        self.button_view.grid(row=5, column=0, columnspan=2)

        

    def add_entry(self):
        # storing data from entries the users
        # using get() function to retrieve the information that are stored
        # within each entry_x variables
        date = self.entry_date.get()
        description = self.entry_description.get()
        amount = self.entry_amount.get()
        entry_type = self.entry_type.get()

        if date and description and amount and entry_type:
            # Creates a new dataframe with the data entered above
            new_entry = pd.DataFrame({
                "Date": [date],
                "Description": [description],
                "Amount": [amount],
                "Type": [entry_type],
            })

            # allowing us to use the df variable which is outside of this function
            global df

            # the df variable from the start of this program is now updated
            # because both df and new_entry are being combined
            # and also ignoring index values
            df = pd.concat([df, new_entry], ignore_index=True)

            # saving the updated dataframe to csv
            df.to_csv('./records.csv', index=False)

            # Opens another user interface to display the message
            messagebox.showinfo("Saved", "Everything has been stored!")

        else:
            # Opens another user interface to display the message
            # and not showing it in terminal
            messagebox.showerror("Error", "All fields should be filled in")

    def view_entries(self):
        # temporary output to terminal
        print("This is the view of the information you have stored")
        print(df)


    
            # ---- workaround for VS Code debugger repaint lag ----
        def force_redraw(event=None):
            self.root.update_idletasks()

        for entry in (self.entry_date, self.entry_description, self.entry_amount, self.entry_type):
            entry.bind("<KeyRelease>", force_redraw)
            entry.bind("<FocusIn>", force_redraw)


# creates the window application
root = tk.Tk()
# creates the app using the class
app = BudgetTrackerApp(root)
# used to process user actions until the window is closed
root.mainloop()

import tkinter as tk    # graphical interface
from tkinter import messagebox 
import pandas as pd

# tries to search if the users currently has a files called records.csv,
# if not, the program makes a temporary dataframe to help store data
try:
    df = pd.read_csv('./records.csv')
except Exception as e:
    # Creating a dictionary
    data = {
        "Date": [],
        "Description": [],
        "Amount": [],
        "Type": [],
    }

    # Creating a dataframe that creates a visualisation of the dictionary data
    df = pd.DataFrame(data)


# The class MUST be outside the try/except block
# Otherwise, if records.csv exists, the class never gets created

class BudgetTrackerApp:
    def __init__(self, root):
        # essentially saying ""this" root = root(from the function parameter)
        # and we use title to fetch the title function "
        self.root = root
        self.root.title("Budget Tracker")
        self.root.grid_columnconfigure(1, weight=1)


        # Labels and entries for each inputs from our dictionary above

        # Date
        self.label_date = tk.Label(root, text="Date (YY-MM-DD):")
        self.label_date.grid(row=0, column=0)
        self.entry_date = tk.Entry(root)
        self.entry_date.grid(row=0, column=1)

        # Description
        self.label_description = tk.Label(root, text="Description:")
        self.label_description.grid(row=1, column=0)
        self.entry_description = tk.Entry(root)
        self.entry_description.grid(row=1, column=1)

        # Amount
        self.label_amount = tk.Label(root, text="Amount:")
        self.label_amount.grid(row=2, column=0)
        self.entry_amount = tk.Entry(root)
        self.entry_amount.grid(row=2, column=1)

        # Type
        self.label_type = tk.Label(root, text="Type(Income/Expense):")
        self.label_type.grid(row=3, column=0)
        self.entry_type = tk.Entry(root)
        self.entry_type.grid(row=3, column=1)

        # Buttons
        self.button_add = tk.Button(
            root,
            text="Enter Information",
            command=self.add_entry
        )
        self.button_add.grid(row=4, column=0, columnspan=2)

        self.button_view = tk.Button(
            root,
            text="View Entries",
            command=self.view_entries
        )
        self.button_view.grid(row=5, column=0, columnspan=2)

        

    def add_entry(self):
        # storing data from entries the users
        # using get() function to retrieve the information that are stored
        # within each entry_x variables
        date = self.entry_date.get()
        description = self.entry_description.get()
        amount = self.entry_amount.get()
        entry_type = self.entry_type.get()

        if date and description and amount and entry_type:
            # Creates a new dataframe with the data entered above
            new_entry = pd.DataFrame({
                "Date": [date],
                "Description": [description],
                "Amount": [amount],
                "Type": [entry_type],
            })

            # allowing us to use the df variable which is outside of this function
            global df

            # the df variable from the start of this program is now updated
            # because both df and new_entry are being combined
            # and also ignoring index values
            df = pd.concat([df, new_entry], ignore_index=True)

            # saving the updated dataframe to csv
            df.to_csv('./records.csv', index=False)

            # Opens another user interface to display the message
            messagebox.showinfo("Saved", "Everything has been stored!")

        else:
            # Opens another user interface to display the message
            # and not showing it in terminal
            messagebox.showerror("Error", "All fields should be filled in")



    #Creating a graphical interface where it will display the entries seperated from the main interface
    def view_entries(self):
        global df
        top = tk.Toplevel(self.root)
        top.title("View Entries")

        text = tk.Text(top)
        text.pack()

        for index,row in df.itterowws():
            text.insert(tk.END, "Date: " + row['Date'], "Description: " + row['Description'], "Amount: " + str(row['Amount']),"Type: " + row['Type'] + "\n"  )



# creates the window application
root = tk.Tk()
# creates the app using the class
app = BudgetTrackerApp(root)
# used to process user actions until the window is closed
root.mainloop()

