import os
from openai import OpenAI
import asyncio

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_text(prompt: str, max_tokens=900, temperature=0.7):
    loop = asyncio.get_event_loop()

    def call():
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a content generator."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return resp

    resp = await loop.run_in_executor(None, call)
    return resp.choices[0].message.content
