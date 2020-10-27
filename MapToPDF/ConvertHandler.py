class ConvertHandler:
   def __init__(self):
        print_contents(self)
    
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
