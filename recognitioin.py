import face_recognition
from PIL import Image, ImageDraw
from PIL import ImageFont
import time



# تحميل الصور للأشخاص المعروفين
dr_mahmoud_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/Dr-Mahmoud.jpeg")
dr_mahmoud_encoding = face_recognition.face_encodings(dr_mahmoud_image)[0]

ghofran_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/ghofran.jpeg")
ghofran_encoding = face_recognition.face_encodings(ghofran_image)[0]

sundus_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/sundus.jpeg")
sundus_encoding = face_recognition.face_encodings(sundus_image)[0]

sunduss_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/sundus1.jpeg")
sunduss_encoding = face_recognition.face_encodings(sunduss_image)[0]

ssundus_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/sundus2.jpeg")
ssundus_encoding = face_recognition.face_encodings(ssundus_image)[0]

zaidd_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/zaid.jpeg")
zaidd_encoding = face_recognition.face_encodings(zaidd_image)[0]

zaiid_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/zaid3M.jpeg")
zaiid_encoding = face_recognition.face_encodings(zaiid_image)[0] 

zaid_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/zaid 4 years.jpeg")
zaid_encoding = face_recognition.face_encodings(zaid_image)[0]


Albert_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/Albert einstein2.jpg")
Albert_encoding = face_recognition.face_encodings(Albert_image)[0]

Alberten_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/Albert einstein3.jpg")
Alberten_encoding = face_recognition.face_encodings(Alberten_image)[0]

Albertein_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/Albert einstein1.jpg")
Albertein_encoding = face_recognition.face_encodings(Albertein_image)[0]

Bassam_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/Bassam.jpg")
Bassam_encoding = face_recognition.face_encodings(Bassam_image)[0]

cris_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/cris.jpg")
cris_encoding = face_recognition.face_encodings(cris_image)[0]


criss_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/cris1.jpg")
criss_encoding = face_recognition.face_encodings(criss_image)[0]

cristiano_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/cristiano1.jpg")
cristiano_encoding = face_recognition.face_encodings(cristiano_image)[0]

cristianoo_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/cristiano2.jpg")
cristianoo_encoding = face_recognition.face_encodings(cristianoo_image)[0]

cristianno_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/cristiano3.jpg")
cristianno_encoding = face_recognition.face_encodings(cristianno_image)[0]

crristiano_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/cristiano4.jpg")
crristiano_encoding = face_recognition.face_encodings(crristiano_image)[0]


messi_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/messi.jpg")
messi_encoding = face_recognition.face_encodings(messi_image)[0]

messii_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/messi1.jpg")
messii_encoding = face_recognition.face_encodings(messii_image)[0]

meessi_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/messi2.jpg")
meessi_encoding = face_recognition.face_encodings(meessi_image)[0]

mmessi_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/messi3.jpg")
mmessi_encoding = face_recognition.face_encodings(mmessi_image)[0]

mess_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/messi4.jpg")
mess_encoding = face_recognition.face_encodings(mess_image)[0]

moatasem_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/Moatasem.jpg")
moatasem_encoding = face_recognition.face_encodings(moatasem_image)[0]

qusay_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/QUSAY.jpg")
qusay_encoding = face_recognition.face_encodings(qusay_image)[0]


samer_image = face_recognition.load_image_file("C:/Users/user/Desktop/recognitioin/known/samer.jpg")
samer_encoding = face_recognition.face_encodings(samer_image)[0]


known_face_encodings = [dr_mahmoud_encoding, ghofran_encoding, sundus_encoding ,zaid_encoding ,sunduss_encoding 
                        ,zaidd_encoding,zaidd_encoding  ,Albert_encoding,
                        Alberten_encoding,Albertein_encoding ,Bassam_encoding,cris_encoding, criss_encoding ,
                        cristiano_encoding , cristianno_encoding ,cristianoo_encoding,crristiano_encoding
                        ,messi_encoding,messii_encoding,mmessi_encoding,mess_encoding ,moatasem_encoding,
                        qusay_encoding ,samer_encoding ,]  


known_face_names = ["Dr-mahmoud ", "ghofran", "sundus" ,"zaid 4 years ","samer" ,"QUSAY"  ,"Moatasem"  ,"messi" ,
                    "messi1,","messi2." ,"messi3" ,"messi4","cristiano1","cristiano2","cristiano3",
                    "cristiano4.","cris","cris1" ,"Bassam" ,"Albert einstein1","Albert einstein2" ,"Albert einstein3"
                    ,"zaid" ,"zaid3M" , "sundus1" ,"sundus2"
                                          ]

image_number = input("please enter image number: ")
unknown_image = face_recognition.load_image_file(f'C:/Users/user/Desktop/recognitioin/unknown/{image_number}.jpeg')

face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

pil_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(pil_image)

# تحميل الصور للأشخاص المعروفين
# (الكود الحالي)

# ...

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "unknown"

    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    print(face_distances)
    match_found = any(matches)
    

import time

start_time = time.time()

match_found = False  # افتراضيًا لم يتم العثور على تطابق
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    for name, match in zip(known_face_names, matches):
        if match:
            print(f"Matched with: {name}")
            match_found = True  
            

            # عرض الصورة المطابقة بشكل منفصل
           # matched_face = unknown_image[top:bottom, left:right]
           # pil_matched_image = Image.fromarray(matched_face)
           # pil_matched_image.show()  # عرض الصورة المُعرَّف

            # حساب الوقت المستغرق
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Elapsed Time: {elapsed_time} seconds")

            # عرض الصورة الأصلية مع الوجه المُعرَّف واسمه
            pil_image_with_boxes = Image.fromarray(unknown_image)
            draw = ImageDraw.Draw(pil_image_with_boxes)
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255), width=2)

            # تحديد خصائص النص
            font = ImageFont.truetype("arial.ttf", 30)  # تحديد نوع الخط وحجمه
            text_color = (255, 0, 0)  # لون النص (بالترتيب: الأحمر، الأخضر، الأزرق)

            # عرض الاسم على الصورة
            draw.text((left, top - 30), name, fill=text_color, font=font)
            pil_image_with_boxes.show()  # عرض الصورة النهائية مع الوجه المُعرَّف واسمه

            break  # توقف عند العثور على تطابق

    if match_found:
        break  # توقف بمجرد العثور على تطابق


