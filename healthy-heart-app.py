import streamlit as st
import base64
import sklearn
import numpy as np
import pickle as pkl
from sklearn.preprocessing import MinMaxScaler
scal=MinMaxScaler()
#Load the saved model
model=pkl.load(open("final_model.p","rb"))

#Title Page
st.set_page_config(page_title="Heart Disease Prediction App",page_icon="⚕️",layout="centered",initial_sidebar_state="expanded")

#function
def preprocess(age,sex,chestpain,restbp,choles,fastbs,restecg,maxhr,exagina,oldpeak,stslope):   
 
    # Pre-processing user input   
    
    #SEX
    if sex=="Male":
        sex=1 
    else: 
        sex=0
    
    #CHEST PAIN
    if chestpain=="Typical Angina":
        chestpain=0
    elif chestpain=="Atypical Angina":
        chestpain=1
    elif chestpain=="Non-Anginal Pain":
        chestpain=2
    elif chestpain=="Asymptomatic":
        chestpain=3
    
    #EXERCISE AGINE
    if exagina=="Yes":
        exagina=1
    elif exagina=="No":
        exagina=0
 
    #FASTING BLOOD SUGAR
    if fastbs=="Yes":
        fastbs=1
    elif fastbs=="No":
        fastbs=0
 
    #ST SLOPE
    if stslope=="Upsloping: better heart rate with excercise(uncommon)":
        stslope=0
    elif stslope=="Flatsloping: minimal change(typical healthy heart)":
          stslope=1
    elif stslope=="Downsloping: signs of unhealthy heart":
        stslope=2  

    #RESTING ECG
    if restecg=="Nothing to note":
        restecg=0
    elif restecg=="ST-T Wave abnormality":
        restecg=1
    elif restecg=="Possible or definite left ventricular hypertrophy":
        restecg=2


    user_input=[age,sex,chestpain,restbp,choles,fastbs,restecg,maxhr,exagina,oldpeak,stslope]
    user_input=np.array(user_input)
    user_input=user_input.reshape(1,-1)
    #user_input=scal.fit_transform(user_input) # training data
    prediction = model.predict(user_input) 

    return prediction

    

       
    # front end elements of the web page 
html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Healthy Heart App</h1> 
    </div> 
    """
    
    # Display front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
st.subheader('by TARC Liaw Jing Shiong & Phoon Wen Hao ')
      
      
    # following lines create boxes in which user can enter data required to make prediction
    
    # Age (Drop Down)
age=st.selectbox ("Age",range(1,101,1))
    
    # Gender (Radio Button)
sex = st.radio("Select Gender: ", ('Male', 'Female'))
    
    # CHEST PAIN (Drop Down)
chestpain = st.selectbox('Chest Pain Type',("Typical Angina","Atypical Angina","Non-Anginal Pain","Asymptomatic")) 
    
    # RESTING BLOOD PRESSURE (Drop Down)
restbp = st.selectbox('Resting Blood Sugar',range(1,500,1))
    
    #CHOLESTEROL (Drop Down)
choles = st.selectbox('Serum Cholestoral in mg/dl',range(1,1000,1))
    
    # FASTING BLOOD SUGAR (Radio Button)
fastbs = st.radio("Fasting Blood Sugar higher than 120 mg/dl", ['Yes','No'])
    
    # RESTING ECG (Drop Down)
restecg = st.selectbox('Resting Electrocardiographic Results',("Nothing to note","ST-T Wave abnormality","Possible or definite left ventricular hypertrophy"))
    
    # MAXIMUM HEART RATE (Drop Down)
maxhr = st.selectbox('Maximum Heart Rate Achieved',range(1,300,1))
    
    # EXERCISE ANGINA (Drop Down)
exagina = st.selectbox('Exercise Induced Angina',["Yes","No"])
    
    # OLD PEAK (INPUT BOX)
oldpeak = st.number_input('Oldpeak')
    
    # ST SLOPE (Drop Down)
stslope = st.selectbox('Heart Rate Slope',("Upsloping: better heart rate with excercise(uncommon)","Flatsloping: minimal change(typical healthy heart)","Downsloping: signs of unhealthy heart"))

#user_input=preprocess(sex,cp,exang, fbs, slope, thal )
pred = preprocess(age,sex,chestpain,restbp,choles,fastbs,restecg,maxhr,exagina,oldpeak,stslope)
    

if st.button("Predict"):
    
    if pred[0] == 0:
        st.success('You have lower risk of getting a heart disease!')
    else:
        st.error('Warning! You have high risk of getting a heart attack!')
    
    # FEEDBACK
st.sidebar.subheader("About App")

st.sidebar.info("This web app is helps you to find out whether you are at a risk of developing a heart disease.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check whether you have a healthy heart")
st.sidebar.info("Don't forget to rate this app")

feedback = st.sidebar.slider('How muchh would you rate this app?',min_value=0,max_value=5,step=1)

if feedback:
    st.header("Thank you for rating the app!")
    st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.") 


     
