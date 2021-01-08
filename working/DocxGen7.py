
"""
from docx import Document

document = Document('temp/mai6.docx')

dic = {'Your_Amazing_Name': 'Farhan Hai Khan',
       'YOUR_AWESOME_NAME_HERE': 'FARHAN HAI KHAN',
       'COVID': 'Coronavirus Scale : 11.67 %',
       'Automated': 'Automated Tests : Passed Successfully',
       'Manual': 'Manual Tests : Passed with Considerations',
       'Description': 'Comments : Fit for Travel',
       'UID_Aadhaar': 'UID (Aadhaar) : 7458-2541-7364',
       'Cert': 'Certificate ID : 9546-8741-9463',
       'Generated':'Generated : 22.06.2020 5:30GMT',
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

document.save('temp/mai_out7.docx')
# python DocxGen7.py
"""


import zipfile

z = zipfile.ZipFile("temp/mai6.docx")

#print list of valid attributes for ZipFile object
#print (dir(z))

#print all files in zip archive
all_files = z.namelist()
#print (all_files)

#get all files in word/media/ directory
# images = filter(lambda x: x.startswith('word/media/') and (x.endswith('.png') or x.endswith('.jpg') or x.endswith('.jpeg') ), all_files)
images=[]
for x in all_files:
    condition=x.startswith('word/media/') and (x.endswith('.png') or x.endswith('.jpg') or x.endswith('.jpeg') )
    if condition:
        images.append(x)
print (images)

for img in images:
    image1 = z.open(img).read()
    f = open(img,'wb')
    f.write(image1)
"""
#open an image and save it
image1 = z.open('word/media/image1.jpeg').read()
f = open('image1.jpeg','wb')
f.write(image1)

#Extract file
z.extract('word/media/image1.jpeg', r'path_to_dir')
"""