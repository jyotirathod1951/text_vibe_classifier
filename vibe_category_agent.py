VIBE_MAPPING = {
    "sad": "Sad",
    "happy": "Energetic",
    "calm": "Calm",
    "busy": "Busy",
    "confused": "Confused",
    "neutral": "Neutral"
}

class VibeCategoryAgent:
    def __init__(self):
        self.map = VIBE_MAPPING

    def classify_vibe(self, emotion: str):
        return self.map.get(emotion.lower(), "Neutral")
