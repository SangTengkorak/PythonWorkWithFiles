import PyPDF2 as ppdf


def read_pdf():
    with open('recipe-book.pdf', 'r+b') as f:
        reader = ppdf.PdfFileReader(f)
        print(reader.numPages)
        print(reader.getDocumentInfo)

        for page in range(0, reader.numPages):
            pageObj = reader.getPage(page)
            print("\n" + pageObj.extractText())


if __name__ == "__main__":
    read_pdf()
