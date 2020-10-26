import sys,os
import tkinter as tk
import time
import _thread as thread
import tkinter.ttk as ttk
from docx2pdf import convert
from PyPDF2 import PdfFileMerger
from PIL import Image
from tkinter import messagebox, Menu
from ttkthemes import ThemedStyle


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.w = ttk.Button(text ="Merge", command = self.thread_start)
        self.w.place(x = 629, y = 0, height = 35)

        self.entrythingy = ttk.Entry(font = "Calibri 12")
        self.entrythingy.place(x = 0, y = 0, height = 35, width = 620)

        self.contents = tk.StringVar()

        self.entrythingy["textvariable"] = self.contents

        self.entrythingy.bind('<Key-Return>', self.print_contents)

        self.entrythingy.event_add('<<Paste>>', '<Button-3>')

        self.progress = ttk.Progressbar(root, length = 100, mode = 'indeterminate')
        self.progress.place(x = 0, y = 40, height = 15, width = 620)

        self.entrythingy.insert(0, "Klistra in sökvägen")
        self.entrythingy.configure(state="DISABLED")
        self.entrythingy.bind('<Button-1>', self.on_click)

    def on_click(self, master):
        self.entrythingy.configure(state="NORMAL")
        self.entrythingy.delete(0, "")
    
    def thread_start(self):
         thread.start_new_thread(ConvertHanlder(self))

    def exitProgram(self):
        exit()

root = tk.Tk()
root.title("Map To PDF - Produced by Philip Wingemo")
root.geometry("700x60")
style = ThemedStyle(root)
style.set_theme("plastik")
myapp = App(root)
myapp.mainloop()
