import streamlit as st
from translator import translate_text
from tts import text_to_speech
from styles import apply_styles

# Set page configuration
st.set_page_config(page_title="Text to Telugu TTS", page_icon="🔊")

# Apply the inline CSS styles
apply_styles()

# Streamlit UI
st.title("Text to Speech")

# Input text
src_text = st.text_area("Enter the text to translate:", "")

# Convert text and generate speech
if st.button("Convert"):
    if src_text:
        # Translate text
        translated_text = translate_text(src_text)

        st.write(f"**Translated Text:** {translated_text}")

        # Convert to speech
        audio_file = text_to_speech(translated_text, lang='te')
        if audio_file:
            st.audio(audio_file, format="audio/mp3")
        else:
            st.error("Failed to convert text to speech.")
    else:
        st.error("Please enter some text.")