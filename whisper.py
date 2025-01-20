import streamlit as st
import whisper
from tempfile import NamedTemporaryFile

# Title of the app
st.title('Transcripter App')

# Load the Whisper model once (outside the app's logic to avoid reloading on every refresh)
@st.cache_resource
def load_model():
    return whisper.load_model('base')

model = load_model()

# File uploader
audio = st.file_uploader('Upload an Audio File', type=['mp3', 'wav', 'm4a'])

if audio:
    # Save the uploaded audio to a temporary file
    with NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(audio.read())
        temp_audio.flush()

        # Notify user that processing is happening
        with st.spinner('Transcribing your audio...'):
            transcription = model.transcribe(temp_audio.name)
            st.markdown("### Transcription:")
            st.markdown(transcription['text'])

