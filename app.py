from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import shutil
#from utils import detect

import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/detect",methods =['POST'])
def images():

    if (request.method=='POST'):

        shutil.rmtree(os.path.join('tmp'))
        os.mkdir(os.path.join('tmp'))
        img = request.files['image']
        file_path = os.path.join('tmp',img.filename)
        img.save(file_path)

        #prediction = detect(file_path)

        return render_template('index.html', result='result',image = 'tmp/img.filename')
        


if __name__ == "__main__":
    app.run(debug=True)