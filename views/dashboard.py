import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.helpers import get_all_prompts, get_category_names

def show():
    st.title("📊 Dashboard")

    prompts    = get_all_prompts()
    categories = get_category_names()
    total      = len(prompts)
    favorites  = sum(1 for p in prompts if p.favorite)

    counts = {c: sum(1 for p in prompts if p.category == c) for c in categories}

    col1, col2, col3 = st.columns(3)
    col1.metric("📝 Total Prompts", total)
    col2.metric("⭐ Favorites",     favorites)
    col3.metric("📂 Categories",    len([c for c in counts if counts[c] > 0]))

    st.divider()
    st.subheader("Prompts by Category")

    if not categories:
        st.info("No categories yet. Add categories from Manage Categories page.")
        return

    for cat, count in counts.items():
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.progress(count / total if total else 0, text=cat)
        with col_b:
            st.markdown(f"**{count}**")
