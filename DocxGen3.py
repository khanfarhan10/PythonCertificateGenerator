
from docx import Document

document = Document('templates/2.docx')

dic = {'Damik_Dhar': 'P. J. James',
       '00.00': '04.03',
       'Passed_1': 'Passed Successfully',
       'Passed_2': 'Passed with Considerations',
       'Description': 'Fit for Travel',
       'XXXX-XXXX-XXXX': '7458-2541-7364',
       'AAAA-AAAA-AAAA': '9546-8741-9463',
       'FARHAN_HAI_KHAN': 'Rameshwar Manav',
       'NIRMALYA_MISRA': 'Shreya Shambhavi',
       }
for p in document.paragraphs:
    inline = p.runs
    for i in range(len(inline)):
        text = inline[i].text
        print(text)
        if text in dic.keys():
            text = text.replace(text, dic[text])
            inline[i].text = text

document.save('outputs/generated_doc2.docx')
