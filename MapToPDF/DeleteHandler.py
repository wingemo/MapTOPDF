for filename in os.listdir(path):
            if filename != PDF_OUTPUT_NAME:
                os.remove(path + "\\" + filename)
