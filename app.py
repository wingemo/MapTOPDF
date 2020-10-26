from docx2pdf import convert
from PyPDF2 import PdfFileMerger
from PIL import Image
import sys,os
import tkinter as tk
from tkinter import messagebox, Menu
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import time
import _thread as thread

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

        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

        self.entrythingy.event_add('<<Paste>>', '<Button-3>')

        self.progress = ttk.Progressbar(root,
            length = 100, mode = 'indeterminate')
        self.progress.place(x = 0, y = 40, height = 15, width = 620)

        self.entrythingy.insert(0, "Klistra in sökvägen")
        self.entrythingy.configure(state="DISABLED")
        self.entrythingy.bind('<Button-1>', self.on_click)

    def on_click(self, master):
        self.entrythingy.configure(state="NORMAL")
        self.entrythingy.delete(0, "")


    def exitProgram(self):
        exit()

    def thread_start(self):
        thread.start_new_thread(self.print_contents())

    def print_contents(self):
        self.progress['maximum'] = 100
        self.progress['value'] = 10
        self.progress.update()
        x = 10

        try:
            path = self.contents.get()

            for filename in os.listdir(path):
                if filename.endswith(".docx") or filename.endswith(".doc"):
                    convert(path + "\\" + filename)
                    x = x + 2
                    self.progress['value'] = x
                    self.progress.update()
                    continue
                else:
                    continue
        except:
            messagebox.showerror("Info", "Error")


        self.progress['value'] = x
        self.progress.update()
        for filename in os.listdir(path):
            if filename.endswith(".jpg") or filename.endswith(".PNG")  or filename.endswith(".png"):
                image1 = Image.open(path + "\\" + filename)
                im1 = image1.convert('RGB')
                im1.save(path + "\\" + filename + ".pdf")
                continue
            else:
                continue

        self.progress['value'] = 30
        self.progress.update()

        open_pdf = []
        x = [a for a in os.listdir(path) if a.endswith(".pdf")]
        merger = PdfFileMerger()

        for pdf in x:
            f = open(path + "\\"+ pdf, 'rb')
            open_pdf.append(f)
            merger.append(f)


        self.progress['value'] = 40
        self.progress.update()

        with open(path + "\\"+ "result.pdf", "wb") as fout:
            merger.write(fout)

        for pdf in open_pdf:
            pdf.close()
            merger.close()

        self.progress['value'] = 50
        self.progress.update()

        for filename in os.listdir(path):
            if filename != "result.pdf":
                os.remove(path + "\\" + filename)

        self.progress['value'] = 100
        self.progress.update()

        messagebox.showinfo("Info", "All files have been compiled into a pdf - Philip")

        x = 0
        self.progress['value'] = 0


root = tk.Tk()
root.title("Map To PDF - Produced for Swedbank Philip Wingemo")
root.geometry("700x60")
style = ThemedStyle(root)
style.set_theme("plastik")
myapp = App(root)
myapp.mainloop()
