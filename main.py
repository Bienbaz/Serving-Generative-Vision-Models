from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from models import generate_image
from utils import image_to_bytes

app = FastAPI(title="Lumina Creative - Text-to-Image API")

class ImageRequest(BaseModel):
    prompt: str
    negative_prompt: str = ""
    height: int = 512
    width: int = 512
    num_inference_steps: int = 30

@app.post("/generate/image")
async def generate(request: ImageRequest):
    try:
        image = generate_image(
            prompt=request.prompt,
            negative_prompt=request.negative_prompt,
            height=request.height,
            width=request.width,
            num_inference_steps=request.num_inference_steps
        )
        image_bytes = image_to_bytes(image)
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
