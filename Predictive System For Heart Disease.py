# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#loading the saved model
loaded_logreg = pickle.load(open('C:/Users/gadda/Desktop/Project files/heart_disease_model.sav', 'rb'))

input_data = (89,5,2,235,325,6,8,98,2,0.7,7,3,90)



#change the input array into numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshaping the numpy array as we are predicting for only one instance.
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# prediction logic for person is having heart disease or not
prediction1 = loaded_logreg.predict(input_data_reshaped)
print(prediction1)
if(prediction1[0] == 1):
  print("The person does not have heart disease")
else:
  print("person is having heart disease")