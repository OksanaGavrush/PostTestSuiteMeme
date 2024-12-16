from pydantic import BaseModel
from typing import List


class CreateScheme(BaseModel):
    id: int
    info: dict
    tags: List[str]
    text: str
    updated_by: str
    url: str
