import streamlit as st
import whisper
import io
# Load the Whisper model (small, medium, large)
# Audio file uploader
model = whisper.load_model("small",device="cpu")
audio_data = st.audio_input("Record your audio")

if audio_data:
    # Use BytesIO to simulate a file-like object from the audio byte data
    audio_file = io.BytesIO(audio_data)

    # Perform speech-to-text using Whisper
    result = model.transcribe(audio_file)

    # Display the transcribed text
    st.write("Transcription:")
    st.text(result["text"])
