from PIL import Image
import io

def image_to_bytes(image: Image.Image) -> bytes:
    """Convert PIL Image to PNG bytes without saving to disk."""
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr.getvalue()
