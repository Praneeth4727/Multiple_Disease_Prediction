# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 00:51:16 2023

@author: gadda
"""

import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
import streamlit as st

#loading the saved model
loaded_suvmac = pickle.load(open('C:/Users/gadda/Desktop/Project files/parkinsons_disease_model.sav', 'rb'))

def parkinsonsdisease_prediction(input_data):
    input_data = np.array([
        [119.992,157.302,74.997,0.00784,0.00007,0.0037,0.00554,0.01109,0.04374,0.426,0.02182,0.0313,0.02971,0.06545,0.02211,21.033,0.414783,0.815285,-4.813031,0.266482,2.301442,0.284654]
    ])

    # Initialize the StandardScaler and fit on the input data
    scaler = StandardScaler()
    scaler.fit(input_data)

    # Reshape the input data
    input_data_reshaped = scaler.transform(input_data)

    # Make predictions
    prediction = loaded_suvmac.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 1:
        return "The person does not have Parkinson's disease"
    else:
        return "The person has Parkinson's disease"
    
def main():
    
    #title for webapp
    st.title('ParkinsonsDisease Prediction WebApp')
    
    #Getting input from user
    input_fields = ["MDVP:Fo(Hz)","MDVP:Fhi(Hz)","MDVP:Flo(Hz)","MDVP:Jitter(%)","MDVP:Jitter(Abs)","MDVP:RAP","MDVP:PPQ","Jitter:DDP","MDVP:Shimmer","MDVP:Shimmer(dB)","Shimmer:APQ3","Shimmer:APQ5","MDVP:APQ","Shimmer:DDA","NHR","HNR","RPDE","DFA","spread1","spread2","D2","PPE"]
     
    input_data_1 = []
    for i in range(len(input_fields)):
        sample_input = st.text_input('Enter value of '+ input_fields[i] + ':')
        input_data_1.append(sample_input)
        
        status = ''
        
    if st.button('ParkinsonsDisease Classification Result'):
        status = parkinsonsdisease_prediction(input_data_1)

    st.success(status)
    

if __name__ == '__main__':
    main()
