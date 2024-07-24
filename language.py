import streamlit as st
from gtts import gTTS
import io
import base64

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    buf = io.BytesIO()
    tts.write_to_fp(buf)
    buf.seek(0)
    return buf

def get_audio_download_link(audio_buf, filename='output.mp3'):
    # Convert audio buffer to base64
    audio_base64 = base64.b64encode(audio_buf.read()).decode()
    download_link = f'<a href="data:audio/mp3;base64,{audio_base64}" download="{filename}">Click here to download the audio file</a>'
    return download_link

st.title('Text-to-Speech Converter')

text_input = st.text_area("Enter text:", height=150)
lang = st.selectbox(
    "Choose language:",
    options=[
        ('English', 'en'),
        ('French', 'fr'),
        ('Spanish', 'es'),
        ('German', 'de'),
        ('Italian', 'it'),
        ('Japanese', 'ja'),
        ('Korean', 'ko'),
        ('Chinese', 'zh-CN')
    ],
    format_func=lambda x: x[0]
)

if st.button('Play'):
    if text_input.strip():
        with st.spinner('Generating speech...'):
            audio_buf = text_to_speech(text_input, lang[1])
            st.audio(audio_buf, format='audio/mp3')

            # Provide a download link
            audio_buf.seek(0)  # Rewind the buffer to the beginning
            download_link = get_audio_download_link(audio_buf)
            st.markdown(download_link, unsafe_allow_html=True)
    else:
        st.error("Please enter some text.")
