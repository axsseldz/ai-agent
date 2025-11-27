import os
import json
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Eres un asistente especializado en interpretar mensajes de pacientes dentales.

Tu tarea:
1. Identificar intención (consulta, pregunta, síntomas, solicitud de cita, etc.)
2. Detectar tratamiento recomendado
3. Detectar doctor sugerido
4. Detectar fecha y/o hora si el paciente la menciona
5. Identificar síntomas
6. Generar datos estructurados para el backend

Formato de respuesta OBLIGATORIO:
{
  "intent": "...",
  "appointment_type": "",
  "raw_date": "",
  "raw_time": "",
  "symptoms": [],
  "doctor": "",
  "recommended_service": "",
  "name": "",
  "phone_number": "",
  "message_for_patient": "",
  "should_generate_report": false
}

Tu respuesta SIEMPRE debe ser JSON 100% válido, sin explicación.
"""

KNOWLEDGE = open("knowledge_base.txt").read()


def normalize_phone(num: str):
    if not num:
        return ""
    return re.sub(r"\D", "", num)

def analyze_message(user_message: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT + KNOWLEDGE},
            {"role": "user", "content": user_message}
        ]
    )

    raw = completion.choices[0].message.content

    cleaned = (
        raw.replace("```json", "")
           .replace("```", "")
           .strip()
    )

    data = json.loads(cleaned)

    data["phone_number"] = normalize_phone(data.get("phone_number", ""))

    return data
