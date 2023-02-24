import tkinter as tk 
from tkinter import ttk

file = open("list.txt","r",encoding="utf8")
data = {}
while True:
    kelime = file.readline()
    if kelime != "":
        
            kelime = kelime.split("**")
            print(kelime)
            data.update({kelime[0] : kelime[1]})
            
    else:
         break        

    
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sözlük")
        self.geometry("600x400+50+50")
        self.name_var = tk.StringVar()
        self.create_widgets()
        root = tk.Tk()
        root.iconbitmap("logo.ico")

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 5}
        ttk.Label(self, text='Arayacağın şey nedir?').grid(column=0, row=0, **padding)

        name_entry = ttk.Entry(self, textvariable=self.name_var)
        name_entry.grid(column=1, row=0, **padding)
        name_entry.focus()

        submit_button = ttk.Button(self, text='Ara', command=self.submit)
        submit_button.grid(column=2, row=0, **padding)

        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=1, columnspan=3, **padding)

    def submit(self):
        yaazi = self.name_var.get()
        if yaazi in data:
            self.output_label.config(text=data[yaazi])

if __name__ == "__main__":
    app = App()
    app.mainloop()     
            