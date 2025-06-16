from django.shortcuts import render
from app import tests

# Create your views here.
def index(request):
    return render(request,'index.html')
def diabetes(request):
    return render(request,'diabetes.html')
def brain(request):
    return render(request,'brain.html')
def heart(request):
    return render(request,'heart.html')
def liver(request):
    return render(request,'liver.html')
# diabetes
def dia_predict(request):
    if request.method=='POST':
        Pregnancies=request.POST.get('Pregnancies')
        Glucose=request.POST.get('Glucose')
        Blood_Pressure=request.POST.get('Blood_Pressure')
        Skin_Thickness=request.POST.get('Skin_Thickness')
        Insulin=request.POST.get('Insulin')
        BMI=request.POST.get('BMI')
        DPF=request.POST.get('DPF')
        Age=request.POST.get('Age')
        diabetes_output=tests.diabetespredict(Pregnancies,Glucose,Blood_Pressure,Skin_Thickness,Insulin,BMI,DPF,Age)
    context={
        "diabetes_Result":f"{diabetes_output}"
    }
    return render(request,'diabetes.html',context)
# liver disease
def liver_predict(request):
    if request.method=='POST':
        Age=request.POST.get('age')
        Gender=request.POST.get('gender')
        BMI=request.POST.get('bmi')
        Alcohol=request.POST.get('alcohol')
        Smoking=request.POST.get('smoking')
        Genetic_risk=request.POST.get('genetic-risk')
        Physical_activity=request.POST.get('physical-activity')
        Diabetes=request.POST.get('diabetes')
        Hypertension=request.POST.get('hypertension')
        Liver_function_test=request.POST.get('liver-function-test')
        liver_output=tests.liverpredict(Age,Gender,BMI,Alcohol,Smoking,Genetic_risk,Physical_activity,Diabetes,Hypertension,Liver_function_test)
    context={
        "liver_Result":f"{liver_output}"
    }
    return render(request,'liver.html',context)
# heart disease
def heart_predict(request):
    if request.method=='POST':
        Age=request.POST.get('age')
        Sex=request.POST.get('sex')
        chest_pain_type=request.POST.get('chest-pain-type')
        resting_bp=request.POST.get('resting-bp')
        cholesterol=request.POST.get('cholesterol')
        fasting_blood_sugar=request.POST.get('fasting-blood-sugar')
        resting_ecg=request.POST.get('resting-ecg')
        max_heart_rate=request.POST.get('max-heart-rate')
        exercise_angina=request.POST.get('exercise-angina')
        oldpeak=request.POST.get('oldpeak')
        st_slope=request.POST.get('st-slope')
        heart_output=tests.heartpredict(Age,Sex,chest_pain_type,resting_bp,cholesterol,fasting_blood_sugar,resting_ecg,max_heart_rate,exercise_angina,oldpeak,st_slope)
    context={
        "heart_Result":f"{heart_output}"
    }
    return render(request,'heart.html',context)
# brain disease
def brain_predict(request):
    if request.method=='POST':
        Age=request.POST.get('age')
        Gender=request.POST.get('gender')
        Ethnicity=request.POST.get('ethnicity')
        Education=request.POST.get('educationLevel')
        BMI=request.POST.get('bmi')
        Smoking=request.POST.get('smoking')
        Alcohol=request.POST.get('alcoholConsumption')
        Physical_activity=request.POST.get('physicalActivity')
        Diet=request.POST.get('dietQuality')
        Sleep=request.POST.get('sleepQuality')
        Family_history=request.POST.get('familyHistory')
        CardiovascularDisease=request.POST.get('CardiovascularDisease')
        Diabetes=request.POST.get('Diabetes')
        Depression=request.POST.get('Depression')
        HeadInjury=request.POST.get('HeadInjury')
        Hypertension=request.POST.get('Hypertension')
        SystolicBP=request.POST.get('SystolicBP')
        DiastolicBP=request.POST.get('DiastolicBP')
        CholesterolTotal=request.POST.get('CholesterolTotal')
        CholesterolLDL=request.POST.get('CholesterolLDL')
        CholesterolHDL=request.POST.get('CholesterolHDL')
        CholesterolTriglycerides=request.POST.get('CholesterolTriglycerides')
        MMSE=request.POST.get('MMSE')
        FunctionalAssessment=request.POST.get('FunctionalAssessment')
        Memory_comp=request.POST.get('memoryComplaints')
        Behaviour=request.POST.get('behavioralProblems')
        Adl=request.POST.get('adl')
        confusion=request.POST.get('confusion')
        disorientation=request.POST.get('disorientation')
        personalityChanges=request.POST.get('personalityChanges')
        difficultyCompletingTasks=request.POST.get('difficultyCompletingTasks')
        forgetfulness=request.POST.get('forgetfulness')
        brain_output=tests.brainpredict(Age,Gender,Ethnicity,Education,BMI,Smoking,Alcohol,Physical_activity,Diet,Sleep,Family_history,CardiovascularDisease,Diabetes,Depression,HeadInjury,Hypertension,SystolicBP,DiastolicBP,CholesterolTotal,CholesterolLDL,CholesterolHDL,CholesterolTriglycerides,MMSE,FunctionalAssessment,Memory_comp,Behaviour,Adl,confusion,disorientation,personalityChanges,difficultyCompletingTasks,forgetfulness)
    context={
        "brain_Result":f"{brain_output}"
    }
    return render(request,'brain.html',context)
