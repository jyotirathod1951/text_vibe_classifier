# Text Vibe Classifier — Multi-Agent System

Detect the vibe of any text message using 3 simple agents: 
Emotion Keyword → Vibe Category → Summary

## Run

1. Create virtual environment:
   python -m venv venv
   .\venv\Scripts\activate    # Windows
   source venv/bin/activate   # Linux/macOS

2. Install packages:
   pip install -r requirements.txt

3. Copy .env.example -> .env and set CREW_API_KEY if available

4. Run Streamlit app:
   streamlit run streamlit_app/app.py
