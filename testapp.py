'''

Joti Gokaraju
Computer Science 20
Period 5, Mr. Schellenberg
Temperature Converter
Purpose: To Build a Streamlit App That Converts Celsius, Kelvin, and Farenheit to Each Other

'''

#Import Streamlit
import streamlit as st

#Headers
st.title("Temperature Convertor App")
st.header("*By Joti Gokaraju*")
st.divider()

#Conversion Function. Takes Variables and Determines How to Convert Accordingly. Returns Calculated Result Value
def convert(start_type, start_temp, conversion_type):

    #Celsius Conversions
    if start_type == "Celsius":
        if conversion_type == "Celsius":
            return start_temp
        elif conversion_type == "Farenheit":
            return (start_temp*(9/5))+32
        else:
            return start_temp+273.15

    #Farenheit Conversions
    elif start_type == "Farenheit":
        if conversion_type == "Celsius":
            return (start_temp-32)*5/9
        elif conversion_type == "Farenheit":
            return start_temp
        else:
            return ((start_temp-32)*5/9)+273.15
            
    #Kelvin Conversions
    else:
        if conversion_type == "Celsius":
            return start_temp-273.15
        elif conversion_type == "Farenheit":
            return ((start_temp-273.15)*(9/5))+32
        else:
            return start_temp

#User Input Variables 
#Selectbox Variable to Determine Starting Temperature
start_type = st.selectbox(
    "What is the Starting Temperature Unit?",
   ("Celsius", "Farenheit", "Kelvin"),
   index=None,
   placeholder="Select Starting Temperature...")
st.write("You Selected:", start_type)

#User Inputs the Temperature Value They Want Converted
start_temp = st.number_input("What is the Current Temperature?", value=None, placeholder="Type the Starting Temperature...")
st.write("You Entered:", start_temp)

#Selectbox Variable to Determine Conversion Temperature
conversion_type = st.selectbox(
   "What is the Conversion Temperature Unit?",
   ("Celsius", "Farenheit", "Kelvin"),
   index=None,
   placeholder="Select Conversion Temperature...")
st.write('You Selected:', conversion_type)

#Divider
st.divider()

#Button to Intitiate Conversion
if st.button("Convert!", type="primary"):
    
    #Run The Variables Through the Conversion Function
    converted_temp = convert(start_type, start_temp, conversion_type)
    
    #Divider
    st.divider()
    
    #Print Results
    st.write(start_temp, "Degrees", start_type, "is", converted_temp, "Degrees", conversion_type)

    


    
    

    
