import re

def clean_text(t):
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def truncate_text(t, max_length=500):
    if len(t) <= max_length:
        return t
    return t[:max_length].rstrip() + "..."
