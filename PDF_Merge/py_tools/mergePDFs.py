from PyPDF2 import PdfFileReader, PdfFileWriter
import time, os

def merge(input_files, output_folder):
    now = time.strftime("%Y%m%d%H%M%S")
    outputPDF = PdfFileWriter()
    for file in input_files:
        current_file = PdfFileReader(open(file, 'rb'))
        for pageNum in range(current_file.getNumPages()):
            outputPDF.addPage(current_file.getPage(pageNum))
    output_filename = 'MergedPDF-' + now + '.pdf'
    output_file = open(output_filename, 'wb')
    outputPDF.write(output_file)
    output_file.close()
    return os.path.join(output_folder, output_filename)
