# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import base64

from streamlit_option_menu import option_menu

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown



st.set_page_config(
        page_icon="https://www.svgrepo.com/show/390209/bug-insect-code-development.svg",
        page_title="Code Debugger | app",
        layout="wide"
        
            )






genai.configure(api_key="AIzaSyBX9BFeAk8HcMmWSuhh0xR_4CnrtEGrHok")




model = genai.GenerativeModel('gemini-pro')




def generate_code_assistance(code_snippet):
    prompt = f"""
    You are given the following programming code:

    {code_snippet}

    Your task is to:
    1. Review the provided code and add comments to explain each part.
    2. Debug the code to identify and fix any errors.
    3. If the code is correct and well-commented, return a message stating that the code is free of errors and already well-commented.
    4. If the code contains errors, provide only the corrected version of the given code, without adding any additional code or functionality.

    Ensure that:
    - Comments are clear and describe the purpose and functionality of each section of the code.
    - Only the issues in the provided code are addressed.
    - The corrected code is functional and error-free, with no additional modifications or code snippets.

    Provide your response in the following structure:

    **Original Code with Comments:**
    [Add comments here]

    **Corrected Code:**
    [Provide corrected code here without adding any new code]

    If the code is already correct and commented:
    - Provide a message: "The code is correct and well-commented. No changes are necessary."

    """
    response = model.generate_content(prompt)
    return response




     
     
# CSS styling for the Streamlit app
page_bg_img = f"""
<style>
[data-testid="stSidebar"] > div:first-child {{
    background-repeat: no-repeat;
    background-attachment: fixed;
    background: rgb(18 18 18 / 0%);
}}

.st-emotion-cache-1gv3huu {{
    position: relative;
    top: 2px;
    background-color: #000;
    z-index: 999991;
    min-width: 244px;
    max-width: 550px;
    transform: none;
    transition: transform 300ms, min-width 300ms, max-width 300ms;
}}

.st-emotion-cache-1jicfl2 {{
    width: 100%;
    padding: 4rem 1rem 4rem;
    min-width: auto;
    max-width: initial;

}}


.st-emotion-cache-4uzi61 {{
    border: 1px solid rgba(49, 51, 63, 0.2);
    border-radius: 0.5rem;
    padding: calc(-1px + 1rem);
    background: rgb(240 242 246);
    box-shadow: 0 5px 8px #6c757d;
}}

.st-emotion-cache-1vt4y43 {{
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    user-select: none;
    background-color: #ffc107;
    border: 1px solid rgba(49, 51, 63, 0.2);
}}

.st-emotion-cache-qcpnpn {{
    border: 1px solid rgb(163, 168, 184);
    border-radius: 0.5rem;
    padding: calc(-1px + 1rem);
    background-color: rgb(38, 39, 48);
    MARGIN-TOP: 9PX;
    box-shadow: 0 5px 8px #6c757d;
}}


.st-emotion-cache-15hul6a {{
    user-select: none;
    background-color: #ffc107;
    border: 1px solid rgba(250, 250, 250, 0.2);
    
}}

.st-emotion-cache-1hskohh {{
    margin: 0px;
    padding-right: 2.75rem;
    color: rgb(250, 250, 250);
    border-radius: 0.5rem;
    background: #000;
}}

.st-emotion-cache-12pd2es {{
    margin: 0px;
    padding-right: 2.75rem;
    color: #f0f2f6;
    border-radius: 0.5rem;
    background: #000;
}}
</style>
"""

# Apply CSS styling to the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    # Display logo image
    st.image("code Debuging project/Logo3.png", use_column_width=True)

    # Adding a custom style with HTML and CSS for sidebar
    st.markdown("""
        <style>
            .custom-text {
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                color:#ffc107
            }
            .custom-text span {
                color: #04ECF0; /* Color for the word 'Recommendation' */
            }
        </style>
    """, unsafe_allow_html=True)
    
 
    # Displaying the subheader with custom styling
    st.markdown('<p class="custom-text">Code  <span>Debugging</span> App</p>', unsafe_allow_html=True)

    # HTML and CSS for the GitHub button
    github_button_html = """
    <div style="text-align: center; margin-top: 50px;">
        <a class="button" href="https://github.com/Salman7292" target="_blank" rel="noopener noreferrer">Visit my GitHub</a>
    </div>

    <style>
        /* Button styles */
        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #ffc107;
            color: black;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #000345;
            color: white;
            text-decoration: none; /* Remove underline on hover */
        }
    </style>
    """

    # Display the GitHub button in the sidebar
    st.markdown(github_button_html, unsafe_allow_html=True)
    
    # Footer HTML and CSS
    footer_html = """
    <div style="padding:10px; text-align:center;margin-top: 10px;">
        <p style="font-size:20px; color:#ffffff;">Made with ❤️ by Salman Malik</p>
    </div>
    """

    # Display footer in the sidebar
    st.markdown(footer_html, unsafe_allow_html=True)



# Define the option menu for navigation
selections = option_menu(
    menu_title=None,  # No title for the menu
    options=['Home', "Debug Your Code"],  # Options for the menu
    icons=['house-fill', " bi-code"],  # Icons for the options
    menu_icon="cast",  # Optional: Change the menu icon
    default_index=0,  # Optional: Set the default selected option
    orientation='horizontal',  # Set the menu orientation to horizontal
    styles={  # Define custom styles for the menu
        "container": {
            "padding": "5px 23px",
            "background-color": "#0d6efd",  # Background color (dark grey)
            "border-radius": "8px",
            "box-shadow": "0px 4px 10px rgba(0, 0, 0, 0.25)"
        },
        "icon": {"color": "#f9fafb", "font-size": "18px"},  # Style for the icons (light grey)
        "hr": {"color": "#0d6dfdbe"},  # Style for the horizontal line (very light grey)
        "nav-link": {
            "color": "#f9fafb",  # Light grey text color
            "font-size": "15px",
            "text-align": "center",
            "margin": "0 10px",  # Adds space between the buttons
            "--hover-color": "#0761e97e",  # Slightly lighter grey for hover
            "padding": "10px 10px",
            "border-radius": "16px"

        },
        "nav-link-selected": {"background-color": "#ffc107","font-size": "12px",},  # Green background for selected option
    }
)



if selections=="Home":
      # Define HTML and CSS for the hero section
        code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Streamlit App Description</title>
    <style>
        .hero-section {
        background-color: #ffffff /* Set your background color */
        padding: 80px 20px; /* Adjust padding as needed */
        text-align: center;
        font-family: Arial, sans-serif;
        }
        .hero-heading {
            font-size: 2.5rem;
            margin-bottom: 20px;
            color: #333;
            font-family: 'Roboto', sans-serif;
            font-weight: 700;
            margin-top: 29px;
        }
        .hero-text {
        font-size: 1.2rem;
        line-height: 1.6;
        color: #666; /* Set your text color */
        max-width: 900px;
        margin: 0 auto;
        }
 
        
    </style>
    </head>
    <body>

    <section class="hero-section">
    <div class="container">
        <h1 class="hero-heading">Streamline Your Coding with Advanced Debugging</span> Analytics</h1>
        <p class="hero-text">
       Elevate your coding efficiency with our powerful Streamlit app designed for seamless code debugging. Effortlessly paste your code snippets into our tool, and let it automatically detect errors, offer intelligent corrections, and enhance your code quality. Whether you’re tackling syntax issues, refining logic, or optimizing performance, our app simplifies the debugging process with real-time feedback and actionable insights. Make coding errors a thing of the past and transform your development workflow with our user-friendly and interactive debugging assistant.
        </p>
    </div>
    </section>

    </body>
    </html>
    """
    # Display the hero section using markdown
        st.markdown(code, unsafe_allow_html=True)

elif selections=="Debug Your Code":

     st.markdown(
            """
            <h1 style='text-align: center;'> Debug Your code Here</h1>
            """,
            unsafe_allow_html=True
            )

     st.markdown(
                """
                <hr style="border: none; height: 2px;width: 50%; background: linear-gradient(90deg, rgba(216,82,82,1) 13%, rgba(237,242,6,1) 57%, rgba(226,0,255,1) 93%); margin: 0 auto;" />
                """,
                unsafe_allow_html=True
            )
     

     form=st.form("insert your code")
     # Create a text area with various options
     user_input_code = form.text_area(
        label="Insert your Code",
        value="",
        height=200,
        max_chars=2000,
        placeholder="Type your Code here.",
        key="feedback"
    )
     
     submit=form.form_submit_button("Debug")

     if submit:
        st.markdown(
            """
            <h1 style='text-align: center;'>Corrected code</h1>
            """,
            unsafe_allow_html=True
            )

        st.markdown(
                """
                <hr style="border: none; height: 2px;width: 50%; background: linear-gradient(90deg, rgba(216,82,82,1) 13%, rgba(237,242,6,1) 57%, rgba(226,0,255,1) 93%); margin: 0 auto;" />
                """,
                unsafe_allow_html=True
            )
        # st.write(user_input_code)

        result=generate_code_assistance(user_input_code)
        st.markdown(result.text)
        # Markdown(result.text)


