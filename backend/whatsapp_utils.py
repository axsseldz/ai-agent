from twilio.rest import Client
import os
from dotenv import load_dotenv
import json

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP = os.getenv("SANDBOX_PHONE_NUMBER")
WHATSAPP_TEMPLATE_SID = os.getenv("WHATSAPP_TEMPLATE_SID")

client = Client(TWILIO_SID, TWILIO_AUTH)


def send_whatsapp_confirmation(to_number: str, name: str, date: str, time: str, service: str):

    if not to_number or len(to_number) < 10:
        print("ERROR: No se puede enviar WhatsApp porque el número está vacío o incompleto.")
        return None

    try:
        variables = {
            "1": name,
            "2": service,
            "3": date,
            "4": time
        }

        message = client.messages.create(
            from_=TWILIO_WHATSAPP,
            to=f"whatsapp:+521{to_number}",
            content_sid=WHATSAPP_TEMPLATE_SID,
            content_variables=json.dumps(variables)
        )

        return message.sid

    except Exception as e:
        print(f"Error enviando WhatsApp: {e}")
        return None
