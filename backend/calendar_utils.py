import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID")

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_calendar_service():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )
    return build("calendar", "v3", credentials=creds)


def create_calendar_event(summary, description, start_datetime, end_datetime):
    service = get_calendar_service()

    event = {
        "summary": summary,
        "description": description,
        "start": {"dateTime": start_datetime, "timeZone": "America/Tijuana"},
        "end": {"dateTime": end_datetime, "timeZone": "America/Tijuana"},
    }

    created_event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    return created_event