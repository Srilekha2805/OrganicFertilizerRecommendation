# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import pickle


loaded_model=pickle.load(open(r"C:\Users\murali\Downloads\FinalProject\trained_model.sav",'rb'))

#Formats the loaded model and gives the result back
def dataprocessing(inputdata):
    dict1={ "CropType":{"Barley":1,"Cotton":2,"Ground Nuts":3,"Maize":4,"Millets":5,"Oil seeds":6,"Paddy":7,"Pulses":8,"Sugarcane":9,"Wheat":10}}
    dict2={"SoilType":{"Black":1,"Clayey":2,"Loamy":3,"Red":4,"Sandy":5}}
    inputdata.replace(dict1,inplace=True)
    inputdata.replace(dict2,inplace=True)
    
    output=loaded_model.predict(inputdata)
    return output
    
    
def main():
       
    st.title("ORG-F Recommendation App")
    Temparature=st.text_input("Enter temperature")
    Humidity=st.text_input("Humidity")
    Moisture=st.text_input("Current Moisture content")
    SoilType=st.text_input("Soil Type")
    CropType=st.text_input("Crop Type")
    Nitrogen=st.text_input("Nitrogen content")
    Potassium=st.text_input("Potassium content")
    Phosphorous=st.text_input("Phosphorous")
    
    df1 = pd.DataFrame(data=[[Temparature,Humidity,Moisture,SoilType,CropType,Nitrogen,
                              Potassium,Phosphorous]],
                       columns=["Temparature", "Humidity", "Moisture","SoilType", 
                                "CropType", "Nitrogen","Potassium","Phosphorous"])
    result = ""
    nextcrop = ""
    
    if (st.button('Predict')):
        outputset=dataprocessing(df1)[0]
        result += outputset[0] 
        nextcrop +=outputset[1]
        st.success("Suitable organic fertilizer:" +result+"  \n Crop rotation choice:"+nextcrop)
    


if __name__ == '__main__':
    main()
