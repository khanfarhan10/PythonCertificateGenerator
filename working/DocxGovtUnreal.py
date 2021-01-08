
from docx import Document

"""
import os
print(os.getcwd())
"""

document = Document('Government_Certificate_Sample_Unreal.docx')

dic = {'Your_Amazing_Name': 'Farhan Hai Khan',
       'YOUR_AWESOME_NAME_HERE': 'FARHAN HAI KHAN',
       'COVID': 'Coronavirus Scale : 11.67 %',
       'Automated': 'Automated Tests : Passed Successfully',
       'Manual': 'Manual Tests : Passed with Considerations',
       'Description': 'Comments : Fit for Travel',
       'UID_Aadhaar': 'UID (Aadhaar) : 7458-2541-7364',
       'Cert': 'Certificate ID : 9546-8741-9463',
       'Generated': 'Generated : 22.06.2020 5:30GMT',
       'Signature': 'Rameshwar Manav',
       'Esteemed': 'RAMESHWAR MANAV',
       'Designation': 'Chief Engg. DVC',
       'Autograph': 'Shreya Shambhavi',
       'Responsibility': 'SHREYA SHAMBHAVI',
       'Pos': 'Radiologist RIMS'
       }
for p in document.paragraphs:
    inline = p.runs
    for i in range(len(inline)):
        text = inline[i].text
        print(text)
        if text in dic.keys():
            text = text.replace(text, dic[text])
            inline[i].text = text

document.save('Government_Certificate_Generated_Unreal.docx')

# TODO save to pdf

"""
from docx2pdf import convert

convert("input.docx", "output.pdf")

"""

# python DocxGovtUnreal.py
