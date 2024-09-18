# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:45:12 2024

@author: rampr
"""
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os


st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f5dc;
    }
    </style>
    """,
    unsafe_allow_html=True
)




# Load environment variables from a .env file
load_dotenv()

# Configure Google Gemini API with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to generate a response from the Gemini model
def generate_gemini_response(prompt):
    try:
        # Use the Gemini model for generating text
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
       
            
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit application layout
def app():
    st.title("Gemini AI Chatbot 🌟")
    st.write("Ask any question and get a response from the Gemini model!")

    # Input text box
    user_prompt = st.text_input("Enter your prompt or question:", "")

    # Button to submit the request
    if st.button("Get Response"):
        with st.spinner("Generating response..."):
            if user_prompt:
                # Generate the response from the Gemini model
                response = generate_gemini_response(user_prompt)
                # Display the response
                st.success("Response from Gemini Model:")
                st.write(response)
            else:
                st.warning("Please enter a prompt before submitting.")

if __name__ == "__main__":
    app()

