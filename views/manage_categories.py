import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.helpers import get_all_categories, add_category, delete_category

def show():
    st.title("🗂️ Manage Categories")
    st.markdown("Add your own custom categories to organize your prompts any way you want.")

    st.divider()

    # ── ADD NEW CATEGORY ─────────────────────────────────────
    st.subheader("➕ Add New Category")

    with st.form("add_category_form", clear_on_submit=True):
        new_cat = st.text_input(
            "Category Name",
            placeholder="e.g. Image Editing, Marketing, Finance..."
        )
        submitted = st.form_submit_button("Add Category", use_container_width=True)

        if submitted:
            if not new_cat.strip():
                st.error("Please enter a category name.")
            else:
                result, message = add_category(new_cat.strip())
                if result:
                    st.success(f'✅ Category "{new_cat.strip()}" added successfully!')
                else:
                    st.error(f'❌ {message}')

    st.divider()

    # ── EXISTING CATEGORIES ───────────────────────────────────
    st.subheader("📂 Existing Categories")

    categories = get_all_categories()

    if not categories:
        st.info("No categories yet. Add your first one above!")
        return

    st.markdown(f"**{len(categories)} categories in your library**")
    st.spacer if hasattr(st, 'spacer') else None

    for cat in categories:
        col1, col2, col3 = st.columns([6, 2, 2])
        with col1:
            st.markdown(f"📁 **{cat.name}**")
        with col2:
            st.caption(f"Added: {cat.created_at.strftime('%d %b %Y')}")
        with col3:
            if st.button("🗑️ Delete", key=f"delcat_{cat.id}"):
                delete_category(cat.id)
                st.success(f'Deleted "{cat.name}"')
                st.rerun()

    st.divider()
    st.warning(
        "⚠️ Warning: Deleting a category will permanently delete ALL prompts inside it. "
        "This action cannot be undone."
    )
