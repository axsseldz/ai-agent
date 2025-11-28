const flow = [
  {
    title: "Llamas al agente",
    detail: "Captura motivo y horario en segundos con voz natural.",
  },
  {
    title: "Orquesta la agenda",
    detail: "Asigna especialista, valida políticas y bloquea calendario.",
  },
  {
    title: "Confirma y envía",
    detail: (
      <>
        Te comparte dirección y recordatorio por{" "}
        <span className="whatsapp-glow">WhatsApp</span>.
      </>
    ),
  },
];

const stack = [
  { id: "twilio", name: "Twilio Voice", icon: TwilioIcon, desc: "Entrada de llamadas y routing." },
  { id: "openai", name: "OpenAI API", icon: OpenAIIcon, desc: "Comprensión y guías dinámicas." },
  { id: "elevenlabs", name: "ElevenLabs", icon: ElevenLabsIcon, desc: "Voz natural y clara." },
  { id: "gcal", name: "Google Calendar API", icon: GoogleCalIcon, desc: "Bloqueo y disponibilidad real." },
  {
    id: "whatsapp",
    name: <span className="whatsapp-glow">WhatsApp API</span>,
    icon: WhatsAppIcon,
    desc: "Envía dirección y recordatorios.",
  },
];

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-[#f3f6fb] via-white to-[#eef3fb] text-slate-900 relative overflow-hidden">
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute left-10 top-10 h-64 w-64 bg-emerald-200/40 blur-3xl rounded-full" />
        <div className="absolute right-10 top-32 h-72 w-72 bg-indigo-200/40 blur-3xl rounded-full" />
        <div className="absolute left-1/3 bottom-10 h-80 w-80 bg-cyan-200/35 blur-3xl rounded-full" />
      </div>

      <main className="relative z-10 max-w-6xl mx-auto px-6 py-16 space-y-20">
        <header className="grid md:grid-cols-[1.05fr_0.95fr] gap-12 items-center">
          <div className="space-y-6">
            <p className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white border border-emerald-100 text-sm text-emerald-700 shadow-sm">
              <span className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse" />
              Agente de voz siempre disponible
            </p>
            <div className="space-y-4">
              <h1 className="text-4xl md:text-5xl font-semibold leading-tight text-slate-900">
                Agenda con un agente de IA. Llama, confirma y recibe los detalles por{" "}
                <span className="whatsapp-glow">WhatsApp</span>.
              </h1>
              <p className="text-lg text-slate-600">
                Marca al <span className="font-semibold text-slate-800">804-689-4282</span>.
                El agente guía la llamada, asigna a la doctora correcta y agenda tu cita.
              </p>
            </div>
            <div className="flex flex-wrap gap-3">
              <a
                href="tel:+18046894282"
                className="px-5 py-3 rounded-full bg-emerald-600 text-white font-semibold shadow-md shadow-emerald-200/60 hover:-translate-y-0.5 transition"
              >
                Llamar ahora
              </a>
              <span className="px-4 py-3 rounded-full bg-white border border-slate-200 text-sm text-slate-700 shadow-sm">
                Sin chat. Todo se confirma en la llamada.
              </span>
            </div>
          </div>

          <AIAgentAnimation />
        </header>

        <section className="space-y-6">
          <div className="flex items-center gap-3">
            <span className="h-10 w-10 rounded-full bg-white border border-slate-100 flex items-center justify-center text-emerald-600 shadow-sm">
              ⟳
            </span>
            <div>
              <p className="text-sm uppercase tracking-wide text-emerald-700">Flujo del agente</p>
              <p className="text-xl font-semibold">Llamas, agenda y recibes dirección</p>
            </div>
          </div>
          <div className="grid md:grid-cols-3 gap-4">
            {flow.map((item, idx) => (
              <div
                key={item.title}
                className="relative overflow-hidden p-5 rounded-3xl bg-white border border-slate-100 shadow-sm group flow-animate"
                style={{ animationDelay: `${idx * 0.1}s` }}
              >
                <div className="absolute -right-10 -top-10 h-28 w-28 bg-emerald-200/30 blur-2xl rounded-full group-hover:scale-110 transition" />
                <div className="absolute left-0 top-0 flow-bar" />
                <p className="text-xs font-semibold text-emerald-700 mb-2">Paso {idx + 1}</p>
                <p className="text-lg font-semibold">{item.title}</p>
                <p className="text-sm text-slate-600 mt-2">{item.detail}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="space-y-6">
          <div className="flex items-center gap-3">
            <span className="h-10 w-10 rounded-full bg-white border border-slate-100 flex items-center justify-center text-indigo-600 shadow-sm">
              ⚙️
            </span>
            <div>
              <p className="text-sm uppercase tracking-wide text-emerald-700">
                Cómo fue construido
              </p>
              <p className="text-xl font-semibold">Stack del agente</p>
            </div>
          </div>
          <div className="grid md:grid-cols-5 sm:grid-cols-3 grid-cols-2 gap-4">
            {stack.map((item, idx) => (
              <div
                key={item.id}
                className="p-4 rounded-2xl bg-white border border-slate-100 shadow-sm flex flex-col gap-2 hover:-translate-y-1 transition stack-animate"
                style={{ animationDelay: `${idx * 0.08}s` }}
              >
                <div className="flex items-center gap-2">
                  <item.icon />
                  <p className="text-sm font-semibold text-slate-800">{item.name}</p>
                </div>
                <p className="text-xs text-slate-600">{item.desc}</p>
              </div>
            ))}
          </div>
          <p className="text-xs text-slate-500">
            Todo se orquesta en tu backend: captura de motivos, asignación segura, bloqueo en Google Calendar
            y envío de detalles por <span className="whatsapp-glow">WhatsApp</span> tras la llamada.
          </p>
        </section>
      </main>
    </div>
  );
}

function IconBase({
  children,
  bg,
}: {
  children: React.ReactNode;
  bg: string;
}) {
  return (
    <span
      className="h-8 w-8 rounded-full inline-flex items-center justify-center shadow-sm"
      style={{ background: bg }}
    >
      {children}
    </span>
  );
}

function TwilioIcon() {
  return (
    <IconBase bg="linear-gradient(135deg,#f22f46,#d60b2f)">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none">
        <rect x="3.5" y="3.5" width="17" height="17" rx="5" stroke="white" strokeWidth="2" />
        <circle cx="9" cy="9" r="1.6" fill="white" />
        <circle cx="15" cy="9" r="1.6" fill="white" />
        <circle cx="9" cy="15" r="1.6" fill="white" />
        <circle cx="15" cy="15" r="1.6" fill="white" />
      </svg>
    </IconBase>
  );
}

function OpenAIIcon() {
  return (
    <IconBase bg="linear-gradient(135deg,#10b981,#059669)">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="white" strokeWidth="1.6">
        <path d="M12 2.5 6 6v5l6 3 6-3V6l-6-3.5Z" />
        <path d="M6 11v5l6 3 6-3v-5" />
        <path d="M6 11 12 8l6 3" />
      </svg>
    </IconBase>
  );
}

function ElevenLabsIcon() {
  return (
    <IconBase bg="linear-gradient(135deg,#ff7b00,#ffb347)">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none">
        <path
          d="M6 5h4v14H6zM14 5h4v14h-4z"
          fill="white"
          opacity="0.9"
        />
        <path d="M6 9h12" stroke="white" strokeWidth="1.6" opacity="0.85" />
        <path d="M6 13h12" stroke="white" strokeWidth="1.6" opacity="0.7" />
      </svg>
    </IconBase>
  );
}

function GoogleCalIcon() {
  return (
    <IconBase bg="linear-gradient(135deg,#4285f4,#7ba7ff)">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none">
        <rect x="5" y="6" width="14" height="13" rx="2" fill="white" />
        <path d="M8 4v4M16 4v4" stroke="#4285f4" strokeWidth="2" strokeLinecap="round" />
        <rect x="8" y="11" width="8" height="5" rx="1" fill="#4285f4" />
      </svg>
    </IconBase>
  );
}

function WhatsAppIcon() {
  return (
    <IconBase bg="linear-gradient(135deg,#25d366,#128c7e)">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none">
        <path
          d="M12 4.5A7.5 7.5 0 0 0 6.1 17.1L5 20l3-1a7.5 7.5 0 1 0 4-14.5Z"
          stroke="white"
          strokeWidth="1.6"
          fill="none"
        />
        <path
          d="M10.2 9.5c-.3.6-.1 1.3.2 1.8.4.7 1 .9 1.6 1.2.5.2.8.4 1.3.2.4-.2.5-.7.7-1.1"
          stroke="white"
          strokeWidth="1.6"
          strokeLinecap="round"
        />
      </svg>
    </IconBase>
  );
}

function AIAgentAnimation() {
  return (
    <div className="relative h-full flex items-center justify-center">
      <div className="relative h-[420px] w-full max-w-[520px] bg-white border border-slate-100 rounded-[34px] shadow-2xl overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-emerald-50 via-white to-indigo-50" />
        <div className="absolute inset-4 rounded-[28px] border border-emerald-50/70 shadow-inner" />

        <div className="absolute inset-0 flex items-center justify-center">
          <div className="relative h-64 w-64 agent-float">
            <div className="absolute inset-0 rounded-[32px] bg-gradient-to-br from-white via-emerald-50 to-cyan-50 shadow-2xl" />
            <div className="absolute inset-2 rounded-[28px] border border-emerald-100/80 agent-glow" />

            <div
              className="absolute inset-5 rounded-3xl border border-emerald-200/70"
              style={{ animation: "spinSlow 18s linear infinite" }}
            />
            <div
              className="absolute inset-10 rounded-3xl border border-indigo-200/70"
              style={{ animation: "spinSlow 12s linear infinite reverse" }}
            />
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="relative h-32 w-32 rotate-6 rounded-[22px] bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white text-sm font-semibold flex items-center justify-center shadow-lg agent-pulse">
                IA Core
                <div className="absolute inset-0 rounded-[22px] border border-white/15" />
              </div>
              <div className="absolute h-44 w-44 rounded-full border border-emerald-200/80 orbital" />
              <div
                className="absolute h-12 w-12 rounded-full bg-gradient-to-br from-emerald-400 to-cyan-400 shadow-lg orbital"
                style={{ animationDuration: "14s" }}
              />
              <div
                className="absolute h-9 w-9 rounded-full bg-gradient-to-br from-indigo-400 to-emerald-300 shadow-lg orbital"
                style={{ animationDuration: "10s", animationDirection: "reverse" }}
              />
            </div>

            <div className="absolute inset-0 pointer-events-none">
              <div
                className="absolute inset-x-6 top-1/2 h-14 bg-gradient-to-r from-transparent via-emerald-100 to-transparent rounded-full blur-2xl"
                style={{ animation: "sweep 5s ease-in-out infinite" }}
              />
              <div className="absolute inset-x-10 top-1/2 h-px bg-gradient-to-r from-emerald-400 via-cyan-400 to-indigo-500 opacity-60" />
              {[...Array(6)].map((_, i) => (
                <span
                  key={i}
                  className="particle absolute h-2 w-2 rounded-full bg-gradient-to-br from-emerald-400 to-cyan-400"
                  style={{
                    top: `${20 + i * 10}%`,
                    left: `${30 + i * 7}%`,
                    animationDelay: `${i * 0.4}s`,
                  }}
                />
              ))}
            </div>
          </div>
        </div>

        <div className="absolute left-6 right-6 bottom-6 space-y-3">
          <div className="flex items-center justify-between text-xs text-slate-600">
            <span className="flex items-center gap-2">
              <span className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse" />
              Agente operativo
            </span>
            <span>Sonrisa Perfecta</span>
          </div>
        </div>
      </div>
    </div>
  );
}
