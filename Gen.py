# import PDFNetPython3
import os
from PDFNetPython3 import PDFDoc, PDFNet, ContentReplacer, SDFDoc
print("Running Successfully")

ROOT_DIR = os.getcwd()
PDF_FILE = os.path.join(ROOT_DIR, "templates",
                        "Dark Blue Outer Space Achievement Certificate.pdf")
OUT_FILE = os.path.join(ROOT_DIR, "outputs",
                        "Out.pdf")


def generate_pdf():
    PDFNet.Initialize()

    # Example 1) Update a business card template with personalized info

    doc = PDFDoc(PDF_FILE)
    doc.InitSecurityHandler()

    # first, replace the image on the first page
    replacer = ContentReplacer()
    page = doc.GetPage(0)

    # next, replace the text place holders on the second page
    replacer.AddString("YOUR_AWESOME_NAME", "John Smith")
    # finally, apply
    replacer.Process(page)

    doc.Save(OUT_FILE, SDFDoc.e_linearized)
    doc.Close()

    print("Done. Result saved in :", OUT_FILE)


def generate_pdfs():
    PDFNet.Initialize()

    # Example 1) Update a business card template with personalized info

    doc = PDFDoc(input_path + "BusinessCardTemplate.pdf")
    doc.InitSecurityHandler()

    # first, replace the image on the first page
    replacer = ContentReplacer()
    page = doc.GetPage(1)
    img = Image.Create(doc.GetSDFDoc(), input_path + "peppers.jpg")
    replacer.AddImage(page.GetMediaBox(), img.GetSDFObj())
    # next, replace the text place holders on the second page
    replacer.AddString("NAME", "John Smith")
    replacer.AddString("QUALIFICATIONS", "Philosophy Doctor")
    replacer.AddString("JOB_TITLE", "Software Developer")
    replacer.AddString("ADDRESS_LINE1", "#100 123 Software Rd")
    replacer.AddString("ADDRESS_LINE2", "Vancouver, BC")
    replacer.AddString("PHONE_OFFICE", "604-730-8989")
    replacer.AddString("PHONE_MOBILE", "604-765-4321")
    replacer.AddString("EMAIL", "info@pdftron.com")
    replacer.AddString("WEBSITE_URL", "http://www.pdftron.com")
    # finally, apply
    replacer.Process(page)

    doc.Save(output_path + "BusinessCard.pdf", SDFDoc.e_linearized)
    doc.Close()

    print("Done. Result saved in BusinessCard.pdf")

    # Example 2) Replace text in a region with new text

    doc = PDFDoc(input_path + "newsletter.pdf")
    doc.InitSecurityHandler()

    replacer = ContentReplacer()
    page = doc.GetPage(1)
    replacer.AddText(page.GetMediaBox(),
                     "hello hello hello hello hello hello hello hello hello hello")
    replacer.Process(page)

    doc.Save(output_path + "ContentReplaced.pdf", SDFDoc.e_linearized)
    doc.Close()

    print("Done. Result saved in ContentReplaced.pdf")

    print("Done.")


if __name__ == '__main__':
    generate_pdf()
