# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:27:50 2023

@author: gadda
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models


heart_disease_model = pickle.load(open('C:/Users/gadda/Desktop/Project files/heart_disease_model.sav', 'rb'))

breast_cancer_model = pickle.load(open('C:/Users/gadda/Desktop/Project files/breast_cancer_model.sav', 'rb'))

parkinsons_disease_model = pickle.load(open('C:/Users/gadda/Desktop/Project files/parkinsons_disease_model.sav', 'rb'))

# creating sidebar for navigation

with st.sidebar:
    
    selected = option_menu("Multiple Disease Prediction System", 
                           ['Heart Disease Prediction',
                            'Breast Cancer Prediction',
                            'Parkinsons Disease Prediction'],
                           icons = ['heart','person', 'activity'],
                           default_index = 0)
    

# heart disease prediction page

if selected == "Heart Disease Prediction":
    
    # Page Title
    st.title('Heart Disease Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
           
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')        
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
        
    # code for Prediction
    heart_target = ''
    
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        
            
        
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
        
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_target = 'The person is having heart disease'
        else:
          heart_target = 'The person does not have any heart disease'
        
    st.success(heart_target)
    
    
    
# breast cancer prediction page

if selected == "Breast Cancer Prediction":
    
    # Page Title
    st.title('Breast Cancer Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        radius_mean = st.text_input('Enter the value of radius mean')
        
    with col2:
        texture_mean = st.text_input('Enter the value of texture mean')
        
    with col3:
        perimeter_mean = st.text_input('Enter the value of perimeter mean')
        
    with col1:
        area_mean = st.text_input('Enter the value of area mean')
        
    with col2:
       smoothness_mean = st.text_input('Enter the value of smoothness mean')
        
    with col3:
        compactness_mean = st.text_input('Enter the value of compactness mean')
        
    with col1:
        concavity_mean = st.text_input('Enter the value of concavity mean')
        
    with col2:
        concave_points_mean = st.text_input('Enter the value of concave points mean')
        
    with col3:
        symmetry_mean = st.text_input('Enter the value of symmetry mean')
        
    with col1:
        fractal_dimension_mean = st.text_input('Enter the value of fractional dimensional mean')
        
    with col2:
        radius_se = st.text_input('Enter the value of radius se')
        
    with col3:
        texture_se = st.text_input('Enter the value of texture se')
        
    with col1:
        perimeter_se = st.text_input('Enter the value of perimeter se')
        
    with col2:
        area_se = st.text_input('Enter the value of area se')
        
    with col3:
        smoothness_se = st.text_input('Enter the value of smoothness se')
        
    with col1:
        compactness_se = st.text_input('Enter the value of compactness se')
        
    with col2:
        concavity_se = st.text_input('Enter the value of concavity se')
        
    with col3:
        concave_points_se = st.text_input('Enter the value of concave points se')
        
    with col1:
        symmetry_se = st.text_input('Enter the value of symmetry se')
        
    with col2:
        fractal_dimension_se = st.text_input('Enter the value of fractal dimensional se')
        
    with col3:
        radius_worst = st.text_input('Enter the value of radius worst')
        
    with col1:
        texture_worst = st.text_input('Enter the value of texture worst')
        
    with col2:
         perimeter_worst = st.text_input('Enter the value of perimeter worst')
         
    with col3:
         area_worst = st.text_input('Enter the value of area worst')
         
    with col1:
         smoothness_worst = st.text_input('Enter the value of smoothness worst')
         
    with col2:
         compactness_worst = st.text_input('Enter the value of compactness worst')
         
    with col3:
         concavity_worst = st.text_input('Enter the value of concavity worst')
         
    with col1:
         concave_points_worst = st.text_input('Enter the value of concave points worst')
         
    with col2:
         symmetry_worst = st.text_input('Enter the value of symmetry worst')
         
    with col3:
         fractal_dimension_worst = st.text_input('Enter the value of fractal dimensional worst')
         
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        breast_cancer_prediction = breast_cancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, 
perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])                          
        
        if (breast_cancer_prediction[0] == 1):
          breast_cancer_diagnosis = 'The breast cancer is Benign'
        else:
          breast_cancer_diagnosis = 'The breast cancer is Malignant'
        
    st.success(breast_cancer_diagnosis)
    
    # Parkinsons disease prediction page
    
if selected == "Parkinsons Disease Prediction":
    
    # Page Title
    
    st.title('Parkinsons Disease Prediction')
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('Enter the value of MDVP:Fo(Hz)')
            
    with col2:
        fhi = st.text_input('Enter the value of MDVP:Fhi(Hz)')
    
    with col3:
        flo = st.text_input('Enter the value of MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('Enter the value of MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('Enter the value of MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('Enter the value of MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('Enter the value of MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Enter the value of Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('Enter the value of MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('Enter the value of MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Enter the value of Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Enter the value of Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('Enter the value of MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Enter the value of Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('Enter the value of NHR')
    
    with col1:
        HNR = st.text_input('Enter the value of HNR')
        
    with col2:
        RPDE = st.text_input('Enter the value of RPDE')
        
    with col3:
        DFA = st.text_input('Enter the value of DFA')
        
    with col4:
        spread1 = st.text_input('Enter the value of spread1')
        
    with col5:
        spread2 = st.text_input('Enter the value of spread2')
        
    with col1:
        D2 = st.text_input('Enter the value of D2')
               
    with col2:
        PPE = st.text_input('Enter the value of PPE')
        
        
    
    
    # code for Prediction
    parkinsons_status = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Disease Test Result"):
        
        fo = float(fo)
        fhi = float(fhi)
        flo = float(flo)
        Jitter_percent = float(Jitter_percent)
        Jitter_Abs = float(Jitter_Abs)
        RAP = float(RAP)
        PPQ = float(PPQ)
        DDP = float(DDP)
        Shimmer = float(Shimmer)
        Shimmer_dB = float(Shimmer_dB)
        APQ3 = float(APQ3)
        APQ5 = float(APQ5)
        APQ = float(APQ)
        DDA = float(DDA)
        NHR = float(NHR)
        HNR = float(HNR)
        RPDE = float(RPDE)
        DFA = float(DFA)
        spread1 = float(spread1)
        spread2 = float(spread2)
        D2 = float(D2)
        PPE = float(PPE)
        parkinsons_disease_prediction = parkinsons_disease_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_disease_prediction[0] == 1):
          parkinsons_status = "The person has Parkinson's disease"
        else:
          parkinsons_status = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_status)

    
    

