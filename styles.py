import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
            body {
                background-color: #121212; /* Dark background */
                color: #ffffff; /* White text */
            }

            h1 {
                color: #F01D0B /* Blue color for heading */
            }

            textarea {
                background-color: #1e1e1e; /* Darker text area */
                color: #F7EAF1; /* White text */
                border: 1px solid #ffcc00; /* Yellow border */
                border-radius: 5px; /* Rounded corners */
                padding: 10px; /* Inner padding */
                width: 100%; /* Full width */
                resize: none; /* Disable resizing */
            }

            button {
                background-color: #ff9999; /* Light red button */
                color: #931D29; /* Dark text on button */
                border: none; /* No border */
                border-radius: 5px; /* Rounded corners */
                padding: 10px 20px; /* Padding */
                cursor: pointer; /* Pointer cursor */
                transition: background-color 0.3s; /* Smooth transition */
            }

            button:hover {
                background-color: #ff6666; /* Darker red on hover */
            }

            audio {
                margin-top: 20px; /* Margin for audio player */
            }
        </style>
    """, unsafe_allow_html=True)
