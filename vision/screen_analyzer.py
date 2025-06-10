# Screen Analyzer: OCR + UI element extraction
from promptops.vision.ocr import extract_text
from promptops.vision.screen_capture import capture_screen

async def find_button_coordinates(label: str):
    # Capture screen and run OCR to find button coordinates
    img = await capture_screen()
    elements = await extract_text(img)
    for el in elements:
        if label.lower() in el["text"].lower():
            return el["bbox"]  # (x, y)
    return None
