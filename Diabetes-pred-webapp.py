# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 01:51:19 2024

@author: Owner
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users\Owner\Documents\Ml-deploying model/Diabetes_model.sav','rb'))

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
def main():

    #giving a title
    st.title('Diabetes Prediction Web App')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPredigreeFunction = st.text_input('Diabetes Predigree Function value')
    Age = st.text_input('Age of the person')
    
    diagnosis = ''
    
    #creating a button
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPredigreeFunction,Age])
        
    st.success(diagnosis) 
    
if __name__ == '__main__':
    main()    
    