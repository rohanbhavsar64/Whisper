import streamlit as st
st.title('Transcripter App')
audio=st.file_uploader('Upload Audio File',type=['wav','mp3','m4a'])
import whisper
model = whisper.load_model('base')
if st.button('Transcribe'):
  if audio is not None:
    t=model.transcribe(audio.name)
    st.markdown(t['text'])
