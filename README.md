# MapTOPDF
Free GUI software that converts a folder of files into a single pdf.

pyinstaller is missing hook script to run docx2pdf. [Issue](https://github.com/AlJohri/docx2pdf/issues/5)


>save hook-docx2pdf.py to \Lib\site-packages\PyInstaller\hooks
> and paste from PyInstaller.utils.hooks import collect_all
> datas, binaries, hiddenimports = collect_all('docx2pdf')

or

>go to Lib\site-packages\PyInstaller\hooks folder. open the fiile hook-docx2pdf.py remove or comment its content and paste
>from PyInstaller.utils.hooks import collect_all
>datas, binaries, hiddenimports = collect_all('docx2pdf')
