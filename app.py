import streamlit as st
import whisper
st.title('Transcripter App')
audio=st.file_uploader('Upload Audio File')
if audio:
  model = whisper.load_model('base')
  t=model.transcribe(audio)
  st.markdown(t['text'])
