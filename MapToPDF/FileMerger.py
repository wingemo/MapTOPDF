  """Deletes placeholder for input"""
        open_pdf = []
        x = [a for a in os.listdir(path) if a.endswith(".pdf")]
        merger = PdfFileMerger()

        for pdf in x:
            f = open(path + "\\"+ pdf, 'rb')
            open_pdf.append(f)
            merger.append(f)

        with open(path + "\\"+ PDF_OUTPUT_NAME, "wb") as fout:
            merger.write(fout)

        for pdf in open_pdf:
            pdf.close()
            merger.close()
