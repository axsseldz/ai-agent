import re
from fastapi import FastAPI
from pydantic import BaseModel, field_validator, model_validator
from intent_engine import analyze_message
from report_generator import generate_report
from calendar_utils import create_calendar_event
from check_availability import check_availability
from whatsapp_utils import send_whatsapp_confirmation
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
LAST_KNOWN_PHONE = ""

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
    phone_number: str | None = ""

    @model_validator(mode="before")
    @classmethod
    def merge_phone_fields(cls, data):
        if isinstance(data, dict):
            phone = data.get("phone_number") or data.get("phone") or data.get("phoneNumber")
            if phone is not None:
                data["phone_number"] = phone
        return data

    @field_validator("phone_number", mode="before")
    @classmethod
    def normalize_phone(cls, value):
        if value is None:
            return ""
        return re.sub(r"\D", "", str(value))

class AvailabilityRequest(BaseModel):
    year: int
    month: int
    day: int
    time: str


@app.post("/interpret")
def interpret_message(req: PatientMessage):
    print("🟦 interpret called")
    result = analyze_message(req.transcript)

    global LAST_KNOWN_PHONE
    if result.get("phone_number"):
        LAST_KNOWN_PHONE = result["phone_number"]

    print(f"🤖 Interpretation result: {result}")
    return result


@app.post("/schedule-appointment")
def schedule_appointment(req: AppointmentRequest):
    print("🟩 scheduling appointment...")

    global LAST_KNOWN_PHONE
 
    if (not req.phone_number or len(req.phone_number) < 10) and LAST_KNOWN_PHONE:
        req.phone_number = LAST_KNOWN_PHONE

    start_datetime = f"{req.date}T{req.time}:00"
    hour = int(req.time.split(":")[0]) + 1
    end_datetime = f"{req.date}T{hour:02d}:{req.time.split(':')[1]}:00"

    event = create_calendar_event(
        summary=f"Cita dental: {req.name}",
        description=f"Tipo de cita: {req.appointment_type}\nTeléfono: {req.phone_number}",
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

    send_whatsapp_confirmation(
        to_number=req.phone_number,
        name=req.name,
        date=req.date,
        time=req.time,
        service=req.appointment_type
    )

    print("💬 whatsapp sent")

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
