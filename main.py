import os
from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import MultipleFileField, StringField
import time
from instagrapi import Client

app = Flask(__name__)
name=None
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_IMAGES_DEST'] = 'name'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)
cl=Client()
class MyForm(FlaskForm):
    image = MultipleFileField('image')
    name=StringField('UserName')
    passw=StringField('Password')
    time=IntegerField('no. of hours between them')
def main(i,a,hours):
    cl.photo_upload(i,str(i).split('/')[-1].replace(".jpg",''))
    print('posr' +str(a))
    time.sleep(int(hours))
    return render_template('data.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    forms = MyForm()
    name=None
    passw=None
    hours=None

    if request.method=='POST':
        name=request.form['username']
        passw=request.form['password']
        hours=request.form['hours']
        for f in request.files.getlist('file[]'):
            f.save(os.path.join(f.filename))
        cl.login(name,passw)
        files = os.listdir()
        all_paths=[]
        for file in files:
            # make sure file is an image
            if file.endswith(('.jpg', '.png', 'jpeg')):
                all_paths.append(file)
        print(all_paths)
        a=0

            
        for i in all_paths:
            main(i,a,hours)
            print(a)
            
        a=a+1


    return render_template('home.html', form=forms,name=name,passw=passw,time=hours)
if __name__ == '__main__': 
    app.run(debug=True,host='0.0.0.0',port=8080)