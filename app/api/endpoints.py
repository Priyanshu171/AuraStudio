from fastapi import APIRouter
from ..models.schemas import GenerateRequest
from ..pipelines.prompt_chain import build_prompt
from ..services.openai_service import generate_text
from ..services.image_service import generate_image
from ..services.assets_store import save_text
import asyncio

router = APIRouter()

@router.post("/generate")
async def generate(req: GenerateRequest):
    prompt = build_prompt(req)

    text = await generate_text(prompt)
    text_path = save_text(req.title.replace(" ", "_"), text)

    images = []
    if req.include_images:
        prompts = req.image_prompts or [f"Illustration for: {req.title} #{i}" for i in range(2)]
        tasks = [generate_image(p, i) for i, p in enumerate(prompts)]
        images = await asyncio.gather(*tasks)

    return {
        "title": req.title,
        "text_path": text_path,
        "images": images
    }
