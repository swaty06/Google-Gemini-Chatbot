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
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    st.success("✅ API Key loaded successfully!")
else:
    st.error("❌ GOOGLE_API_KEY not found in environment variables!")

# DEBUG SECTION - Remove this after fixing
st.subheader("🔍 Debug: Available Models")
try:
    available_models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available_models.append(m.name)
            st.write(f"✓ {m.name}")
    
    if not available_models:
        st.warning("No models found that support generateContent")
except Exception as e:
    st.error(f"Error listing models: {e}")

st.divider()
# END DEBUG SECTION

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
