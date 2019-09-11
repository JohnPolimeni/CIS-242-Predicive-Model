from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Sub Prime Mortag")
        vcmd = master.register(self.validate) # we have to wrap the command

        self.param1_value = 0
        self.param1_label = Label(master, text="param1")
        self.param1 = IntVar()
        self.param1.set(self.param1_value)
        self.param1_entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.param2_value = 0
        self.param2_label = Label(master, text="param2")
        self.param2 = IntVar()
        self.param2.set(self.param2_value)
        self.param2_entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.param3_value = 0
        self.param3_label = Label(master, text="param3")
        self.param3 = IntVar()
        self.param3.set(self.param3_value)
        self.param3_entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.param4_value = 0
        self.param4_label = Label(master, text="param4")
        self.param4 = IntVar()
        self.param4.set(self.param4_value)
        self.param4_entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.param5_value = 0
        self.param5_label = Label(master, text="param5")
        self.param5 = IntVar()
        self.param5.set(self.param5_value)
        self.param5_entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.submit_button = Button(master, text="Submit", command=lambda: self.update("submit"))
        
        # GLOBALS
        self.param_entries = [self.param1_entry, self.param2_entry, self.param3_entry, self.param4_entry, self.param5_entry]

        # LAYOUT
        self.param1_label.grid(row=0, column=0, sticky=W)
        self.param1_entry.grid(row=0, column=1, columnspan=2, sticky=E)
        self.param2_label.grid(row=1, column=0, sticky=W)
        self.param2_entry.grid(row=1, column=1, columnspan=2, sticky=E)
        self.param3_label.grid(row=2, column=0, sticky=W)
        self.param3_entry.grid(row=2, column=1, columnspan=2, sticky=E)
        self.param4_label.grid(row=3, column=0, sticky=W)
        self.param4_entry.grid(row=3, column=1, columnspan=2, sticky=E)
        self.param5_label.grid(row=4, column=0, sticky=W)
        self.param5_entry.grid(row=4, column=1, columnspan=2, sticky=E)

        self.submit_button.grid(row=5, column=0)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update_background_color(self, entry):
    	for entry in self.param_entries:
    		entry.config({"background": "red"})


    def update(self, method):
        if method == "submit":
            self.update_background_color("add")

root = Tk()
my_gui = Calculator(root)
root.mainloop()