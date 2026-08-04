import streamlit as st
from utils.search import search_prompts
from utils.helpers import delete_prompt, toggle_favorite, update_prompt

def show():
    st.title("📚 Prompt Library")

    col1, col2, col3, col4 = st.columns([3,1,1,1])
    with col1:
        query = st.text_input("🔍 Search", placeholder="Search by title, tag, or keyword...")
    with col2:
        category = st.selectbox("Category", ["All","Study","Coding","Research","Resume","Productivity"])
    with col3:
        difficulty = st.selectbox("Difficulty", ["All","Beginner","Intermediate","Advanced"])
    with col4:
        favs_only = st.checkbox("⭐ Favorites only")

    prompts = search_prompts(query, category, difficulty, favs_only)
    st.markdown(f"**{len(prompts)} prompt(s) found**")
    st.divider()

    if not prompts:
        st.info("No prompts found. Add your first one!")
        return

    for p in prompts:
        star = "⭐" if p.favorite else "☆"
        with st.expander(f"{star}  {p.title}  |  {p.category}  |  {p.difficulty}"):
            if p.role:       st.markdown(f"**Role:** {p.role}")
            if p.goal:       st.markdown(f"**Goal:** {p.goal}")
            if p.context:    st.markdown(f"**Context:** {p.context}")
            st.markdown(f"**Prompt:**")
            st.code(p.prompt_text, language="markdown")
            if p.output_fmt: st.markdown(f"**Output Format:** {p.output_fmt}")
            if p.tags:       st.markdown(f"🏷️ `{'` `'.join(p.tags.split(','))}`")

            c1, c2, c3, c4 = st.columns(4)
            with c1:
                if st.button("⭐ Favorite", key=f"fav_{p.id}"):
                    toggle_favorite(p.id)
                    st.rerun()
            with c2:
                if st.button("✏️ Edit", key=f"edit_{p.id}"):
                    st.session_state[f"editing_{p.id}"] = True
            with c3:
                if st.button("🗑️ Delete", key=f"del_{p.id}"):
                    delete_prompt(p.id)
                    st.rerun()

            if st.session_state.get(f"editing_{p.id}"):
                with st.form(key=f"edit_form_{p.id}"):
                    new_title = st.text_input("Title", value=p.title)
                    new_text  = st.text_area("Prompt Text", value=p.prompt_text, height=150)
                    new_tags  = st.text_input("Tags", value=p.tags or "")
                    if st.form_submit_button("💾 Save Changes"):
                        update_prompt(p.id, title=new_title, prompt_text=new_text, tags=new_tags)
                        st.session_state[f"editing_{p.id}"] = False
                        st.rerun()
