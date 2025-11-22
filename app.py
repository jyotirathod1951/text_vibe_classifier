import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from crew.orchestrator import Orchestrator

st.set_page_config(page_title="Text Vibe Classifier", layout="wide")
st.title("🎯 Text Vibe Classifier — Multi-Agent System")

if "orch" not in st.session_state:
    st.session_state.orch = Orchestrator()
orch = st.session_state.orch

with st.sidebar:
    st.header("Settings")
    add_reset = st.button("Clear analysis history")
    if add_reset:
        orch.reset_context()
        st.experimental_rerun()

text_input = st.text_area("Enter your message here:")

if st.button("Analyze Vibe"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        result = orch.analyze_text(text_input)
        st.markdown("### Results")
        st.write(f"**Keywords Detected:** {', '.join(result['keywords']) or 'None'}")
        st.write(f"**Vibe:** {result['vibe']}")
        st.write(f"**Summary:** {result['summary']}")

if len(orch.context.items) > 0:
    st.markdown("---")
    st.subheader("History")
    for i, entry in enumerate(reversed(orch.context.get_history())):
        st.write(f"{i+1}. {entry['summary']}")
