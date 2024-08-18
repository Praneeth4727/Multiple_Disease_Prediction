# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 18:26:50 2023

@author: gadda
"""

import numpy as np
import pickle

#loading the saved model
loaded_suvmac = pickle.load(open('C:/Users/gadda/Desktop/Project files/breast_cancer_model.sav', 'rb'))

input_data = (20.29,14.34,135.1,1297,0.1003,0.1328,0.198,0.1043,0.1809,0.05883,0.7572,0.7813,5.438,94.44,0.01149,0.02461,0.05688,0.01885,0.01756,0.005115,22.54,16.67,152.2,1575,0.1374,0.205,0.4,0.1625,0.2364,0.07678)

#change the input array into numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshaping the numpy array as we are predicting for only one instance.
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# prediction logic for women is having Maligant or Benign

prediction2 = loaded_suvmac.predict(input_data_reshaped)
print(prediction2)
if(prediction2[0] == 0):
  print("The breast cancer is Malignant")
else:
    print("The Breast cancer is Benign")