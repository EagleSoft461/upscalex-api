import os
from dotenv import load_dotenv
import torch

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")
SCALE = int(os.getenv("SCALE", 4))
DEVICE_ENV = os.getenv("DEVICE", "auto").lower()

API_KEYS_FREE = set(os.getenv("API_KEYS_FREE", "").split(","))
API_KEYS_PRO = set(os.getenv("API_KEYS_PRO", "").split(","))

if not MODEL_PATH:
    raise RuntimeError("MODEL_PATH .env içinde tanımlı değil")

if not API_KEYS_FREE and not API_KEYS_PRO:
    raise RuntimeError("API key'ler tanımlı değil")

# DEVICE seçimi
if DEVICE_ENV == "auto":
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
elif DEVICE_ENV in ["cpu", "cuda"]:
    DEVICE = torch.device(DEVICE_ENV)
else:
    raise RuntimeError("DEVICE değeri auto | cpu | cuda olmalı")
