# -*- coding: utf-8 -*-

!pip install torch transformers

import torch
from transformers import pipeline

# Path to the uploaded audio file
audio = "/content/Sri Sri dialogue from అకలిరాజ్యం 🖤(MP3_160K).mp3"
# Set the device to "cuda:0" if available, otherwise "cpu
device = "cuda:0" if torch.cuda.is_available() else "cpu"

"""## **Whisper Models**"""

# model_name = "vasista22/whisper-telugu-tiny"
model_name = "vasista22/whisper-telugu-small"
# model_name = "vasista22/whisper-telugu-base"
# model_name = "vasista22/whisper-telugu-medium"
# model_name = "vasista22/whisper-telugu-large-v2"
# model_name = "kowshik/whisper-telugu-medium"
# model_name = "kowshik/whisper-telugu-large-v2"
# model_name = "Mukund017/whisper-small-telugu"
# model_name = "eswardivi/whisper-tiny-fluers_V2_telugu_Augmentation_full_datset_V2_e5"
# model_name = "Anujgr8/Whisper-Anuj-small-Telugu-final"

# Initialize the ASR pipeline
transcribe = pipeline(
    task = "automatic-speech-recognition",
    model = model_name,
    chunk_length_s = 30,
    device = device
)

# Set the forced decoder IDs for Telugu transcription
transcribe.model.config.forced_decoder_ids = transcribe.tokenizer.get_decoder_prompt_ids(language="te", task="transcribe")
# Perform transcription and print the result
print('Transcription: ', transcribe(audio)["text"])

_______________________________________________________________________________________________________________________________________

"""### **Wav2Vec2 Models**"""

!pip install kenlm
!pip install pyctcdecode

# model_name = "henilp105/wav2vec2-large-xls-r-300m-telugu-asr"
# model_name = "anuragshas/wav2vec2-large-xlsr-53-telugu"
# model_name = "Anujgr8/wav2vec2-base-Telugu-large"
# model_name = "Fredium/wav2vec2-large-xlsr-53-demo-colab-telugu_new
# model_name = "Hemantrao/wav2vec2-large-xls-r-300m-hindi_telugu-colab"
# model_name = "Harveenchadha/vakyansh-wav2vec2-telugu-tem-100"
# model_name = "addy88/wav2vec2-telugu-stt"
# model_name = "krishnateja/wav2vec2-telugu"
model_name = "krishnateja/wav2vec2-telugu_150"
# model_name = "henilp105/wav2vec2-base-ASR-telugu"

# Initialize the ASR pipeline
transcribe = pipeline(
    task="automatic-speech-recognition",
    model=model_name,
    chunk_length_s=30,
    device=device
)

# Perform transcription
transcription = transcribe(audio)["text"]

# Remove unwanted tokens
cleaned_transcription = transcription.replace("<s>", "").strip()

# Print the cleaned transcription
print('Transcription: ', cleaned_transcription)



_______________________________________________________________________________________________________________________________________



"""### **Bert Models**"""

# Choose the model to use
# model_name = "Anujgr8/w2v-bert-Telugu-large"
model_name = "cdactvm/telugu_w2v-bert_model"

# Initialize the ASR pipeline
try:
    transcribe = pipeline(
        task="automatic-speech-recognition",
        model=model_name,
        chunk_length_s=30,
        device=device,
    )
except Exception as e:
    print(f"Error initializing pipeline: {e}")
    exit()

# Set the forced decoder IDs if supported by the model
if hasattr(transcribe.model.config, 'forced_decoder_ids') and hasattr(transcribe.tokenizer, 'get_decoder_prompt_ids'):
    transcribe.model.config.forced_decoder_ids = transcribe.tokenizer.get_decoder_prompt_ids(language="te", task="transcribe")

# Perform transcription and print the result
try:
    result = transcribe(audio_path)
    print('Transcription:', result["text"])
except Exception as e:
    print(f"An error occurred during transcription: {e}")
