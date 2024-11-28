import streamlit as st
import whisper

# Load the Whisper model (small, medium, large)
model = whisper.load_model("small",device="cpu")

# Audio file uploader
audio_file = st.audio_input("Record")

if audio_file:
    # Save the uploaded audio file to a temporary file
    with open("temp_audio.mp3", "wb") as f:
        f.write(audio_file.getbuffer())
    
    # Perform speech-to-text using Whisper
    result = model.transcribe("temp_audio.mp3")

    # Display the transcribed text
    st.write("Transcription:")
    st.text(result["text"])

