
from docx import Document

document = Document('template_certificates/MedicAI_Certification_2_Column.docx')

dic = {'Your_Amazing_Name': 'Farhan Hai Khan',
       'YOUR_AWESOME_NAME_HERE': 'FARHAN HAI KHAN',
       '00.00': '04.03',
       'Passed_1': 'Passed Successfully',
       'Passed_2': 'Passed with Considerations',
       'Brief_Description': 'Fit for Travel',
       'XXXX-XXXX-XXXX': '7458-2541-7364',
       'AAAA-AAAA-AAAA': '9546-8741-9463',
       'Signature_1': 'Rameshwar Manav',
       'Person_Name': 'RAMESHWAR MANAV',
       'Person_Designation': 'Chief Engg. DVC',
       'Signature_2': 'Shreya Shambhavi',
       'Person_Name_2': 'SHREYA SHAMBHAVI',
       'Person_Designation_2': 'Radiologist RIMS'
       }
for p in document.paragraphs:
    inline = p.runs
    for i in range(len(inline)):
        text = inline[i].text
        print(text)
        if text in dic.keys():
            text = text.replace(text, dic[text])
            inline[i].text = text

document.save('outputs/generated_docmedicAI.docx')
