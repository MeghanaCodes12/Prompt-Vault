from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Prompt(Base):
    __tablename__ = "prompts"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String(200), nullable=False)
    category    = Column(String(50),  nullable=False)
    difficulty  = Column(String(20),  nullable=False)
    tags        = Column(String(200), nullable=True)
    role        = Column(Text,        nullable=True)
    goal        = Column(Text,        nullable=True)
    context     = Column(Text,        nullable=True)
    prompt_text = Column(Text,        nullable=False)
    output_fmt  = Column(Text,        nullable=True)
    favorite    = Column(Boolean,     default=False)
    created_at  = Column(DateTime,    default=datetime.utcnow)
