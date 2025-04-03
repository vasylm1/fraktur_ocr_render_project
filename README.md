Fraktur OCR – Streamlit App (Render.com + Docker + Tesseract OCR)

📝 An online OCR application for recognizing German blackletter script (Fraktur, Schwabacher, Antiqua) based on Streamlit, Docker, and Tesseract OCR.

🔥 How to launch on Render.com:
	1.	Go to https://render.com
	2.	Sign in or create a free account
	3.	Click New Web Service
	4.	Choose Deploy from GitHub repo OR Upload repo ZIP as your own project
	5.	Render will detect the Dockerfile and automatically build the app
	6.	Once built, you’ll get a working link (e.g., https://fraktur-ocr.onrender.com)

📁 Repository contents:
	•	app.py – Streamlit frontend
	•	fraktur_reader/ – OCR code + transliteration
	•	Dockerfile – environment with Tesseract
	•	requirements.txt – Python dependencies
