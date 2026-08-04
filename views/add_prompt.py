import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.helpers import add_prompt as save_prompt

def show():
    st.title("➕ Add New Prompt")

    with st.form("add_form", clear_on_submit=True):
        title      = st.text_input("Prompt Title *")
        col1, col2 = st.columns(2)

        with col1:
            category = st.selectbox("Category", [
                "Study", "Coding", "Research", "Resume", "Productivity"
            ])
        with col2:
            difficulty = st.selectbox("Difficulty", [
                "Beginner", "Intermediate", "Advanced"
            ])

        tags        = st.text_input("Tags (comma separated)", placeholder="python, debugging, AI")

        st.markdown("#### 📐 Prompt Framework")
        role        = st.text_area("Role",          placeholder="e.g. Senior Python Engineer")
        goal        = st.text_area("Goal",          placeholder="e.g. Find and fix bugs in my code")
        context     = st.text_area("Context",       placeholder="e.g. Flask web app, Python 3.11")
        prompt_text = st.text_area("Prompt Text *", placeholder="Write your full prompt here...", height=150)
        output_fmt  = st.text_area("Output Format", placeholder="e.g. Return corrected code with comments")

        submitted = st.form_submit_button("💾 Save Prompt", use_container_width=True)

        if submitted:
            if not title or not prompt_text:
                st.error("Title and Prompt Text are required.")
            else:
                save_prompt(title, category, difficulty, tags,
                            role, goal, context, prompt_text, output_fmt)
                st.success(f'✅ "{title}" saved successfully!')
