from flask import Flask,render_template,request,send_file
import numpy as np
import pandas as pd
import pickle
app = Flask(__name__)

model=pickle.load(open('pipeline.pkl','rb'))
#df=pickle.load(open('travel_data.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/pred')
def pred():
    return render_template('model.html')

@app.route('/additional/UD_RESUME.pdf')
def download_resume():
    return send_file('additional/UD_RESUME.pdf')

@app.route('/additional/Resume_Aditi.pdf')
def download_resumew():
    return send_file('additional/Resume_Aditi.pdf')

@app.route('/pred',methods=['POST','GET'])
def predd():
    input_features = {
        'Destination': request.form['Destination'],
        'Traveller_Count': float(request.form['Traveller_Count']),
        'Stay_Duration': float(request.form['Stay_Duration'])
    }
    dfs = pd.DataFrame([input_features])  # Create a DataFrame from the input

    prediction = model.predict(dfs)  # Assuming your model takes a DataFrame as input
    return render_template('model.html', preddd='Your budget for travel is {:.2f}'.format(prediction[0]))
  
if __name__=='__main__':
    app.run(debug=True)
