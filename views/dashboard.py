import streamlit as st
from utils.helpers import get_all_prompts

def show():
    st.title("📊 Dashboard")

    prompts = get_all_prompts()
    total     = len(prompts)
    favorites = sum(1 for p in prompts if p.favorite)

    cats = ["Study","Coding","Research","Resume","Productivity"]
    counts = {c: sum(1 for p in prompts if p.category == c) for c in cats}

    col1, col2, col3 = st.columns(3)
    col1.metric("📝 Total Prompts", total)
    col2.metric("⭐ Favorites",     favorites)
    col3.metric("📂 Categories",    len([c for c in counts if counts[c] > 0]))

    st.divider()
    st.subheader("Prompts by Category")

    for cat, count in counts.items():
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.progress(count / total if total else 0, text=cat)
        with col_b:
            st.markdown(f"**{count}**")
