# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 23:30:06 2023

@author: gadda
"""

import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# Load the saved model
loaded_suvmac = pickle.load(open('C:/Users/gadda/Desktop/Project files/parkinsons_disease_model.sav', 'rb'))

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

if prediction[0] == 0:
    print("The person does not have Parkinson's disease")
else:
    print("The person has Parkinson's disease")
