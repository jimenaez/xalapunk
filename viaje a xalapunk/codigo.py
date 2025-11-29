# ======= CONFIGURACIÓN FIJA =======

# Precios fijos que tú proporcionaste
PRECIO_AVION_JZ_CDMX_IDA = 700
PRECIO_AVION_CDMX_JZ_REGRESO = 1600

PRECIO_CAMION_CDMX_XALAPA = 800
PRECIO_CAMION_XALAPA_CDMX = 800

DESCUENTO_ESTUDIANTE = 0.5   # 50%
DESCUENTO_APLICA_A = "camion"  # solo camión

# Hospedaje ya dividido entre 5 personas
HOSPEDAJE_POR_PERSONA = 4985 / 5


# ======= SISTEMA =======

print("=== SISTEMA DE PRESUPUESTO DE VIAJE — VERSION PERSONALIZADA ===")

personas = []

while True:
    print("\nAgregar nueva persona (o escribe 'no' para terminar)")
    nombre = input("Nombre: ")
    if nombre.lower() == "no":
        break

    # Origen
    while True:
        origen = input("Origen (Juarez/CDMX): ").capitalize()
        if origen in ["Juarez", "Cdmx"]:
            break
        print("Origen inválido. Usa 'Juarez' o 'CDMX'.")

    # Descuento estudiante
    es_estudiante = input("¿Tiene descuento de estudiante? (si/no): ").lower()
    es_estudiante = (es_estudiante == "si")

    # Cálculo de transporte
    costo_transporte = 0

    # Personas de Juárez pagan avión de ida
    if origen == "Juarez":
        costo_transporte += PRECIO_AVION_JZ_CDMX_IDA

    # Camión CDMX → Xalapa
    if DESCUENTO_APLICA_A == "camion" and es_estudiante:
        costo_transporte += PRECIO_CAMION_CDMX_XALAPA * (1 - DESCUENTO_ESTUDIANTE)
    else:
        costo_transporte += PRECIO_CAMION_CDMX_XALAPA

    # Camión Xalapa → CDMX
    if DESCUENTO_APLICA_A == "camion" and es_estudiante:
        costo_transporte += PRECIO_CAMION_XALAPA_CDMX * (1 - DESCUENTO_ESTUDIANTE)
    else:
        costo_transporte += PRECIO_CAMION_XALAPA_CDMX

    # Personas de CDMX sí pagan avión de regreso a Juárez
    costo_transporte += PRECIO_AVION_CDMX_JZ_REGRESO

    # Guardar persona
    personas.append({
        "nombre": nombre,
        "origen": origen,
        "estudiante": es_estudiante,
        "transporte": costo_transporte,
        "hospedaje": HOSPEDAJE_POR_PERSONA,
        "total": costo_transporte + HOSPEDAJE_POR_PERSONA
    })

# ======= RESULTADOS =======
print("\n=== PRESUPUESTO FINAL POR PERSONA ===\n")

for p in personas:
    print(f"--- {p['nombre']} ---")
    print(f"  Origen: {p['origen']}")
    print(f"  Estudiante: {'Sí' if p['estudiante'] else 'No'}")
    print(f"  Transporte: ${p['transporte']:.2f}")
    print(f"  Hospedaje: ${p['hospedaje']:.2f}")
    print(f"  TOTAL: ${p['total']:.2f}\n")
