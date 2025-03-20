fraktur_map = {
    "ſ": "s",
    "ẞ": "ß",
}

def transliterate(text):
    for k, v in fraktur_map.items():
        text = text.replace(k, v)
    return text
