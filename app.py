import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from database.db import init_db

st.set_page_config(
    page_title="PromptVault",
    page_icon="🧠",
    layout="wide"
)

init_db()

import importlib.util

def load_view(filepath):
    spec = importlib.util.spec_from_file_location("module", filepath)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

BASE = os.path.dirname(__file__)

st.sidebar.title("🧠 PromptVault")
st.sidebar.markdown("*Your Personal Prompt Library*")
st.sidebar.divider()

page = st.sidebar.radio("Navigate", [
    "📊 Dashboard",
    "➕ Add Prompt",
    "📚 View Prompts",
    "📈 Analytics"
])

st.sidebar.divider()
st.sidebar.caption("Built with Streamlit + SQLite")

if page == "📊 Dashboard":
    load_view(os.path.join(BASE, "views", "dashboard.py")).show()
elif page == "➕ Add Prompt":
    load_view(os.path.join(BASE, "views", "add_prompt.py")).show()
elif page == "📚 View Prompts":
    load_view(os.path.join(BASE, "views", "view_prompts.py")).show()
elif page == "📈 Analytics":
    load_view(os.path.join(BASE, "views", "analytics.py")).show()

    