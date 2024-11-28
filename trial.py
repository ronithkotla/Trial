import streamlit as st
import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Streamlit file uploader for audio file input
audio_file = st.audio_input("Record")

if audio_file is not None:
    # Save uploaded audio file
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.getbuffer())

    # Recognize speech from audio file
    with sr.AudioFile("temp_audio.wav") as source:
        audio_data = recognizer.record(source)
        try:
            # Use Google Web Speech API to convert speech to text
            text = recognizer.recognize_google(audio_data)
            st.write("Transcription: ", text)
        except sr.UnknownValueError:
            st.error("Could not understand the audio.")
        except sr.RequestError:
            st.error("Could not request results from Google Speech Recognition service.")
