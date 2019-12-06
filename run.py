from data import app,db
import os
from model.school import School
from flask import render_template,request,redirect,url_for
import uuid



UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    S = School.query.order_by(School.id.desc()).first()
    print(S)
    if S.photos == None:
        S.photos = []
    print(S.photos)
    return render_template('index.html',photos=S.photos)

@app.route('/postimg',methods=['POST'])
def postimg():
    l = []
    S = School.query.order_by(School.id.desc()).first()
    if 'img' not in request.files:
        return '{"id": 0}'
    file = request.files['img']
    if file.filename == '':
        return '{"id": 0}'
    if file and allowed_file(file.filename):
        filename = str(uuid.uuid4())+'.'+file.filename.rsplit('.', 1)[1].lower()
        if S.photos != None:
            l += S.photos
        # print(l)    
        l.append(filename)
        S.photos=l
        # print(S.photos,l)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        db.session.commit()
    # print(img)
    # return redirect(url_for('index'))
    return '{"id": 101}'

app.run(debug= True)