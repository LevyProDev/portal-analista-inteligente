# crear_documentos_profesion.py
# Fase 3: crea documentos FICTICIOS para probar los perfiles profesionales
from pathlib import Path                  # herramienta para trabajar con rutas de archivos
from reportlab.lib.pagesizes import A4    # tamaño de hoja A4
from reportlab.pdfgen import canvas       # herramienta para "dibujar" texto en un PDF
 
CARPETA = Path(__file__).parent / "documentos_prueba"   # carpeta de documentos de prueba
 
ESTADO_FINANCIERO = [   # (subtítulo, párrafos) de cada página
    ("Ingresos", ["Los ingresos del tercer trimestre fueron: julio Bs 120.000, agosto Bs 135.000,",
                  "septiembre Bs 128.000. Total de ingresos informado: Bs 395.000."]),
    ("Gastos", ["Sueldos Bs 150.000, alquiler Bs 36.000, servicios Bs 18.000, marketing Bs 22.000.",
                "Total de gastos informado: Bs 226.000."]),
    ("Resultado", ["La utilidad del trimestre fue de Bs 169.000, con un margen del 43%.",
                   "El saldo bancario final al 30 de septiembre fue de Bs 82.150."]),
]
ACTA = [
    ("Asistentes y temas", ["Reunión del 14 de octubre de 2026. Asistentes: Rosa, Pedro y Elena.",
                            "Temas: cierre contable, contrato de alquiler y auditoría interna."]),
    ("Acuerdos", ["Rosa enviará el cierre contable de septiembre hasta el 10 de octubre.",
                  "Pedro devolverá el borrador del contrato de alquiler el 21 de octubre.",
                  "Elena coordinará la auditoría interna la semana del 26 de octubre."]),
]
MANUAL = [
    ("Mantenimiento preventivo", ["La bomba P-101 requiere mantenimiento cada 500 horas de operación.",
                                  "Responsable: jefe de mantenimiento. Registro en el formulario MNT-02."]),
    ("Límites de operación", ["La presión máxima de trabajo es de 8 bar y la temperatura máxima de 85 grados.",
                              "Si se superan los límites, se debe detener el equipo y avisar al supervisor."]),
    ("Calibración", ["Los sensores de presión se calibran cada 6 meses.",
                     "La calibración debe quedar registrada y firmada por el responsable técnico."]),
]
 
 
def crear_pdf(ruta, titulo, paginas):   # crea un PDF con una página por cada elemento de la lista
    pdf = canvas.Canvas(str(ruta), pagesize=A4)   # crea el PDF vacío
    alto = A4[1]   # altura de la hoja
    for numero, (subtitulo, parrafos) in enumerate(paginas, start=1):   # una página por elemento
        pdf.setFont("Helvetica-Bold", 18)   # letra grande y en negrita
        pdf.drawString(50, alto - 70, titulo)   # título del documento
        pdf.setFont("Helvetica-Bold", 14)   # letra mediana en negrita
        pdf.drawString(50, alto - 110, f"Página {numero} - {subtitulo}")   # subtítulo de la página
        pdf.setFont("Helvetica", 11)   # letra normal
        y = alto - 145   # posición vertical del primer párrafo
        for parrafo in parrafos:   # escribe cada párrafo
            pdf.drawString(50, y, parrafo)
            y -= 22   # baja una línea
        pdf.showPage()   # termina la página
    pdf.save()   # guarda el PDF
 
 
def main():   # función principal
    CARPETA.mkdir(exist_ok=True)   # crea la carpeta si no existe
    crear_pdf(CARPETA / "estado_financiero_demo.pdf", "Estado Financiero Trimestral (ficticio)", ESTADO_FINANCIERO)
    crear_pdf(CARPETA / "acta_reunion_demo.pdf", "Acta de Reunión (ficticia)", ACTA)
    crear_pdf(CARPETA / "manual_tecnico_demo.pdf", "Manual Técnico de Equipos (ficticio)", MANUAL)
    print("Documentos por profesión creados en documentos_prueba:")
    print("  estado_financiero_demo.pdf   (Contabilidad y Finanzas, 3 páginas)")
    print("  acta_reunion_demo.pdf        (Gestión, 2 páginas)")
    print("  manual_tecnico_demo.pdf      (Ingeniería, 3 páginas)")
    print("Tu contrato ficticio de la Clase 8 sirve para el perfil de Derecho.")
 
 
main()   # ejecuta el programa
