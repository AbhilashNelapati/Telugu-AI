from gtts import gTTS
from pydub import AudioSegment
import io


def translate_time_to_telugu(time_str):
    # Example: "6:30 am" -> "6:30 ఉదయం"
    hours, minutes = time_str.split(':')
    period = "ఉదయం" if "am" in time_str else "సాయంత్రం" in "pm"
    return f"{hours}:{minutes} {period}"

def text_to_speech(text, lang='te'):
    try:
        # Replace the time with its Telugu equivalent
        time_in_english = "6:30 am"  # You can make this dynamic if needed
        time_in_telugu = translate_time_to_telugu(time_in_english)
        text = text.replace(time_in_english, time_in_telugu)
        
        # Split the text into sentences to prevent repeating issues
        sentences = text.split('. ')
        combined_audio = AudioSegment.empty()

        for sentence in sentences:
            if sentence.strip():  # Ensure the sentence is not empty
                tts = gTTS(text=sentence.strip(), lang=lang)
                audio_file = io.BytesIO()
                tts.write_to_fp(audio_file)
                audio_file.seek(0)
                
                # Load the audio file into pydub
                audio_segment = AudioSegment.from_file(audio_file, format="mp3")
                
                # Optionally, enhance the audio quality (e.g., by changing the frame rate)
                enhanced_audio_segment = audio_segment.set_frame_rate(44100)
                
                # Append each sentence audio to the combined_audio
                combined_audio += enhanced_audio_segment

        # Save the combined audio to another BytesIO object
        enhanced_audio_file = io.BytesIO()
        combined_audio.export(enhanced_audio_file, format="mp3")
        enhanced_audio_file.seek(0)
        
        return enhanced_audio_file
    
    except Exception as e:
        raise ValueError(f"Error in text_to_speech: {e}")




"""
def text_to_speech(text, lang='en'):
    try:
        # Split the text into sentences to prevent repeating issues
        sentences = text.split('. ')
        combined_audio = AudioSegment.empty()

        for sentence in sentences:
            if sentence.strip():  # Ensure the sentence is not empty
                tts = gTTS(text=sentence.strip(), lang=lang)
                audio_file = io.BytesIO()
                tts.write_to_fp(audio_file)
                audio_file.seek(0)
                
                # Load the audio file into pydub
                audio_segment = AudioSegment.from_file(audio_file, format="mp3")
                
                # Optionally, enhance the audio quality (e.g., by changing the frame rate)
                enhanced_audio_segment = audio_segment.set_frame_rate(44100)
                
                # Append each sentence audio to the combined_audio
                combined_audio += enhanced_audio_segment

        # Save the combined audio to another BytesIO object
        enhanced_audio_file = io.BytesIO()
        combined_audio.export(enhanced_audio_file, format="mp3")
        enhanced_audio_file.seek(0)
        
        return enhanced_audio_file
    
    except Exception as e:
        raise ValueError(f"Error in text_to_speech: {e}")

"""
