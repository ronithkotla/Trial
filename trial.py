import streamlit as st
import whisper
import tempfile

# Load the Whisper model
model = whisper.load_model("small", device="cpu")

audio_file = st.audio_input("Record")

if audio_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(audio_file.getvalue())  # Save uploaded file content
        tmp_file_path = tmp_file.name  # Path to temporary file
    
    # Transcribe using Whisper
    result = model.transcribe(tmp_file_path)
    
    st.write("Transcription:")
    st.text(result["text"])
