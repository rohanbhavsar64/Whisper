import streamlit as st
import whisper
st.title('Transcripter App')
audio=st.file_uploader('Upload Audio File')
model = whisper.load_model('base')
if audio:
  t=model.transcribe(audio)
  st.markdown(t['text'])
