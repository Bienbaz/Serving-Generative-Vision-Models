from diffusers import StableDiffusionPipeline
import torch

def load_model():
    """Load the distilled Tiny Stable Diffusion model."""
    pipe = StableDiffusionPipeline.from_pretrained(
        "segmind/tiny-sd", 
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe

model = load_model()

def generate_image(prompt: str, negative_prompt: str = "", height: int = 512, width: int = 512, num_inference_steps: int = 30):
    """Generate image from text prompt."""
    image = model(
        prompt,
        negative_prompt=negative_prompt,
        height=height,
        width=width,
        num_inference_steps=num_inference_steps
    ).images[0]
    return image
