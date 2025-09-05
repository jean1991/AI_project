import os
import uuid
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models.text_generator import generate_text
from models.image_generator import generate_image

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For demo; restrict in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(request: PromptRequest):
    prompt = request.prompt
    text = generate_text(prompt)
    image_filename = f"generated_{uuid.uuid4().hex}.png"
    image_dir = "images"
    os.makedirs(image_dir, exist_ok=True)
    image_path = os.path.join(image_dir, image_filename)
    generate_image(prompt, output_path=image_path)
    return {
        "text": text,
        "image_url": f"/images/{image_filename}"
    }

@app.get("/images/{image_name}")
async def get_image(image_name: str):
    image_path = os.path.join("images", image_name)
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type="image/png")
    return JSONResponse({"error": "Image not found"}, status_code=404)