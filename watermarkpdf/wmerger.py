from fileinput import close
import PyPDF2
import sys
import os

pdf_list = sys.argv[1:]


def ft_pdf_merge(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append('pdfs/' + pdf)
    merger.write('merged_file.pdf')


ft_pdf_merge(pdf_list)

template = PyPDF2.PdfFileReader(open('merged_file.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for index in range(template.getNumPages()):
    page = template.getPage(index)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open('watermarked.pdf', 'wb') as file:
        output.write(file)


'''
PROGRAM
'''
