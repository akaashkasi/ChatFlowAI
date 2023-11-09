# styles.py
import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        .css-18e3th9 {
            background-color: #fafafa; /* Main background color */
            color: #333333; /* Main text color */
        }
        .stTextInput > label {
            color: #4f8bf9; /* Color of the input labels */
        }
        .stButton > button {
            color: #ffffff;
            background-color: #4f8bf9; /* Color of buttons */
            border-radius: 10px; /* Rounded corners for buttons */
            border: none;
        }
        .stTextArea > label {
            color: #4f8bf9; /* Color of the textarea labels */
        }
        .css-1d391kg {
            padding-top: 10px; /* Space above the chat text area */
            padding-bottom: 10px; /* Space below the chat text area */
        }
        </style>
    """, unsafe_allow_html=True)
