from crew.tools.text_tools import clean_text

EMOTION_KEYWORDS = {
    "sad": ["sad", "dull", "tired", "down", "low-energy", "gloomy"],
    "happy": ["happy", "joyful", "excited", "cheerful", "energetic"],
    "calm": ["calm", "relaxed", "peaceful", "quiet"],
    "busy": ["busy", "stressed", "overwhelmed", "rushed"],
    "confused": ["confused", "unsure", "puzzled"],
}

class EmotionKeywordAgent:
    def __init__(self):
        self.keywords = EMOTION_KEYWORDS

    def extract_emotion(self, text: str):
        text_clean = clean_text(text.lower())
        found = []
        emotion_detected = "neutral"

        for emo, kw_list in self.keywords.items():
            for kw in kw_list:
                if kw in text_clean:
                    found.append(kw)
                    emotion_detected = emo
        return {"keywords": found, "emotion": emotion_detected}
