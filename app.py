import streamlit as st
import pandas as pd 
from streamlit_option_menu import option_menu
from PIL import Image
import seaborn as sns
import base64
import pickle
import numpy as np


with st.sidebar:
    selected=option_menu(
    menu_title="Main Menu",
        options=['Home','Prediction'],
        icons=['house','book','envelope'],
        styles={
            "container":{"background-color":"#EC7063"},
            "nav-link":{
                "font-size":"21px",
                "--hover-color":"#CB4335",
                "color":"317202A"
            },
            "nav-link-selected":{
                "background-color":"#F8F521"
            },
            "icon":{
                "font-size":"20px"
            },
        },
    )

if selected == 'Home':
    st.markdown("""
    <style>
    .big-font1{
    font-size:50px !important;
    color:red;
    text-align:center;
    font-weight:bold;
    
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font1"> WELCOME TO THE BANK CAMPAIGN SYSTEM </p>',unsafe_allow_html=True)
    file_=open("bank1.jpg","rb")
    contents=file_.read()
    data_url=base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="700" image-align="center"  alt="Heart gif">',
        unsafe_allow_html=True, )

    st.markdown("""
    <style>
    . paragraph {
        font-size:20px !important;
        text-align: justify;
        }
    </style>
        """, unsafe_allow_html=True)

    st.markdown(' <p class="paragraph"> Bank marketing campaigns are promotional activities undertaken by banks to attract and retain customers, build brand awareness, and promote their products and services. These campaigns are designed to communicate the banks value proposition, differentiate from competitors, and engage with target audiences </p>',
    unsafe_allow_html=True)



if selected=='Prediction':
    image=Image.open('bank2.jpg')
    
    st.image(image,width=200,use_column_width=True)

    st.markdown("""
    <style>
        .big-font1{
            font-size:50px !important;
            color:red;
            text-align:center;
            font-weight:bold;
    </style>
    """,unsafe_allow_html=True)
    loaded_model=pickle.load(open('model.pkl','rb'))

    def bank_prediction(input_data):
    

        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)

        if (prediction[0] == 0):
            return 'We are Not Going to Target the Customer'
        else:
            return 'This Customer is Targeted'
    def main(): 

    # giving title 
        #st.title('HEART DISEASE PREDICTION SYSTEM')
        st.markdown("<h1 style='text-align: center; color: black;'>BANK CUSTOMER CAMPAIGN SYSTEM</h1>", unsafe_allow_html=True)
        #getting the input data from the user
        co1,col2,col3,col4=st.columns(4)


        with co1:
            day_of_week=st.selectbox('Enter Day of Week mon:1 ,tue:3 , wed:4 , thu:2 , fri:0',(0,1,2,3,4),index=0)
            campaign= st.number_input('number of contacts performed during this campaign',min_value=0)
            marital=st.selectbox('Enter Marital Status as married:1  single: 2  divorced:0  unknown:3',(0,1,2,3),index=0)
            education=st.selectbox('Enter the Education  basic 4y:0  high school:3   basic 6y: 1 basic 9y:2  professional course:5  unknown:7  university degree : 6  illiterate :4',(0,1,2,3,4,5,6,7))
            housing=st.selectbox(' Has housing loan?  no:0    unknown:1   yes:2',(0,1,2))  
            loan=st.selectbox(' Has Personal loan?  no:0    unknown:1   yes:2',(0,1,2))  
        with col2:
            default=st.selectbox(' Has credit in default?  no:0    unknown:1   yes:2',(0,1,2))
            contact=st.selectbox('Contact communication type  telephone:1 cellular:0',(0,1),index=0)
            job=st.selectbox('Job Type  housemaid:3  services:7  admin:0  blue-collar:1  technician:9  retired:5  management:4   unemployed:10  self-employed:6  unknown:11  entrepreneur:2  student:8',(0,1,2,3,4,5,6,7,8,9,10,11))
            age=st.number_input('Enter Age:',min_value=0)
        with col3:
            emp_var_rate=st.number_input('Enter Employement Variance Rate',min_value=0)
            euribor3m=st.number_input('Enter Euribor 3 Months Rate',min_value=0)
            cons_conf_idx=st.number_input('Enter Consumer Confidence Index',min_value=0)
            cons_price_idx=st.number_input('Enter Consumer Price Index',min_value=0)
            duration=st.number_input('Last Contact Duration in Seconds',min_value=0)
            
            

        with col4:
            poutcome=st.selectbox("Outcome of the previous marketing campaign  nonexistent:1    failure:0   success:2'",(0,1,2),index=0)
            previous=st.number_input('Number of contacts performed before',min_value=0)
            pdays=st.number_input('Number of days that passed by after the client was last contacted',min_value=0)
            month=st.selectbox('Enter the last contact month of year  may:6  jun:4  jul:3  aug:1  oct:8  nov:7  dec:2  mar:5  apr:0  sep:9',(0,1,2,3,4,5,6,7,8,9),index=0)
            nr_employed=st.number_input('number of employees',min_value=0)
        
    
        #code for the prediction 
    
        prediction=''
    
    
        #creating a button for prediction 
        if st.button('Bank Campaign Result'):
            prediction = bank_prediction([day_of_week,campaign,marital,education,housing,default,contact,job,age,emp_var_rate,euribor3m,cons_conf_idx,cons_price_idx,duration,poutcome,previous,pdays,month,nr_employed,loan])
            st.success(prediction)
        

    
    if __name__ =='__main__':
        main()
