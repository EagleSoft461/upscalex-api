🚀 UpscaleX API – AI Image Upscaling Service

UpscaleX is a fast, secure, and production-ready AI image upscaling API built with FastAPI and Real-ESRGAN.

🔍 4× AI Super Resolution
🔐 API Key protected
⚡ Built for developers & SaaS products

✨ Features

🧠 AI-powered 4× image upscaling

✂️ Optional background removal

🔐 API key authentication

⏱ Daily rate limiting

📦 Simple REST API

🚀 Production-ready backend

📊 Plans
Plan	Daily Limit	Upscaling	Background Removal
Free	10 requests/day	✅	✅
Pro	Unlimited	✅	✅
🛠 Tech Stack

FastAPI

PyTorch

Real-ESRGAN

OpenCV

rembg

Uvicorn

📁 Project Structure
upscalex-api/
│
├── main.py
├── config.py
├── auth.py
├── rate_limit.py
├── models/
│   └── realesr-general-x4v3.pth
├── .env
├── requirements.txt
└── README.md

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/EagleSoft461/upscalex-api.git
cd upscalex-api

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

🔐 Environment Variables

Create a .env file:

MODEL_PATH=models/realesr-general-x4v3.pth
SCALE=4
DEVICE=auto

API_KEYS_FREE=free_key_123
API_KEYS_PRO=pro_key_456

▶️ Run the Server
uvicorn main:app --reload


API will be available at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

❤️ Health Check
GET /health


Response:

{
  "status": "ok",
  "plans": {
    "free_daily_limit": 10,
    "pro": "unlimited"
  }
}

📸 Upscale Image
Endpoint
POST /upscale

Headers
x-api-key: free_key_123

Form Data
Field	Type
file	image file
remove_bg	boolean (optional)
Example (cURL)
curl -X POST "http://127.0.0.1:8000/upscale?remove_bg=false" \
  -H "x-api-key: free_key_123" \
  -F "file=@input.png"

📦 Response Headers
Header	Description
X-Plan	free / pro
X-RateLimit-Limit	Daily limit
X-RateLimit-Remaining	Remaining requests
🚨 Error Codes
Code	Meaning
400	Invalid image
401	Invalid API key
429	Free limit exceeded
500	Server error
🎯 Use Cases

SaaS image enhancement

AI photo tools

E-commerce product images

Mobile & web apps

Background removal pipelines

🧠 Roadmap

 Stripe payments

 User dashboard

 Usage analytics

 Batch image processing

 Docker & cloud deploy

⭐ Support UpscaleX

If you like this project:

⭐ Star the repository

🐛 Report issues

🤝 Contribute

📜 License

MIT License

⚡ UpscaleX API

Sharper images. Smarter AI.