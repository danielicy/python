from os import write
import PyPDF2


def rotatePdf():
    with open("files/first.pdf", "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        print(reader.numPages)
        page = reader.getPage(0)
        page.rotateClockwise(90)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open("files/rotated.pdf", "wb") as output:
            writer.write(output)


def mergepdfs():
    merger = PyPDF2.PdfFileMerger()
    file_names = ["files/first.pdf", "files/second.pdf"]
    for file_name in file_names:
        merger.append(file_name)
    merger.write("files/combined.pdf")


rotatePdf()
mergepdfs()
