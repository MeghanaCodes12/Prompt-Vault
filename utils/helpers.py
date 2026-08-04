from database.db import SessionLocal
from database.models import Prompt

def get_session():
    return SessionLocal()

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
