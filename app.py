from flask import Flask, render_template
from flask import flash,request,redirect,url_for
import urllib.request
import os
import sys
from werkzeug.utils import secure_filename
import pprint
import requests
from flask import send_file
import webbrowser
from flask import Flask, send_from_directory

# rest = 'D:/AI_MODEL/SITE/BOTICX/VISION/YOLO/OBJECT_DETECTION/CODE/yolov5/utils/flask_rest_api'

# import subprocess
# subprocess.Popen("rest/script2.py 1", shell=True)

app = Flask(__name__)

# *************** variables start  *******************
UPLOAD_FOLDER = 'D:/AI_MODEL/SITE/BOTICX/VISION/YOLO/OBJECT_DETECTION/DATA/TRAIN_DATA/'
UPLOAD_IMAGE  = 'D:/AI_MODEL/data/proj1/testing_data/'
UPLOAD_IMAGE_yolo_image_detect    = 'D:/AI_MODEL/SITE/BOTICX/VISION/YOLO/OBJECT_DETECTION/DATA/UPLOAD/'
RES_YOLO = 'D:/AI_MODEL/SITE/BOTICX/VISION/YOLO/OBJECT_DETECTION/DATA/RESULT/'
# UPLOAD_IMAGE    = 'D:/AI_MODEL/SITE/BOTICX/VISION/YOLO/OBJECT_DETECTION/DATA/UPLOAD/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_IMAGE'] = UPLOAD_IMAGE
app.config['UPLOAD_IMAGE_yolo_image_detect'] = UPLOAD_IMAGE_yolo_image_detect
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif','txt'])

# # *************** multiple files upload *******************


# @app.route('/uploader1')
# def uploader1():
#     return render_template('upload.html')

# @app.route('/uploader1', methods = ['GET', 'POST'])
# def upload_file1():
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(request.url)
#     file = request.files['file']
#     if file.filename == '':
#         flash('No image selected for uploading')
#         return redirect(request.url)
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_IMAGE_yolo_image_detect'], filename))
#         #print('upload_image filename: ' + filename)
#         TEST_IMAGE = UPLOAD_IMAGE + filename        
 
#         DETECTION_URL = "http://192.168.0.101:5000/v1/object-detection/yolov5s"
#         params = {'name': filename}
#         response = requests.get(DETECTION_URL,params=params)
#         print(response.url)        
#         #requests.post(url = DETECTION_URL, data = data1) 
#         #requests.post(DETECTION_URL, json={"name": image})
#         return 'file uploaded successfully'


# @app.route('/upload-folder')
# def upload_form():
#     return render_template('data.html')

# @app.route('/upload-folder', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':

#         if 'files[]' not in request.files:
#             flash('No file part')
#             return redirect(request.url)

#         files = request.files.getlist('files[]')

#         for file in files:
#             if file and allowed_file(file.filename):
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#         flash('File(s) successfully uploaded')
#         return redirect('/upload-folder')

# # *************** END MULTIPLE FILES UPLOAD *******************

# *************** single image upload *******************
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload')
def home():
    return render_template('detection.html')
 
@app.route('/upload', methods=['POST', 'POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_IMAGE_yolo_image_detect'], filename))
        #print('upload_image filename: ' + filename)
        TEST_IMAGE = UPLOAD_IMAGE + filename
        #print (p)
        flash('Image successfully uploaded')
        #******************* CALL PYTHON FOR DETECTION ********************#
        # http://192.168.29.99:5000/
        DETECTION_URL = "http://192.168.0.101:5000/v1/object-detection/yolov5s"
        #DETECTION_URL = "http://192.168.29.99:5000/v1/object-detection/yolov5s"
        params = {'name': filename}
        response = requests.get(DETECTION_URL,params=params)
        print(response.url) 
        #RES_IMG = 'D:/AI_MODEL/SITE/BOTICX/VISION/YOLO/OBJECT_DETECTION/DATA/RESUT/' + filename
        #TEST_IMAGE = "D:/AI_MODEL/project/oj_det_yolov5/yolov5/data/images/zidane.jpg"
        #image_data = open(TEST_IMAGE, "rb").read()
        #requests.post(DETECTION_URL, files={"file": filename})
        #response = requests.post(DETECTION_URL, files={"image": image_data}).json()
        #pprint.pprint(response)

        #******************* RETUTN DETECTRD RESULT ********************#
        #return render_template('detection.html')
        #return render_template('detection.html', filename=filename)
        #RES_IMG = r'D:\AI_MODEL\flask\static\uploads\Screenshot_3.png'
        RES_NAME = RES_YOLO + filename
        return send_file(RES_NAME, mimetype='image/gif')
        #return  "success"
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)UPLOAD_IMAGE_yolo_image_detect
    return redirect(url_for('UPLOAD_IMAGE_yolo_image_detect', filename= filename), code=301)

# ***************  end  *******************
@app.route('/drag')
def drag():
    return render_template('drag.html')

@app.route('/drag', methods=['POST'])
def drag_image():
    if 'file' not in request.files:
        #flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        #flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_IMAGE_yolo_image_detect'], filename))
        #print('upload_image filename: ' + filename)
        #TEST_IMAGE = UPLOAD_IMAGE + filename
        #print (p)
        #flash('Image successfully uploaded')
        #******************* CALL PYTHON FOR DETECTION ********************#
        # DETECTION_URL = "http://192.168.0.101:5000/v1/object-detection/yolov5s"
        
        # #TEST_IMAGE = "D:/AI_MODEL/project/oj_det_yolov5/yolov5/data/images/zidane.jpg"
        # image_data = open(TEST_IMAGE, "rb").read()
        # response = requests.post(DETECTION_URL, files={"image": image_data}).json()
        # #flash(response)
        # pprint.pprint(response)

        #******************* RETUTN DETECTRD RESULT ********************#
        
        return render_template('drag.html')
        #return render_template('detection.html', filename=filename)
        #return  "success"
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)   
    
# images = { ‘name’ : ’buildings0.jpg’,‘caption’: ‘Lisboa’}

# @app.route("/show")
# def show():
#     return render_template('show.html',images = 'D:\AI_MODEL\flask\static\uploads\Screenshot_3.png')


###############################################

@app.route("/")
def signin():
    return render_template('page-1.html')


@app.route("/signup")
def signup():
    return render_template('page-2.html')
#...............................................

@app.route("/technology")
def technology():
    return render_template('page-3.html')

#...............................................

@app.route("/vision")
def vision():
    return render_template('page-4.html')

@app.route("/nlp")
def nlp():
    return render_template('page-5.html')

@app.route("/garuda")
def garuda():
    return render_template('garuda.html')
#...............................................

@app.route("/vision/face")
def vision_face():
    return render_template('page-6.html')

# @app.route("/vision/object_detection")
# def vision_boject_detection():
#     return render_template('page-4.html')

@app.route("/vision/object_detection")
def vision_boject_detection():
    return render_template('select.html')

#.......................   OBJECT DETECTION ........................

@app.route("/vision/object_detection/train")
def vision_obj_det_train():
    return render_template('upload_folder.html')

# *************** multiple files upload *******************

@app.route('/vision/object_detection/train', methods=['POST'])
def vision_obj_det_train_folder():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/vision/object_detection/train')


@app.route("/vision/object_detection/detect_yolo")
def vision_obj_det_detect():
    return render_template('detection.html')

@app.route('/vision/object_detection/detect_yolo', methods = ['GET', 'POST'])
def vision_obj_det_detect_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_IMAGE_yolo_image_detect'], filename))
        #print('upload_image filename: ' + filename)
        TEST_IMAGE = UPLOAD_IMAGE + filename        
 
        DETECTION_URL = "http://192.168.0.101:5000/v1/object-detection/yolov5s"
        params = {'name': filename}
        response = requests.get(DETECTION_URL,params=params)
        print(response.url)        
        #requests.post(url = DETECTION_URL, data = data1) 
        #requests.post(DETECTION_URL, json={"name": image})
        return 'file uploaded successfully'

#..................... Garuda ..........................

#.......................   SOLAR PLANT ........................
@app.route("/garuda/solar")
def garuda_solar():
    return render_template('select.html')

@app.route("/garuda/solar/train")
def garuda_solar_train():
    return render_template('upload_folder.html')


@app.route('/garuda/solar/train', methods=['POST'])
def garuda_solar_train_folder():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/vision/object_detection/train')


@app.route("/garuda/solar/detect_yolo")
def garuda_solar_detect():
    return render_template('detection.html')

@app.route('/garuda/solar/detect_yolo', methods = ['GET', 'POST'])
def garuda_solar_detect_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_IMAGE_yolo_image_detect'], filename))
        #print('upload_image filename: ' + filename)
        TEST_IMAGE = UPLOAD_IMAGE + filename        
 
        # DETECTION_URL = "http://192.168.0.101:5000/v1/object-detection/yolov5s"
        # params = {'name': filename}
        # response = requests.get(DETECTION_URL,params=params)
        # print(response.url)        
        #requests.post(url = DETECTION_URL, data = data1) 
        #requests.post(DETECTION_URL, json={"name": image})
        return 'file uploaded successfully'

    #--------------- GARUDA 2ND PROJECT ---------------------------#

    #.......................   TRANSMISSION LINE ........................
@app.route("/garuda/transmission")
def garuda_transmission():
    return render_template('select.html')

@app.route("/garuda/transmission/train")
def garuda_transmission_train():
    return render_template('upload_folder.html')

@app.route('/garuda/transmission/train', methods=['POST'])
def garuda_transmission_train_folder():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/vision/object_detection/train')


@app.route("/garuda/transmission/detect_yolo")
def garuda_transmission_detect():
    return render_template('detection.html')

@app.route('/garuda/transmission/detect_yolo', methods = ['GET', 'POST'])
def garuda_transmission_detect_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_IMAGE_yolo_image_detect'], filename))
        #print('upload_image filename: ' + filename)
        TEST_IMAGE = UPLOAD_IMAGE + filename        
 
        # DETECTION_URL = "http://192.168.0.101:5000/v1/object-detection/yolov5s"
        # params = {'name': filename}
        # response = requests.get(DETECTION_URL,params=params)
        # print(response.url)        
        #requests.post(url = DETECTION_URL, data = data1) 
        #requests.post(DETECTION_URL, json={"name": image})
        return 'file uploaded successfully'

    
#------------ GARUDA 3RD PROJECT------------------------

#.......................  highway ........................
@app.route("/garuda/highway")
def garuda_highway():
    return render_template('select.html')

@app.route("/garuda/highway/train")
def garuda_highway_train():
    return render_template('upload_folder.html')

# # *************** multiple files upload *******************

@app.route('/garuda/highway/train', methods=['POST'])
def garuda_highway_train_folder():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/vision/object_detection/train')

@app.route("/garuda/highway/detect_yolo")
def garuda_highway_detect():
    return render_template('detection.html')

@app.route('/garuda/highway/detect_yolo', methods = ['GET', 'POST'])
def garuda_highway_detect_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_IMAGE_yolo_image_detect'], filename))
        #print('upload_image filename: ' + filename)
        TEST_IMAGE = UPLOAD_IMAGE + filename        
 
        # DETECTION_URL = "http://192.168.0.101:5000/v1/object-detection/yolov5s"
        # params = {'name': filename}
        # response = requests.get(DETECTION_URL,params=params)
        # print(response.url)        
        #requests.post(url = DETECTION_URL, data = data1) 
        #requests.post(DETECTION_URL, json={"name": image})
        return 'file uploaded successfully'

#------------ GARUDA 4TH PROJECT------------------------

#.......................  warehouse ........................
@app.route("/garuda/warehouse")
def garuda_warehouse():
    return render_template('select.html')

@app.route("/garuda/warehouse/train")
def garuda_warehouse_train():
    return render_template('upload_folder.html')

# # *************** multiple files upload *******************

@app.route('/garuda/warehouse/train', methods=['POST'])
def garuda_warehouse_train_folder():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/vision/object_detection/train')

@app.route("/garuda/warehouse/detect_yolo")
def garuda_warehouse_detect():
    return render_template('detection.html')

@app.route('/garuda/warehouse/detect_yolo', methods = ['GET', 'POST'])
def garuda_warehouse_detect_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_IMAGE_yolo_image_detect'], filename))
        #print('upload_image filename: ' + filename)
        TEST_IMAGE = UPLOAD_IMAGE + filename        
 
        # DETECTION_URL = "http://192.168.0.101:5000/v1/object-detection/yolov5s"
        # params = {'name': filename}
        # response = requests.get(DETECTION_URL,params=params)
        # print(response.url)        
        #requests.post(url = DETECTION_URL, data = data1) 
        #requests.post(DETECTION_URL, json={"name": image})
        return 'file uploaded successfully'

#...............................................

@app.route("/train1")
def data_train_1():
    return render_template('page-7.html')

@app.route("/train2")
def data_train_2():
    return render_template('page-8.html')

@app.route("/train3")
def data_train_3():
    return render_template('page-9.html')

@app.route("/chatbot")
def chatbot():
    return render_template('page-10.html')

@app.route("/paragraph")
def paragraph():
    return render_template('page-11.html')
    
@app.route("/stt")
def stt():
    return render_template('page-12.html')

@app.route("/tts")
def tts():
    return render_template('page-13.html')

@app.route("/sentiment")
def sentiment():
    return render_template('page-14.html')

@app.route("/test")
def test():
    return render_template('tool.html')

# path_code  = "D:/AI_MODEL/SITE/Annotation_tool/LabelMeAnnotationTool-master/LabelMeAnnotationTool-master/"
# @app.route("path_code")
# def static_dir(path):
#     return send_from_directory("static", path)

@app.route("/notebook")
def notebook():
    # jupyter_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    # webbrowser.get(jupyter_path).open_new("www.google.com")
    os.chdir(r'D:/AI_MODEL/SITE')
    os.system("jupyter notebook")
    return render_template('page-3.html')


# @app.route("/static/<path:path>")
# def static_dir(path):
#     return send_from_directory("static", path)

@app.route("/label")
def label():
    # jupyter_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    # webbrowser.get(jupyter_path).open_new("www.google.com")
    os.chdir(r'D:/AI_MODEL/SITE/Annotation_tool/tool/LabelImg')
    os.system("python labelImg.py")
    return render_template('page-3.html')

# D:\AI_MODEL\SITE\Annotation_tool\tool\LabelImg
    
if  __name__== '__main__':
  app.debug=True
  #app.run('192.168.2.1', port=2000) #port can be anything higher than 5000.