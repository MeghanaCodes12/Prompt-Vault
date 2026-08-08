from database.db import SessionLocal
from database.models import Prompt, Category

def get_session():
    return SessionLocal()

# ── PROMPT FUNCTIONS ──────────────────────────────────────────

def add_prompt(title, category, difficulty, tags,
               role, goal, context, prompt_text, output_fmt):
    db = get_session()
    new_prompt = Prompt(
        title=title, category=category, difficulty=difficulty,
        tags=tags, role=role, goal=goal, context=context,
        prompt_text=prompt_text, output_fmt=output_fmt
    )
    db.add(new_prompt)
    db.commit()
    db.refresh(new_prompt)
    db.close()
    return new_prompt

def get_all_prompts():
    db = get_session()
    prompts = db.query(Prompt).order_by(Prompt.created_at.desc()).all()
    db.close()
    return prompts

def get_prompt_by_id(prompt_id):
    db = get_session()
    prompt = db.query(Prompt).filter(Prompt.id == prompt_id).first()
    db.close()
    return prompt

def update_prompt(prompt_id, **kwargs):
    db = get_session()
    prompt = db.query(Prompt).filter(Prompt.id == prompt_id).first()
    for key, value in kwargs.items():
        setattr(prompt, key, value)
    db.commit()
    db.close()

def delete_prompt(prompt_id):
    db = get_session()
    prompt = db.query(Prompt).filter(Prompt.id == prompt_id).first()
    db.delete(prompt)
    db.commit()
    db.close()

def toggle_favorite(prompt_id):
    db = get_session()
    prompt = db.query(Prompt).filter(Prompt.id == prompt_id).first()
    prompt.favorite = not prompt.favorite
    db.commit()
    db.close()

# ── CATEGORY FUNCTIONS ────────────────────────────────────────

def get_all_categories():
    db = get_session()
    categories = db.query(Category).order_by(Category.name).all()
    db.close()
    return categories

def get_category_names():
    categories = get_all_categories()
    return [c.name for c in categories]

def add_category(name):
    db = get_session()
    existing = db.query(Category).filter(
        Category.name.ilike(name)
    ).first()
    if existing:
        db.close()
        return None, "Category already exists"
    new_cat = Category(name=name.strip())
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    db.close()
    return new_cat, "success"

def delete_category(category_id):
    db = get_session()
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        # Delete all prompts inside this category first
        db.query(Prompt).filter(Prompt.category == category.name).delete()
        # Then delete the category itself
        db.delete(category)
        db.commit()
    db.close()

def init_default_categories():
    db = get_session()
    defaults = ["Study", "Coding", "Research", "Resume", "Productivity", "Image Editing"]
    for name in defaults:
        existing = db.query(Category).filter(Category.name == name).first()
        if not existing:
            db.add(Category(name=name))
    db.commit()
    db.close()
