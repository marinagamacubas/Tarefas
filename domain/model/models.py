from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Bases = declarative_base()

class task(Bases):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    description = Column(String(255), nullable=True, index=True)
    status = Column(String(50), default="Pendente", index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task(id={self.id}, title={self.title}, description={self.description}, status={self.status}, created_at={self.created_at})>'
