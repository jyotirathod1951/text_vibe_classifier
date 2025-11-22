class SummaryAgent:
    def __init__(self):
        pass

    def generate_summary(self, text: str, keywords: list, vibe: str):
        if not keywords:
            keywords_str = "none detected"
        else:
            keywords_str = ", ".join(keywords)
        summary = f"Your message contains keywords: {keywords_str}. Overall vibe: {vibe}."
        return summary
