# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 02:54:50 2023

@author: gadda
"""

import numpy as np
import pickle
import streamlit as st
#import unittest


#loading the saved model
loaded_logreg = pickle.load(open('C:/Users/gadda/Desktop/Project files/heart_disease_model.sav', 'rb'))

# Creating function for Predicting

def heartdisease_prediction(input_data):
    

    #change the input array into numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshaping the numpy array as we are predicting for only one instance.
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # prediction logic for person is having heart disease or not
    prediction1 = loaded_logreg.predict(input_data_reshaped)
    print(prediction1)
    
    if(prediction1[0] == 1):
      return "Person is have heart disease"
    else:
      return "Person does not have heart disease"
  
    
  
def main():
    
    #title for webapp
    st.title('Heart Disease Prediction WebApp')
    
    # input data from user
    age = st.text_input('Age of person')
    sex = st.text_input('sex of person Male/Female')
    cp = st.text_input('chestpain of person')
    trestbps = st.text_input('Resting Blood Pressure of person')
    chol = st.text_input('Serum Cholesterol of person')
    fbs = st.text_input('Fasting Blood Sugar of person')
    restecg = st.text_input('Resting ElectroCardiographic Results of person')
    thalach = st.text_input('Maximum Heart Rate Achieved for person')
    exang = st.text_input(' Exercise-Induced Angina of person')
    oldpeak = st.text_input('ST depression induced by exercise relative to rest of a person')
    slope = st.text_input('The slope of Peak exercise of person in ST segment')
    ca = st.text_input('Number of Major Vessels for person')
    thal = st.text_input('Effect of Thalassemia of person')
    
    #code for performing prediction
    
    target = ''
    
    # creating a button for prediction
    
    if st.button('HeartDisease Result'):
            
        
        #convert input to appropriate data types
        age = int(age)
        sex = int(sex)
        cp = int(cp)
        trestbps = int(trestbps)
        chol = int(chol)
        fbs = int(fbs)
        restecg = int(restecg)
        thalach = int(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = int(slope)
        ca = int(ca)
        thal = int(thal)
        
        target = heartdisease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
            
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    