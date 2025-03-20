from PIL import Image, ImageOps
import pytesseract
import os

def preprocess_image_pillow(image_path):
    img = Image.open(image_path).convert("L")
    img = ImageOps.autocontrast(img)
    return img

def extract_text(image_path, model='deu-frak'):
    img = preprocess_image_pillow(image_path)
    config = f'--oem 1 --psm 6 -l {model}'
    return pytesseract.image_to_string(img, config=config)
