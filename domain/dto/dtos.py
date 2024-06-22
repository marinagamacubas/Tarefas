from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class taskDTO(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_at: datetime


class taskCreateDTO(BaseModel):
    title: str
    description: str
    status: Optional[str] = "Pendente"
    
    def model_dump(self):
        return self.dict()

class taskUpdateDTO(BaseModel):
    title: str
    description: str
    status: str
 
