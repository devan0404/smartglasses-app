from fastapi import FastAPI
from app.api import router                    # 🔄 Fixed import path
from app.controller import controller         # ✅ Ensure controller is defined in controller.py

app = FastAPI(title="Smart Glasses API")
app.include_router(router)

@app.on_event("shutdown")
def shutdown_event():
    print("Shutting down cleanly...")
    controller.stop()  # ✅ This will safely stop detection and release the camera
