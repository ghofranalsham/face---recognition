from flask import Flask, render_template, request, jsonify, send_from_directory
import face_recognition
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/user/Desktop/recognitioin/known/uploads'# مسار الملف يلي رح يحفظلي الصورالمرفوع على التطبيق
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #المسار الي تم تعينه سابقا بيحفظه كجزء من اعدادات التطبيق

# تحميل الصور للأشخاص المعروفين
known_faces = [
    {"name": "Dr-mahmoud", "path": "C:/Users/user/Desktop/recognitioin/known/Dr-Mahmoud.jpeg"},
    {"name": "ghofran", "path": "C:/Users/user/Desktop/recognitioin/known/ghofran.jpeg"},
    
]

#---------------------------------------------------------------
for person in known_faces:
    person["image_path"] = f"/images/{person['name']}.jpeg"#عمل حلقة لتحديد مسار كل صورة في المجلد

known_face_encodings = [] # تعريف المتغيرين وتهيئتهما لتخزين ترميزات الوجوه وأسماء الأشخاص المعروفين.
known_face_names = []

for person in known_faces:
    image = face_recognition.load_image_file(person["path"])# person["path"]. يقوم هذا السطر بقراءة ملف الصورة وتحميله ككائن صورة يمكن معالجتهاface_recognition لتحميل صورة الشخص من الملف المحدد في وذلك باستخدام مكتبة
    encoding = face_recognition.face_encodings(image)[0]#عمل ترميز للوجه بالصورة لاستخدامه بالمقارنة الوجوه
    known_face_encodings.append(encoding)#ضافة الترميز الذي تم استخراجه للشخص إلى قائمة #known_face_encodings.
    known_face_names.append(person["name"])#: إضافة اسم الشخص إلى قائمة known_face_names.

# --------------------------------------------------------------------------------------
    


@app.route('/upload', methods=['POST'])#، يُستخدم الديكوراتور في فلاسك لتحديد كيفية استجابة التطبيق للطلبات على مسار محدد  يعني ذلك أن الوظيفة التي يتم تحديدها بعد الديكوراتور ستُستدعى عندما يتم إرسال طلب بوست
def upload():#يتم استدعاؤها عندما يتم تقديم طلب نوع POST إلى المسار "/upload" في تطبيق Flask الذي قمت بتطويره.

    try:
        
        file = request.files['file']#و قاموس يحتوي على الملفات المرفقة بالطلب، ويتم الوصول إلى الملف المرفق باستخدام اسم المفتاح (في هذه الحالة، 'file').
        name = request.form.get('name')  #هو قاموس يحتوي على بيانات النموذج المرفق بالطلب، ويتم الوصول إلى قيمة محددة باستخدام اسم المفتاح (هنا، 'name').

        if file.filename == '':     # الشرط يقوم بفحص إذا كان اسم الملف فارغا ام لا


            return jsonify({'result': 'No selected file'})#لارجاع الرد بين  العميل والسيرفر في حالة عدم وجود ملف 

#--------------------------------------------------------------------------------------------
        # قراءة الصورة المرسلة وتحويلها إلى ترميز للوجه
        img = Image.open(file)
        img = img.convert('RGB')
        unknown_image = face_recognition.load_image_file(file)

        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

        if not face_encodings:
            return jsonify({'result': 'No face found'})#الحالة، يتم إرجاع استجابة JSON تُبيِن أنه لم يتم العثور على وجوه.

        # ------------------------------------------------------------------------------------------
        recognized_names = []#هذه القائمة ستُستخدم لتخزين أسماء الأشخاص المُعرَفة في الصورة. فيما بعد، سيتم ملء هذه القائمة بأسماء الأشخاص الذين تم التعرف عليهم خلال مقارنة الوجوه في الصورة المُرفَعة مع الوجوه المعروفة.


        # ----------------------------------------------------------------------------------------------------
        for face_location, face_encoding in zip(face_locations, face_encodings):#يستخدم هذا الحلق للتكرار عبر قائمتين في نفس الوقت موقع الصورة وتشفير الوجه
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)#يُستخدم لمقارنة ترميز الوجه المُعرَّف مع الترميز الحالي للوجه اذا كان توافق رح يشير بترو ةاذا لم يجد سيشر بغير معروف
            name = "unknown"#اسم الوجه الافتراضي
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)#حسب مسافة الوجه الحالي من الوجوه المعروفة.وكل ما قلت المسافة كان التشابه اكبر

            if any(matches):#يتحقق من وجود عنصر
                index = matches.index(True)#يحصل على الفهرس (الموقع) الذي يحتوي على أول قيمة 
                name = known_face_names[index]#ستخدم الفهرس للوصول إلى اسم الشخص
                recognized_names.append(name)#بقوم باضافة اسم الشخص اللي انعرف لهي القائمة

                # رسم إطار حول الوجه المُعرَّف
                top, right, bottom, left = face_location
                draw = ImageDraw.Draw(img)
                draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=2)

                # إضافة اسم الشخص إلى الصورة
                draw.text((left, top - 20), name, fill=(0, 255, 0))

        # ----------------------------------------------------------------------------------------------------
        buffered = BytesIO()#يقوم بانشاء اوبجكت من نوع بايت يتم استخدامه لتخزين البيانات  في الذاكرة مؤقتة متغير
        img.save(buffered, format="JPEG")#يقوم بحفظ الصورة المعدلة في الخطوة السابقة بصيغة jpeg
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")#بتشفير البيانات الموجودة في بوفريد وتحويل النتيجة إلى سلسلة نصيةبيس64 لعرض الصورة بالواجهة

        response = {
            'result': 'success',
            'names': recognized_names,
            'image': img_str,
            'filename': file.filename  # تحمل اسم الملف الذي تم رفعه والمعالجة فيه
        }
        return jsonify(response)
    

    #------------------------------------------------------------------------------------------------------

    except Exception as e:#على سبيل المثال، إذا كان هناك خطأ في محاولة قراءة الصورة المرفوعة أو أي خطأ آخر، ستحتوي الرسالة على تفاصيل هذا الخطأ مما يساعد على تشخيص المشكلة وتحسين عملية التطوير والصيانة.
        return jsonify({'error': f'An error occurred: {str(e)}'})

# ---------------------------------------------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html', known_faces=known_faces)# يتيح للصفحة الرئيسية الوصول إلى البيانات حول الأشخاص المعروفين لديك.

# ---------------------------------------------------------------------------------------------
@app.route('/images/<name>.jpeg')#يقوم بتعريف نقطة نهاية  للمسارا 
def get_image(name):#حيث يتم توفير اسم الملف عن طريق استدعاء هي الدالة مثل لو كتبت اسم ملف د.محمود
    return send_from_directory("C:/Users/user/Desktop/recognitioin/known", f"{name}.jpeg")#تقوم بارسال اسم الملف المطلوب من المسار المحدد

# تقديم الصور
@app.route('/uploads/<filename>')#urlشير إلى أن الدالة التي تليهستُستدعى عندما يتم إرسال طلب إلى مسار محدد يحتوي على متغير داخلي يسمى ملف الاسم هذا المتغير يمكن أن يأخذ أي قيمة في عنوان
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':# تشغيل التطبق
    app.run(debug=True)#هذا يعني أن أي تغيير في الشيفرة سيؤدي إلى إعادة تشغيل التطبيق تلقائيًا بدون الحاجة إلى إعادة تشغيل الخادم يدويً
