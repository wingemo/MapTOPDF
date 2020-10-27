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
import tkinter as tk
import _thread as thread
import tkinter.ttk as ttk
from tkinter import messagebox, Menu
from ttkthemes import ThemedStyle

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
