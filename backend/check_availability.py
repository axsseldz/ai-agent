import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID")
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

TIJUANA_TZ = ZoneInfo("America/Tijuana")

def get_calendar_service():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )
    return build("calendar", "v3", credentials=creds)


def check_availability(year, month, day, time_str):
    service = get_calendar_service()
    
    start_dt = datetime(
        year=int(year),
        month=int(month),
        day=int(day),
        hour=int(time_str.split(":")[0]),
        minute=int(time_str.split(":")[1]),
        tzinfo=TIJUANA_TZ
    )

    end_dt = start_dt + timedelta(hours=1)

    start_iso = start_dt.isoformat()
    end_iso = end_dt.isoformat()

    print("start_iso:", start_iso)
    print("end_iso:", end_iso)

    events = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=start_iso,
        timeMax=end_iso,
        singleEvents=True,
        orderBy="startTime"
    ).execute().get("items", [])

    if not events:
        return {
            "available": True,
            "suggestions": []
        }
    
    suggestions = []
    for i in range(1, 4):
        alt_start = start_dt + timedelta(hours=i)
        suggestions.append({
            "date": alt_start.strftime("%Y-%m-%d"),
            "time": alt_start.strftime("%H:%M")
        })

    return {
        "available": False,
        "suggestions": suggestions
    }
