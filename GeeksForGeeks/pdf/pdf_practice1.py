import PyPDF2

with open('dummy.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)  # It will retrun the total no of pages.

    # Getting the page 1
    page = reader.getPage(0)
    print(reader.getPage(0))

    # Rotating the page
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('twopage.pdf', 'wb') as newfile:
        writer.write(newfile)




