from turtle import home
from flask import Flask,request, render_template
import joblib
import numpy as np
import os

img_f = os.path.join('static', 'img')

app = Flask(__name__,template_folder="Website")
app.config['UPLOAD_FOLDER'] = img_f

model = joblib.load('Air_Quality_Prediction.pkl')

@app.route('/')
@app.route('/home.html')
def hello():
    home = os.path.join(app.config['UPLOAD_FOLDER'], 'hero.png')
    return render_template("home.html", h = home)


@app.route('/about.html')
def hello_about():
    about = os.path.join(app.config['UPLOAD_FOLDER'], 'about.png')
    team1 = os.path.join(app.config['UPLOAD_FOLDER'], 'team-1.jpg')
    team2 = os.path.join(app.config['UPLOAD_FOLDER'], 'team-2.jpg')
    
    return render_template("about.html", ab =about,t1 = team1, t2 = team2)


@app.route('/pred.html')
def hello_price():
    return render_template("pred.html")

@app.route('/contact.html')
def hello_contact():
    return render_template("contact.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    data1= request.form['a']
    data5= request.form['b']
    data6= request.form['c']
    data7= request.form['d']
    data8= request.form['e']
    data10= request.form['f']
    data11= request.form['g']
    data1 = float(data1)
    data5 = float(data5)
    data6 = float(data6)
    data7 = float(data7)
    data8 = float(data8)
    data10 = float(data10)
    data11 = float(data11)
    data2 = (data5 + data6 + data7 + data8)
    data3 = (data5 * data8)
    data4 = (data6 * data8)
    data9 = (data7 * data10)
    arr = np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11]])
    pred=model.predict(arr)
    output = round(pred[0],2)
    return render_template('pred.html', data=f"Quality of Air according to the features you entered is {output}.")


if __name__ == '__main__':
    app.run(debug=True)