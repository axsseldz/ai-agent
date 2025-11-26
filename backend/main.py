from fastapi import FastAPI
from pydantic import BaseModel
from calendar_utils import create_calendar_event

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running correctly"}


# -> Test endpoint to create a calendar event 
# @app.post("/test/create-event")
# def test_create_event():
#     event = create_calendar_event(
#         summary="Cita de prueba con Axel",
#         description="Creada por el backend del agente.",
#         start_datetime="2025-11-26T15:00:00",
#         end_datetime="2025-11-26T16:00:00"
#     )

#     return {"status": "success", "event_link": event.get("htmlLink")}

class AppointmentRequest(BaseModel):
    name: str
    appointment_type: str
    date: str      # YYYY-MM-DD
    time: str      # HH:MM

@app.post("/schedule-appointment")
def schedule_appointment(req: AppointmentRequest):

    start_datetime = f"{req.date}T{req.time}:00"
    
    hour = int(req.time.split(":")[0]) + 1
    end_datetime = f"{req.date}T{hour:02d}:{req.time.split(':')[1]}:00"

    event = create_calendar_event(
        summary=f"Cita dental: {req.name}",
        description=f"Tipo de cita: {req.appointment_type}",
        start_datetime=start_datetime,
        end_datetime=end_datetime
    )

    return {
        "status": "success",
        "message": f"La cita ha sido agendada para {req.date} a las {req.time}.",
        "event_link": event.get("htmlLink")
    }
