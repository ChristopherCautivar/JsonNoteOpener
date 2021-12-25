import json
import tkinter as tk
from tkinter import filedialog as fd


class NoteWindow(tk.Frame):
    def __init__(self, master=None, note=None, geo=None):
        super().__init__(master)
        self.master = master
        self.master.title(f"{self.master.title()} - {note['title']}")
        self.pack()
        i = 0
        for field in note:
            tk.Label(self, text=str(field) + ":").grid(row=i, padx=5, pady=10)
            tk.Label(self, text=str(note[field]), wraplength=200).grid(row=i, column=1, padx=5, pady=10)
            i += 1
        self.master.geometry(geo)
        self.master.geometry("")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.child_windows = []
        tk.Button(self, text="Open File", command=self.open_file).grid(row=1, column=0, padx=25, pady=10)
        tk.Button(self, text="Close All", command=self.close_all).grid(row=1, column=1, padx=25, pady=10)
        self.master.geometry(f"270x50+{int(self.winfo_screenwidth()/2)-120}+{int(self.winfo_screenheight()/2)-30}")
        self.master.resizable(0, 0)
        self.master.attributes("-topmost", 1)

    def close_all(self):
        for child in self.child_windows:
            child.master.destroy()

    def open_file(self):
        # children will be titled "the name of the file" - "the name of the note/todo"
        with open(fd.askopenfilename()) as file:
            if file:
                for note in json.load(file)["todos"]:
                    self.child_windows.append(NoteWindow(tk.Toplevel(), note, f"300x400+{len(self.child_windows) * 20}+"
                                                                              f"{len(self.child_windows) * 20}"))


root = tk.Tk()
root.title("JsonNoteOpener")
app = Application(root)
app.mainloop()
