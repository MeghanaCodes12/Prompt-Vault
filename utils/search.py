from database.db import SessionLocal
from database.models import Prompt

def search_prompts(query="", category="All", difficulty="All", favorites_only=False):
    db = SessionLocal()
    results = db.query(Prompt)

    if query:
        results = results.filter(
            Prompt.title.ilike(f"%{query}%") |
            Prompt.tags.ilike(f"%{query}%") |
            Prompt.prompt_text.ilike(f"%{query}%")
        )
    if category != "All":
        results = results.filter(Prompt.category == category)
    if difficulty != "All":
        results = results.filter(Prompt.difficulty == difficulty)
    if favorites_only:
        results = results.filter(Prompt.favorite == True)

    results = results.order_by(Prompt.created_at.desc()).all()
    db.close()
    return results
