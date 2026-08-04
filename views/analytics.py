import streamlit as st
import pandas as pd
from utils.helpers import get_all_prompts

def show():
    st.title("📈 Analytics")

    prompts = get_all_prompts()
    if not prompts:
        st.info("No data yet. Add some prompts first!")
        return

    data = [{
        "Title":      p.title,
        "Category":   p.category,
        "Difficulty": p.difficulty,
        "Favorite":   p.favorite,
        "Created":    p.created_at
    } for p in prompts]

    df = pd.DataFrame(data)

    st.subheader("Category Breakdown")
    st.bar_chart(df["Category"].value_counts())

    st.subheader("Difficulty Breakdown")
    st.bar_chart(df["Difficulty"].value_counts())

    st.subheader("All Prompts")
    st.dataframe(df, use_container_width=True)
