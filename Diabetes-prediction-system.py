# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 00:26:50 2024

@author: Owner
"""
import numpy as np
import pickle 
loaded_model = pickle.load(open('C:/Users\Owner\Documents\Ml-deploying model/Diabetes_model.sav','rb'))

input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

#import streamlit as st
#import joblib

#def main():
    #html_temp = """
    