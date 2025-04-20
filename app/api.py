from fastapi import APIRouter
from pydantic import BaseModel
from app.controller import DetectionController

router = APIRouter()
controller = DetectionController()

class VoiceConfig(BaseModel):
    gender: str

class DelayConfig(BaseModel):
    seconds: float

@router.get("/start")
def start_detection():
    controller.start()
    return {"status": "started"}

@router.get("/stop")
def stop_detection():
    controller.stop()
    return {"status": "stopped"}

@router.get("/status")
def get_status():
    return {"running": controller.get_status()}

@router.post("/set-voice")
def set_voice(config: VoiceConfig):
    success = controller.set_voice(config.gender)
    return {"voice_set": success, "gender": config.gender}

@router.post("/set-delay")
def set_delay(config: DelayConfig):
    controller.set_delay(config.seconds)
    return {"delay": config.seconds}

