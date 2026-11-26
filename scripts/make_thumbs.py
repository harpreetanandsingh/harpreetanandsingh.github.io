"""Crops one panel from each project figure into a 16:9 card thumbnail (thumb.png)."""
from pathlib import Path

from PIL import Image

IMG = Path(__file__).resolve().parent.parent / "assets" / "img" / "projects"
SIZE = (640, 360)

# slug: (source file, crop box as fractions of width/height: left, top, right, bottom)
CROPS = {
    "neural-beta": ("quintiles.png", (0.0, 0.0, 0.318, 1.0)),
    "tail-risk": ("tails.png", (0.255, 0.0, 0.5, 1.0)),
    "default-prediction": ("roc-pr.png", (0.0, 0.0, 0.5, 1.0)),
    "fomc-event-study": ("coef-by-day.png", (0.0, 0.0, 1.0, 1.0)),
    "financial-rag": ("recall.png", (0.52, 0.0, 1.0, 0.855)),
}


def main():
    for slug, (name, (l, t, r, b)) in CROPS.items():
        im = Image.open(IMG / slug / name).convert("RGB")
        w, h = im.size
        panel = im.crop((int(l * w), int(t * h), int(r * w), int(b * h)))
        panel.thumbnail((SIZE[0] - 24, SIZE[1] - 16), Image.LANCZOS)
        canvas = Image.new("RGB", SIZE, "white")
        canvas.paste(panel, ((SIZE[0] - panel.width) // 2, (SIZE[1] - panel.height) // 2))
        out = IMG / slug / "thumb.png"
        canvas.save(out, optimize=True)
        print(out.relative_to(IMG.parent.parent.parent), panel.size)


if __name__ == "__main__":
    main()
