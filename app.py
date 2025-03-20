import streamlit as st
from fraktur_reader.ocr_engine import extract_text
from fraktur_reader.transliterator import transliterate

st.set_page_config(page_title="Fraktur OCR Web App", layout="wide")
st.title("📝 Fraktur OCR")

model = st.selectbox("Wybierz model OCR:", ["deu"])
uploaded_file = st.file_uploader("Wgraj obraz (PNG, JPG, JPEG, BMP)", type=['png', 'jpg', 'jpeg', 'bmp'])

if uploaded_file:
    with open("uploaded_image.png", "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ Plik wgrany. Rozpoczynam OCR...")
    text = extract_text("uploaded_image.png", model)
    clean_text = transliterate(text)
    st.text_area("Rozpoznany tekst:", clean_text, height=400)
