class FileConverter:
""" This class provides utility functions"""

   MESSAGEBOX_TITLE = "INFO"
   SUCCESS_MESSAGE = "All files have been compiled into a pdf - Philip"

   def __init__(self, path):
        """Deletes placeholder for input"""
        files_to_pdf(self)

   def files_to_pdf(self): 
        """Deletes placeholder for input"""
        try:
            for filename in os.listdir(path):
                if filename.endswith(".docx") or filename.endswith(".doc"):
                    multiprocessing.Process(target=word_to_pdf, args=(pdf))
                    continue
                elif filename.endswith(".jpg") or filename.endswith(".PNG")  or filename.endswith(".png"):
                    multiprocessing.Process(target=image_to_pdf, args=(pdf))
                    continue
                else:
                    continue
        except Exception as e:
            messagebox.showerror("Info", "Error" + str(e))
   
   def word_to_pdf(self):
       """Deletes placeholder for input"""
       convert(path + "\\" + filename)

   def image_to_pdf(self):
       """Deletes placeholder for input"""
       image1 = Image.open(path + "\\" + filename)
       im1 = image1.convert('RGB')
       im1.save(path + "\\" + filename + ".pdf")
