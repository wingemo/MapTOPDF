# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""
    Kubernetes
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501
    The version of the OpenAPI document: release-1.16
    Generated by: https://openapi-generator.tech
"""
class ConvertHandler:
""" This class provides utility functions"""

   def __init__(self):
        """Deletes placeholder for input"""
        print_contents(self)
        path = self.contents.get()

   def update_progressbar(value):
       self.progress['value'] = value
       self.progress.update()

   def files_to_pdf(self): 
       """Deletes placeholder for input"""
        update_progressbar(10)
        
        # and split into a list of lines:
        try:
            for filename in os.listdir(path):
                if filename.endswith(".docx") or filename.endswith(".doc"):
                    convert(path + "\\" + filename)
                    continue
                elif filename.endswith(".jpg") or filename.endswith(".PNG")  or filename.endswith(".png"):
                    image1 = Image.open(path + "\\" + filename)
                    im1 = image1.convert('RGB')
                    im1.save(path + "\\" + filename + ".pdf")
                    continue
                else:
                    continue
        except:
            messagebox.showerror("Info", "Error")
 

    def merge_files(self):
        """Deletes placeholder for input"""
        self.progress['value'] = 30
        self.progress.update()

        # and split into a list of lines:
        open_pdf = []
        x = [a for a in os.listdir(path) if a.endswith(".pdf")]
        merger = PdfFileMerger()

        # and split into a list of lines:
        for pdf in x:
            f = open(path + "\\"+ pdf, 'rb')
            open_pdf.append(f)
            merger.append(f)

        # and split into a list of lines:
        with open(path + "\\"+ "result.pdf", "wb") as fout:
            merger.write(fout)

        # and split into a list of lines:
        for pdf in open_pdf:
            pdf.close()
            merger.close()

    def delete_files(self):
    """Deletes placeholder for input"""
        update_progressbar(50)

        # and split into a list of lines:
        for filename in os.listdir(path):
            if filename != "result.pdf":
                os.remove(path + "\\" + filename)

        update_progressbar(100)
        messagebox.showinfo("Info", "All files have been compiled into a pdf - Philip")
        update_progressbar(0)
