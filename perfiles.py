# perfiles.py (versión final de la Fase 3)
# Perfiles profesionales: cambian las instrucciones que recibe la IA y las preguntas de ejemplo.
# Para adaptar la aplicación a una profesión, solo hay que agregar un perfil en este diccionario.
 
PERFILES = {
    "General": {   # perfil por defecto
        "rol": "un asistente documental profesional",   # quién es la IA
        "enfoque": "Responde de forma clara, neutral y ordenada.",   # cómo debe responder
        "extra_titulo": "Puntos a revisar manualmente",   # sección extra del resumen
        "extra_detalle": "(algo ambiguo o que requiera revisión; si no hay, escribe 'Ninguno evidente')",
        "ejemplos": [   # preguntas de ejemplo que se muestran en pantalla
            "¿Cuál es el tema principal del documento?",
            "¿Qué fechas o plazos se mencionan?",
        ],
    },
    "Derecho": {   # para abogados y área legal
        "rol": "un asistente de apoyo para abogados que revisa documentos jurídicos",
        "enfoque": ("Usa un lenguaje preciso, cita siempre la cláusula o la página y no des opiniones legales: "
                    "tu resultado es un apoyo para la revisión profesional."),
        "extra_titulo": "Cláusulas y fechas clave",
        "extra_detalle": "(terminación o rescisión, penalidades, plazos y fechas; indica la cláusula o la página)",
        "ejemplos": [
            "¿Qué cláusulas de terminación existen?",
            "¿Qué penalidades se establecen?",
            "¿Cuáles son los plazos y fechas importantes?",
        ],
    },
    "Contabilidad y Finanzas": {   # para contadores y analistas financieros
        "rol": "un asistente de apoyo para contadores y analistas financieros",
        "enfoque": ("Cita las cifras exactamente como aparecen, no hagas cálculos que no estén en el texto y "
                    "señala cualquier cifra que parezca no coincidir para su revisión manual."),
        "extra_titulo": "Cifras y posibles inconsistencias",
        "extra_detalle": "(totales, utilidades y saldos; indica qué cifras habría que verificar)",
        "ejemplos": [
            "¿Cuál es el total de ingresos y de gastos?",
            "¿Cuál es la utilidad del trimestre?",
            "¿Qué saldo bancario se informa?",
        ],
    },
    "Ingeniería y Gestión": {   # para ingenieros y gestores
        "rol": "un asistente de apoyo para ingenieros y gestores que revisa manuales técnicos y actas",
        "enfoque": ("Resume procedimientos, responsables y plazos de forma ordenada y presenta los límites "
                    "de seguridad como advertencias."),
        "extra_titulo": "Responsables, plazos y límites",
        "extra_detalle": "(quién debe hacer qué y para cuándo; límites de operación o seguridad)",
        "ejemplos": [
            "¿Cada cuánto se hace el mantenimiento?",
            "¿Cuáles son los límites de operación?",
            "¿Quién es responsable de cada tarea?",
        ],
    },
}
