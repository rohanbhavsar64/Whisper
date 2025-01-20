import streamlit as st
st.title('Transcripter App')
audio=st.file_uploader('Upload Audio File')
import whisper
model = whisper.load_model('base')
if audio:
  t=model.transcribe(audio)
  st.markdown(t['text'])
