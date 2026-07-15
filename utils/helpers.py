# Datos quemados basados en la Fase II

RESUMEN = {
    "filas_entrada": 6362620,
    "filas_salida": 6362620,
    "columnas_entrada": 11,
    "columnas_salida": 22,
    "duplicados": 0,
    "fraudes": 8213,
    "no_fraudes": 6354407,
    "porcentaje_fraude": 0.129,
    "tipos": ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"],
    "fraudes_por_tipo": {"CASH_OUT": 4116, "TRANSFER": 4097, "PAYMENT": 0, "CASH_IN": 0, "DEBIT": 0},
    "particiones": 5,
    "tiempo_escritura": 198.66
}

LOGS_ETL = [
    ("T1 - Limpieza de duplicados y nulos", 6362620, 6362620, 0, 11, 11, "Sin duplicados ni nulos"),
    ("T2 - Corrección de tipos y estandarización", 6362620, 6362620, 0, 11, 13, "Tipos corregidos, variables temporales"),
    ("T3 - Feature Engineering", 6362620, 6362620, 0, 13, 16, "Ratios financieros y promedios"),
    ("T4 - Normalización", 6362620, 6362620, 0, 16, 18, "Log1p + Min-Max sobre amount"),
    ("T5 - Variables de dominio financiero", 6362620, 6362620, 0, 18, 22, "Errores de balance y tipo de riesgo")
]

MUESTRA_DATOS = [
    {"step": 1, "type": "PAYMENT", "amount": 9839.64, "nameOrig": "C1231006815", "oldbalanceOrg": 170136.0, "newbalanceOrig": 160296.36, "nameDest": "M1979787155", "oldbalanceDest": 0.0, "newbalanceDest": 0.0, "isFraud": 0, "isFlaggedFraud": 0},
    {"step": 1, "type": "PAYMENT", "amount": 1864.28, "nameOrig": "C1666544295", "oldbalanceOrg": 21249.0, "newbalanceOrig": 19384.72, "nameDest": "M2044282225", "oldbalanceDest": 0.0, "newbalanceDest": 0.0, "isFraud": 0, "isFlaggedFraud": 0},
    {"step": 1, "type": "TRANSFER", "amount": 181.0, "nameOrig": "C1305486145", "oldbalanceOrg": 181.0, "newbalanceOrig": 0.0, "nameDest": "C553264065", "oldbalanceDest": 0.0, "newbalanceDest": 0.0, "isFraud": 1, "isFlaggedFraud": 0},
    {"step": 1, "type": "CASH_OUT", "amount": 181.0, "nameOrig": "C840083671", "oldbalanceOrg": 181.0, "newbalanceOrig": 0.0, "nameDest": "C38997010", "oldbalanceDest": 21182.0, "newbalanceDest": 0.0, "isFraud": 1, "isFlaggedFraud": 0},
    {"step": 1, "type": "PAYMENT", "amount": 11668.14, "nameOrig": "C2048537720", "oldbalanceOrg": 41554.0, "newbalanceOrig": 29885.86, "nameDest": "M1230701704", "oldbalanceDest": 0.0, "newbalanceDest": 0.0, "isFraud": 0, "isFlaggedFraud": 0},
]