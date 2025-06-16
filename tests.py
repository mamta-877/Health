from django.test import TestCase
import pandas as pd
import pickle
import numpy as np
import os
from django.conf import settings

# Create your tests here.
# loading model
model_path = os.path.join(settings.BASE_DIR, 'app/models/diabetes.pkl')
with open(model_path, 'rb') as model_file:
    diabetes_model = pickle.load(model_file)
# diabetes function
def diabetespredict(Pregnancies,Glucose,Blood_Pressure,Skin_Thickness,Insulin,BMI,DPF,Age):
    input_data=[Pregnancies,Glucose,Blood_Pressure,Skin_Thickness,Insulin,BMI,DPF,Age]
    df = pd.DataFrame(input_data)
    final=np.asarray(df)
    final= final.reshape(1,-1)
    prediction=diabetes_model.predict(final)
    output='Patient has Diabetes' if prediction[0] else '''Patient don't have Diabetes'''
    return output
# loading model
model_path1 = os.path.join(settings.BASE_DIR, 'app/models/liver.pkl')
with open(model_path1, 'rb') as model_file1:
    liver_model = pickle.load(model_file1)
# liver function
def liverpredict(Age,Gender,BMI,Alcohol,Smoking,Genetic_risk,Physical_activity,Diabetes,Hypertension,Liver_function_test):
    input_data=[Age,Gender,BMI,Alcohol,Smoking,Genetic_risk,Physical_activity,Diabetes,Hypertension,Liver_function_test]
    df = pd.DataFrame(input_data)
    final=np.asarray(df)
    final= final.reshape(1,-1)
    prediction=liver_model.predict(final)
    output='''Patient's liver is infected''' if prediction[0] else '''Patient's liver is safe'''
    return output
# loading model
model_path2 = os.path.join(settings.BASE_DIR, 'app/models/heart.pkl')    
with open(model_path2, 'rb') as model_file2:
    heart_model = pickle.load(model_file2)
# heart function
def heartpredict(Age,Sex,chest_pain_type,resting_bp,cholesterol,fasting_blood_sugar,resting_ecg,max_heart_rate,exercise_angina,oldpeak,st_slope):
    input_data=[Age,Sex,chest_pain_type,resting_bp,cholesterol,fasting_blood_sugar,resting_ecg,max_heart_rate,exercise_angina,oldpeak,st_slope]
    df = pd.DataFrame(input_data)
    final=np.asarray(df)
    final= final.reshape(1,-1)
    prediction=heart_model.predict(final)
    output='''Patient's heart is weak and can have a heart attack ''' if prediction[0] else '''Patient's heart is strong and is safe '''
    return output
# loading model
model_path3 = os.path.join(settings.BASE_DIR, 'app/models/brain.pkl')    
with open(model_path3, 'rb') as model_file3:
    brain_model = pickle.load(model_file3)
# brain function
def brainpredict(Age,Gender,Ethnicity,Education,BMI,Smoking,Alcohol,Physical_activity,Diet,Sleep,Family_history,CardiovascularDisease,Diabetes,Depression,HeadInjury,Hypertension,SystolicBP,DiastolicBP,CholesterolTotal,CholesterolLDL,CholesterolHDL,CholesterolTriglycerides,MMSE,FunctionalAssessment,Memory_comp,Behaviour,Adl,confusion,disorientation,personalityChanges,difficultyCompletingTasks,forgetfulness):
    input_data=[Age,Gender,Ethnicity,Education,BMI,Smoking,Alcohol,Physical_activity,Diet,Sleep,Family_history,CardiovascularDisease,Diabetes,Depression,HeadInjury,Hypertension,SystolicBP,DiastolicBP,CholesterolTotal,CholesterolLDL,CholesterolHDL,CholesterolTriglycerides,MMSE,FunctionalAssessment,Memory_comp,Behaviour,Adl,confusion,disorientation,personalityChanges,difficultyCompletingTasks,forgetfulness]
    df = pd.DataFrame(input_data)
    final=np.asarray(df)
    final= final.reshape(1,-1)
    prediction=brain_model.predict(final)
    output='Patient has alzheimers' if prediction[0] else "Patient is safe from alzheimers"
    return output 
