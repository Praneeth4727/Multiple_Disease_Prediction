# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:01:53 2023

@author: gadda
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_ranfor = pickle.load(open('C:/Users/gadda/Desktop/Project files/breast_cancer_model.sav', 'rb'))


# Creating function for Predicting

def breastcancer_prediction(input_data):
    
    input_data = (20.29,14.34,135.1,1297,0.1003,0.1328,0.198,0.1043,0.1809,0.05883,0.7572,0.7813,5.438,94.44,0.01149,0.02461,0.05688,0.01885,0.01756,0.005115,22.54,16.67,152.2,1575,0.1374,0.205,0.4,0.1625,0.2364,0.07678)

    #change the input array into numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshaping the numpy array as we are predicting for only one instance.
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # prediction logic for women who is having Maligant or Benign

    prediction2 = loaded_ranfor.predict(input_data_reshaped)
    print(prediction2)
    if(prediction2[0] == 1):
      return "The breast cancer is Malignant"
    else:
      return "The Breast cancer is Benign"
  
    
def main():
    
    #title for webapp
    st.title('Breast Cancer Prediction WebApp')
    
    #Getting input from user
    input_fields = ["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]
     
    input_data_1 = []
    for i in range(len(input_fields)):
        sample_input = st.text_input('Enter value of '+ input_fields[i] + ':')
        input_data_1.append(sample_input)
        
        diagnosis = ''
        
    if st.button('Breast Cancer Classification Result'):
        diagnosis = breastcancer_prediction(input_data_1)

    st.success(diagnosis)
    

if __name__ == '__main__':
    main()