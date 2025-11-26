from fastapi import FastAPI
from calendar_utils import create_calendar_event

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running correctly"}

@app.post("/test/create-event")
def test_create_event():
    event = create_calendar_event(
        summary="Cita de prueba con Axel",
        description="Creada por el backend del agente.",
        start_datetime="2025-11-26T15:00:00",
        end_datetime="2025-11-26T16:00:00"
    )

    return {"status": "success", "event_link": event.get("htmlLink")}
