import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

OUTPUT_DIR = Path("outputs/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

async def generate_image(prompt: str, index: int = 0):
    resp = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )
    url = resp.data[0].url
    out = OUTPUT_DIR / f"img_{index}.txt"
    out.write_text(url)
    return str(out)
