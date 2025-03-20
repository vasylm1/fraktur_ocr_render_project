# Fraktur OCR – Streamlit App (Render.com + Docker + Tesseract OCR)

📝 Aplikacja OCR online do rozpoznawania niemieckiego pisma gotyckiego (Fraktur, Schwabacha, Antiqua) oparta na Streamlit, Docker i Tesseract OCR.

## 🔥 Jak uruchomić na Render.com:

1. Wejdź na https://render.com
2. Zaloguj się lub utwórz darmowe konto
3. Kliknij **New Web Service**
4. Wybierz opcję **Deploy from GitHub repo** LUB **Upload repo ZIP jako własny projekt**
5. Render wykryje `Dockerfile` i zbuduje aplikację automatycznie
6. Po zbudowaniu otrzymasz działający link (np. `https://fraktur-ocr.onrender.com`)

## 📁 Zawartość repozytorium:
- `app.py` – frontend Streamlit
- `fraktur_reader/` – kod OCR + transliteracja
- `Dockerfile` – środowisko z Tesseractem
- `requirements.txt` – zależności Python
