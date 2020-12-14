
from docx import Document

document = Document('temp/mai5.docx')

dic = {'Your_Amazing_Name': 'Farhan Hai Khan',
       'YOUR_AWESOME_NAME_HERE': 'FARHAN HAI KHAN',
       'Coronavirus_Scale_Percentage': 'Coronavirus Scale : 11.67 %',
       'Automated_Test_Results': 'Automated Tests : Passed Successfully',
       'Manual_Reports': 'Manual Tests : Passed with Considerations',
       'Summary_Brief_Description': 'Comments : Fit for Travel',
       'XXXX_XXXX_XXXX': '7458-2541-7364',
       'AAAA_AAAA_AAAA': '9546-8741-9463',
       'MMDDYYYY_TT':'22.06.2020 5:30GMT',
       'Signature': 'Rameshwar Manav',
       'Esteemed_Name': 'RAMESHWAR MANAV',
       'Respected_Designation': 'Chief Engg. DVC',
       'Autograph': 'Shreya Shambhavi',
       'Responsibility_Name': 'SHREYA SHAMBHAVI',
       'Person_Post': 'Radiologist RIMS'
       }
for p in document.paragraphs:
    inline = p.runs
    for i in range(len(inline)):
        text = inline[i].text
        print(text)
        if text in dic.keys():
            text = text.replace(text, dic[text])
            inline[i].text = text

document.save('temp/mai_out5.docx')
# python DocxGen5.py