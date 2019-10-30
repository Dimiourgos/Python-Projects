import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.convert_units = tk.Button(self, fg="blue", bd=3)
        self.convert_units["text"] = "CONVERT"
        self.convert_units["command"] = self.do_conversion
        self.convert_units.pack(side="left")

        self.in_units = tk.Entry(self, bd=3)
        self.in_units.pack(side="left")

        self.mile_label = tk.Label(self, text="Miles")
        self.mile_label.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red", bd=3, command=self.master.destroy)
        self.quit.pack(side="bottom")

    def do_conversion(self):
        print("Converting to Kilometers...")
        self.int_units = int(self.in_units.get())
        converted_units = float(self.int_units * 1.621371)
        print(converted_units)

        from tkinter import messagebox
        messagebox.showinfo("Kilometers:", converted_units)



root = tk.Tk()
app = Application(master=root)
app.mainloop()