🚀 UpscaleX API – AI Image Upscaling Service

High-performance AI Image Upscaling & Background Removal API
Powered by Real-ESRGAN, built with FastAPI

Upscale images up to 4x resolution with blazing speed.
Designed for developers, SaaS products, and AI pipelines.

✨ Features

⚡ FastAPI backend (high performance)

🧠 Real-ESRGAN (x4) image upscaling

🖼 Optional background removal

🔑 API Key authentication

🆓 Free & 💎 Pro plans

⏱ Daily rate limiting

🧩 Clean, modular architecture

🐳 Docker & cloud ready (coming soon)

📊 Free vs Pro
Feature	Free	Pro
Daily Requests	10 / day	Unlimited
Upscale Resolution	x4	x4
Background Removal	❌	✅
Priority Processing	❌	✅
Commercial Use	❌	✅
Support	Community	Priority
🔐 Authentication

All requests require an API key via header:

x-api-key: YOUR_API_KEY


Example:

Free key → free_key_123

Pro key → pro_key_abc

🧪 API Usage
Health Check
GET /health


Response:

{
  "status": "ok",
  "plans": {
    "free_daily_limit": 10,
    "pro": "unlimited"
  }
}

Image Upscale
curl -X POST "http://localhost:8000/upscale?remove_bg=false" \
  -H "x-api-key: free_key_123" \
  -F "file=@image.png"


✅ Returns a PNG image stream
❌ Free users are rate-limited

⚠️ Rate Limiting

Free users: 10 requests / day

Exceeding the limit returns:

{
  "detail": "Günlük ücretsiz limit doldu"
}


Rate limit info is sent via headers:

X-RateLimit-Limit
X-RateLimit-Remaining

🏗 Project Structure
upscalex-api/
├── main.py          # FastAPI app
├── auth.py          # API key verification
├── rate_limit.py   # Daily request limits
├── config.py       # App configuration
├── test_esrgan.py  # Local testing
├── README.md
└── .gitignore

💳 Pro Plan (Coming Soon)

Stripe subscriptions

Monthly billing

Unlimited requests

Commercial license

Priority inference

This repository is production-ready and designed to evolve into a paid SaaS.

🚀 Roadmap

 Stripe integration

 Dockerfile

 Cloud deploy (Railway / Fly.io)

 Mini web demo

 Usage analytics

⭐ Why Star This Repo?

Clean AI backend architecture

Real production use case

Easy to extend

Perfect base for SaaS products

If you find this project useful, please give it a star ⭐

📜 License

MIT License – free for personal use.
Commercial use requires Pro plan.

👤 Author

EagleSoft
Building practical AI products.
Sharper images. Smarter AI.
