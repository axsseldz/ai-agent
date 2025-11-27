from fastapi import FastAPI
from pydantic import BaseModel
from intent_engine import analyze_message
from report_generator import generate_report
from calendar_utils import create_calendar_event
from check_availability import check_availability
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running correctly"}


class PatientMessage(BaseModel):
    transcript: str

class AppointmentRequest(BaseModel):
    name: str
    appointment_type: str
    date: str     
    time: str      
    symptoms: str | None = ""
    recommended_service: str | None = ""
    doctor: str | None = ""

class AvailabilityRequest(BaseModel):
    year: int
    month: int
    day: int
    time: str


@app.post("/interpret")
def interpret_message(req: PatientMessage):
    print("🟦 interpret called")
    result = analyze_message(req.transcript)
    return result


@app.post("/schedule-appointment")
def schedule_appointment(req: AppointmentRequest):
    print("🟩 scheduling appointment...")

    start_datetime = f"{req.date}T{req.time}:00"
    hour = int(req.time.split(":")[0]) + 1
    end_datetime = f"{req.date}T{hour:02d}:{req.time.split(':')[1]}:00"

    event = create_calendar_event(
        summary=f"Cita dental: {req.name}",
        description=f"Tipo de cita: {req.appointment_type}",
        start_datetime=start_datetime,
        end_datetime=end_datetime
    )

    report = generate_report(
        name=req.name,
        appointment_type=req.appointment_type,
        date=req.date,
        time=req.time,
        symptoms=req.symptoms,
        recommended_service=req.recommended_service,
        doctor=req.doctor
    )

    res = {
        "status": "success",
        "message": f"La cita ha sido agendada para {req.date} a las {req.time}.",
        "event_link": event.get("htmlLink"),
        "report": report
    }

    print("✅ appointment scheduled")

    return res


@app.post("/check-availability")
def check_availability_endpoint(req: AvailabilityRequest):
    print("🗓️ Checking availability...")

    result = check_availability(
        year=req.year,
        month=req.month,
        day=req.day,
        time_str=req.time
    )
    
    return result
