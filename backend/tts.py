from gtts import gTTS
import uuid

def speak(text):
    file = f"static/{uuid.uuid4()}.mp3"
    lang = 'hi' if any(ch in text for ch in 'अआइईउऊएऐओऔ') else 'en'
    tts = gTTS(text=text, lang=lang)
    tts.save(file)
    return file
