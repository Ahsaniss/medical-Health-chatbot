import streamlit as st
import google.generativeai as palm

# Configure the Gemini AI Flash API
palm.configure(api_key="AIzaSyAowzpSMHmMLiYehypB6niVYm0L4eTTjRo")

# Custom CSS to enhance the UI
st.markdown("""
    <style>
    .main {
        background-color: #F7F9FC;
        font-family: 'Arial', sans-serif;
        color: #333333;
    }
    .stButton > button {
        background-color: #4A90E2;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        font-size: 16px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #3B7DC4;
    }
    .stTextInput > div > div > input {
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #CCCCCC;
        font-size: 16px;
    }
    .stSelectbox > div {
        padding: 5px 10px;
        border-radius: 5px;
        border: 1px solid #CCCCCC;
        font-size: 16px;
    }
    .stMarkdown {
        margin-top: 20px;
        font-size: 18px;
    }
    h1 {
        color: #2E3B55;
    }
    h3 {
        color: #6C8EBF;
    }
    </style>
""", unsafe_allow_html=True)

# Function to get food recommendations
def get_food_recommendation(user_input):
    prompt = f"Based on the user's health, suggest the best food items like vegetables and other food items. User's health condition: {user_input}"
    response = palm.chat(messages=[{"content": prompt}])
    return response.messages[-1]['content']

# Function to get disease suggestions
def get_disease_suggestion(user_input):
    prompt = f"Based on the following symptoms, suggest what disease this might be. Symptoms: {user_input}. Please note that this is not a professional diagnosis."
    response = palm.chat(messages=[{"content": prompt}])
    return response.messages[-1]['content']

def main():
    st.markdown("<h1 style='text-align: center;'>AI Health Chatbot</h1>", unsafe_allow_html=True)

    st.markdown("""
        <p style='text-align: center;'>
        Welcome to the AI Health Chatbot! This chatbot can suggest food items according to your health 
        or offer possible diseases based on your symptoms.
        </p>
    """, unsafe_allow_html=True)

    option = st.selectbox("What would you like to do?", ("Get Food Recommendations", "Get Disease Suggestions"))

    user_input = st.text_input("Describe your health condition or symptoms:")

    if st.button("Get Suggestion"):
        if user_input:
            if option == "Get Food Recommendations":
                recommendation = get_food_recommendation(user_input)
                st.markdown("<h3>Recommended Food Items</h3>", unsafe_allow_html=True)
            else:
                recommendation = get_disease_suggestion(user_input)
                st.markdown("<h3>Possible Disease(s)</h3>", unsafe_allow_html=True)
            st.write(recommendation)
        else:
            st.error("Please enter your health condition or symptoms to get a suggestion.")

if __name__ == "__main__":
    main()
