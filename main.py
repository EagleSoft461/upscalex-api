from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from fastapi import Depends
from auth import verify_api_key
from config import MODEL_PATH, SCALE
from rembg import remove
import cv2
import numpy as np
import torch
from realesrgan import RealESRGANer
from realesrgan.archs.srvgg_arch import SRVGGNetCompact
import io

app = FastAPI()

# Cihaz ayarı
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Model yükleme
model = SRVGGNetCompact(num_in_ch=3, num_out_ch=3, num_feat=64, num_conv=32, upscale=4, act_type='prelu')
upsampler = RealESRGANer(
    scale=SCALE,
    model_path=MODEL_PATH,
    model=model,
    tile=0,
    tile_pad=10,
    pre_pad=0,
    half=False,
    device=device
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "plans": {
            "free_daily_limit": 10,
            "pro": "unlimited"
        }
    }

from fastapi import Depends

@app.post("/upscale")
async def upscale_image(
    file: UploadFile = File(...),
    remove_bg: bool = False,
    auth: dict = Depends(verify_api_key)
):
    # 🔒 Content-Type kontrolü
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Sadece resim dosyaları kabul edilir")

    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    if img is None:
        raise HTTPException(status_code=400, detail="Geçersiz resim dosyası")

    if remove_bg:
        img = remove(img)

    try:
        output, _ = upsampler.enhance(img, outscale=SCALE)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    _, buffer = cv2.imencode(".png", output)

    # 🔑 RATE LIMIT HEADER’LARI (❗ MUTLAKA FONKSİYON İÇİNDE)
    headers = {
        "X-Plan": auth["plan"]
    }

    if auth["plan"] == "free":
        headers["X-RateLimit-Limit"] = "10"
        headers["X-RateLimit-Remaining"] = str(auth.get("remaining", 0))
    else:
        headers["X-RateLimit-Limit"] = "unlimited"

    return StreamingResponse(
        io.BytesIO(buffer.tobytes()),
        media_type="image/png",
        headers=headers
    )