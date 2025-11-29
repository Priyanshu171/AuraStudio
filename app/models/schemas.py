from pydantic import BaseModel
from typing import Optional, List

class GenerateRequest(BaseModel):
    title: str
    tone: Optional[str] = "professional"
    audience: Optional[str] = "general"
    format: Optional[str] = "blog"   # blog | social | newsletter
    include_images: bool = True
    image_prompts: Optional[List[str]] = None
