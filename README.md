## AI Agent

Landing en Next.js + backend en FastAPI para un agente de voz que interpreta, agenda y confirma citas dentales. El frontend es una UI de divulgación; el core está en el backend que integra IA, calendario y WhatsApp.

---

## Arquitectura rápida
- **Frontend (UI)**: Next.js 16 / React 19. Landing con animación del agente, flujo y stack tecnológico.
- **Backend (IA + orquestación)**: FastAPI.
  - Interpretación con **OpenAI API** (prompt + knowledge base).
  - **Google Calendar API** vía cuenta de servicio para agendar citas.
  - **Twilio Voice/WhatsApp** para llamadas entrantes y envío de confirmaciones.
  - **ElevenLabs** disponible para voz natural.


## Vista del frontend
Vista de el landing page

[![Website](./frontend/app/landing.png)](https://ai-agent-five-beta.vercel.app)


---

## Requisitos previos
- Python 3.11+ y Node.js 18+.
- Credenciales de Google Calendar (JSON de cuenta de servicio).
- Credenciales de Twilio (voz + WhatsApp).
- API key de OpenAI.
- Opcional: API key de ElevenLabs.

---

## Variables de entorno (backend)
Configura un `.env` en `backend/` con:
- `OPENAI_API_KEY`
- `GOOGLE_SERVICE_ACCOUNT_FILE` (ruta al JSON de cuenta de servicio, p.ej. `backend/credentials.json`)
- `GOOGLE_CALENDAR_ID` (ID del calendario donde se bloquean citas)
- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`
- `SANDBOX_PHONE_NUMBER` (remitente WhatsApp de Twilio, ej. `whatsapp:+1415...`)
- `WHATSAPP_TEMPLATE_SID` (SID de la plantilla WhatsApp)
- `ELEVENLABS_API_KEY` (opcional si usas TTS)

---

## Cómo correrlo

### Backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Endpoints clave:
- `POST /interpret` — interpreta el mensaje del paciente y devuelve campos estructurados.
- `POST /schedule-appointment` — agenda en Google Calendar y envía confirmación por WhatsApp.
- `POST /check-availability` — valida disponibilidad básica.

### Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
```
Abre `http://localhost:3000` para ver la landing del agente.


