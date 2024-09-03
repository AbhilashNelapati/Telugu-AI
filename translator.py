"""from transformers import pipeline

def translate_text(text, target_language):
    models = {
        "Telugu": "facebook/mms-tts-tel",
        "Hindi": "Helsinki-NLP/opus-mt-en-hi",
        "English": "Helsinki-NLP/opus-mt-en-en",
        "Tamil": "Helsinki-NLP/opus-mt-en-ta",
    }

    model_name = models.get(target_language, "Helsinki-NLP/opus-mt-en-en")

    try:
        translator = pipeline("translation", model=model_name)
        translated = translator(text)
        return translated[0]['translation_text']
    except Exception as e:
        raise RuntimeError(f"An error occurred during translation: {e}")
"""
"""from transformers import pipeline

# Define the translation function
def translate_text(text, target_language):
    # Map target languages to their corresponding models
    models = {
        "Telugu": "Helsinki-NLP/opus-mt-en-te",
        "Hindi": "Helsinki-NLP/opus-mt-en-hi",
        "English": "Helsinki-NLP/opus-mt-en-en",
        "Tamil": "Helsinki-NLP/opus-mt-en-ta",
    }
    
    # Default to English if language is not in the list
    model_name = models.get(target_language, "Helsinki-NLP/opus-mt-en-en")
    
    # Initialize the translator pipeline
    translator = pipeline("translation", model=model_name)
    
    # Translate the text
    translated = translator(text)
    
    return translated[0]['translation_text']
"""


from googletrans import Translator

# Initialize the Google Translate API translator
translator = Translator()

def translate_text(text, src='en', dest='te'):
    try:
        # Translate text
        translation = translator.translate(text, src=src, dest=dest)
        return translation.text
    except Exception as e:
        raise ValueError(f"Translation error: {e}")
