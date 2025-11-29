from pathlib import Path

OUT = Path("outputs/text")
OUT.mkdir(parents=True, exist_ok=True)

def save_text(name: str, text: str):
    path = OUT / f"{name}.md"
    path.write_text(text, encoding="utf-8")
    return str(path)
