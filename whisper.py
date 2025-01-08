import streamlit as st
import whisper 
st.title('Transcripter App')
audio=st.file_uploader('Upload Audio File',type=['wav','mp3','m4a','mp4'])
model=whisper.load_model['base']
if st.button('Transcribe'):
  if audio is not None:
    t=model.transcribe(audio.name)
    st.markdown(t['text'])
