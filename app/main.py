from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.init.database import client

app = FastAPI(title="Trustcenter API")

# ===== CORS =====
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== MongoDB Connection Test =====
@app.on_event("startup")
async def startup_db_check():
    try:
        await client.admin.command("ping")
        print("✅ MongoDB connected successfully")
    except Exception as e:
        print("❌ MongoDB connection failed:", e)

# ===== Routers =====
@app.get("/")
async def root():
    return {"status": "Trustcenter API is running"}