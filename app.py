from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Temperature = int(request.form['Temperature'])
        L =float(request.form['L'])
        R=float(request.form['R'])
        A_M=float(request.form['A_M'])
        Spectral_Class=request.form['Spectral_Class']
        if(Spectral_Class=='M'):
                M=1
                B=0
                O=0
                A=0
                F=0
                K=0
                G=0
        elif (Spectral_Class=='B'):
                M=0
                B=1
                O=0
                A=0
                F=0
                K=0
                G=0
        elif (Spectral_Class=='O'):
                M=0
                B=0
                O=1
                A=0
                F=0
                K=0
                G=0
        elif (Spectral_Class=='A'):
                M=0
                B=0
                O=0
                A=1
                F=0
                K=0
                G=0
        elif (Spectral_Class=='F'):
                M=0
                B=0
                O=0
                A=0
                F=1
                K=0
                G=0
        elif (Spectral_Class=='K'):
                M=0
                B=0
                O=0
                A=0
                F=0
                K=1
                G=0
        elif (Spectral_Class=='G'):
                M=0
                B=0
                O=0
                A=0
                F=0
                K=0
                G=1
        Color=request.form['Color']
        if(Color=='Red'):
                Red=1
                Blue=0
                Blue_white=0
                yellow_white=0
                Yellowish_White=0
                Orange_Red=0
                Pale_yellow_orange=0
                Whitish=0
                White=0
                yellowish=0
                orange=0
        elif (Color=='Blue'):
                Red=0
                Blue=1
                Blue_white=0
                yellow_white=0
                Yellowish_White=0
                Orange_Red=0
                Pale_yellow_orange=0
                Whitish=0
                White=0
                yellowish=0
                orange=0
        elif (Color=='White'):
                Red=0
                Blue=0
                Blue_white=0
                yellow_white=0
                Yellowish_White=0
                Orange_Red=0
                Pale_yellow_orange=0
                Whitish=0
                White=1
                yellowish=0
                orange=0
        elif (Color=='yellowish'):
                Red=0
                Blue=0
                Blue_white=0
                yellow_white=0
                Yellowish_White=0
                Orange_Red=0
                Pale_yellow_orange=0
                Whitish=0
                White=0
                yellowish=1
                orange=0
        elif (Color=='orange'):
                Red=0
                Blue=0
                Blue_white=0
                yellow_white=0
                Yellowish_White=0
                Orange_Red=0
                Pale_yellow_orange=0
                Whitish=0
                White=0
                yellowish=0
                orange=1
        elif (Color=='Blue_white'):
                Red=0
                Blue=0
                Blue_white=1
                yellow_white=0
                Yellowish_White=0
                Orange_Red=0
                Pale_yellow_orange=0
                Whitish=0
                White=0
                yellowish=0
                orange=0
        elif (Color=='yellow_white'):
                Red=0
                Blue=0
                Blue_white=0
                yellow_white=1
                Yellowish_White=0
                Orange_Red=0
                Pale_yellow_orange=0
                Whitish=0
                White=0
                yellowish=0
                orange=0
        elif (Color=='Yellowish_White'):
                Red=0
                Blue=0
                Blue_white=0
                yellow_white=0
                Yellowish_White=1
                Orange_Red=0
                Pale_yellow_orange=0
                Whitish=0
                White=0
                yellowish=0
                orange=0
        elif (Color=='Orange_Red'):
                Red=0
                Blue=0
                Blue_white=0
                yellow_white=0
                Yellowish_White=0
                Orange_Red=1
                Pale_yellow_orange=0
                Whitish=0
                White=0
                yellowish=0
                orange=0
        elif (Color=='Pale_yellow_orange'):
                Red=0
                Blue=0
                Blue_white=0
                yellow_white=0
                Yellowish_White=0
                Orange_Red=0
                Pale_yellow_orange=1
                Whitish=0
                White=0
                yellowish=0
                orange=0
        elif (Color=='Whitish'):
                Red=0
                Blue=0
                Blue_white=0
                yellow_white=0
                Yellowish_White=0
                Orange_Red=0
                Pale_yellow_orange=0
                Whitish=1
                White=0
                yellowish=0
                orange=0
        prediction=model.predict([[Temperature,L,R,A_M,O,B,A,F,G,K,M,Red,Blue,White,Whitish,Blue_white,yellow_white,Yellowish_White,Orange_Red,Pale_yellow_orange,yellowish,orange]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Input correct Parameters")
        else:
            return render_template('index.html',prediction_text="The Star is been classified as {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)