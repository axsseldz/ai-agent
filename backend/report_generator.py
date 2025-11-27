from datetime import datetime

def generate_report(name, appointment_type, date, time, symptoms, recommended_service, doctor):

    report = {
        "patient_name": name,
        "appointment_type": appointment_type,
        "date": date,
        "time": time,
        "symptoms": symptoms,
        "recommended_service": recommended_service,
        "doctor": doctor,
        "created_at": datetime.now().isoformat()
    }

    return report

