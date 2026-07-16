import pandas as pd

# Datos para el dashboard
DASHBOARD_METRICS = {
    "total_transacciones": 6_362_620,
    "normales": 6_354_407,
    "sospechosas": 8_213,
    "fraudes_confirmados": 7_891,
    "alertas_pendientes": 322
}

# Datos para gráfico de tipo de transacción (distribución general)
TRANSACTION_TYPES = {
    "TRANSFER": 1_500_000,
    "CASH_OUT": 1_200_000,
    "PAYMENT": 2_800_000,
    "CASH_IN": 600_000,
    "DEBIT": 262_620
}

# Datos de ejemplo para análisis de transacción (precargados)
SAMPLE_TRANSACTION = {
    "id": "TX-2024-001234",
    "type": "TRANSFER",
    "amount": 4500.00,
    "nameOrig": "C123456789",
    "oldbalanceOrg": 5000.00,
    "newbalanceOrig": 500.00,
    "nameDest": "M987654321",
    "oldbalanceDest": 1000.00,
    "newbalanceDest": 5500.00,
    "step": 132
}

# Datos para historial de cuenta (ejemplo)
HISTORIAL_DATA = [
    {"step": 120, "type": "TRANSFER", "amount": 200.00, "oldbalanceOrg": 1000.00, "newbalanceOrig": 800.00, "resultado": "normal", "riesgo": "bajo"},
    {"step": 115, "type": "PAYMENT", "amount": 50.00, "oldbalanceOrg": 1050.00, "newbalanceOrig": 1000.00, "resultado": "normal", "riesgo": "bajo"},
    {"step": 110, "type": "CASH_OUT", "amount": 5000.00, "oldbalanceOrg": 6050.00, "newbalanceOrig": 1050.00, "resultado": "sospechoso", "riesgo": "alto"},
    {"step": 105, "type": "TRANSFER", "amount": 1500.00, "oldbalanceOrg": 7550.00, "newbalanceOrig": 6050.00, "resultado": "normal", "riesgo": "medio"},
    {"step": 100, "type": "PAYMENT", "amount": 100.00, "oldbalanceOrg": 7650.00, "newbalanceOrig": 7550.00, "resultado": "normal", "riesgo": "bajo"}
]

# Datos para alertas
ALERTAS_DATA = [
    {"id": "AL-001", "tipo": "TRANSFER", "monto": 4500.00, "origen": "C123456789", "destino": "M987654321", "probabilidad": 0.87, "riesgo": "alto", "estado": "Pendiente"},
    {"id": "AL-002", "tipo": "CASH_OUT", "monto": 12000.00, "origen": "C456789012", "destino": "C345678901", "probabilidad": 0.94, "riesgo": "alto", "estado": "Pendiente"},
    {"id": "AL-003", "tipo": "TRANSFER", "monto": 350.00, "origen": "C789012345", "destino": "M456789012", "probabilidad": 0.65, "riesgo": "medio", "estado": "Revisada"},
    {"id": "AL-004", "tipo": "CASH_OUT", "monto": 8000.00, "origen": "C234567890", "destino": "C567890123", "probabilidad": 0.92, "riesgo": "alto", "estado": "Bloqueada"},
    {"id": "AL-005", "tipo": "PAYMENT", "monto": 2000.00, "origen": "C345678901", "destino": "M678901234", "probabilidad": 0.45, "riesgo": "medio", "estado": "Descartada"},
    {"id": "AL-006", "tipo": "TRANSFER", "monto": 7500.00, "origen": "C456789012", "destino": "C789012345", "probabilidad": 0.89, "riesgo": "alto", "estado": "Pendiente"},
    {"id": "AL-007", "tipo": "CASH_OUT", "monto": 1500.00, "origen": "C567890123", "destino": "M890123456", "probabilidad": 0.58, "riesgo": "medio", "estado": "Revisada"},
]

# Datos para detalle de alerta (ejemplo)
DETALLE_ALERTA = {
    "id": "AL-001",
    "fecha": "2024-01-15",
    "step": 132,
    "tipo": "TRANSFER",
    "monto": 4500.00,
    "origen": "C123456789",
    "saldo_orig_antes": 5000.00,
    "saldo_orig_despues": 500.00,
    "destino": "M987654321",
    "saldo_dest_antes": 1000.00,
    "saldo_dest_despues": 5500.00,
    "probabilidad": 0.87,
    "riesgo": "alto",
    "estado": "Pendiente",
    "factores_riesgo": [
        "Tipo de transacción de alto riesgo (TRANSFER)",
        "Monto elevado (€4,500)",
        "Saldo origen reducido a €500 después de la transacción",
        "Error de balance en origen: 0.05% de discrepancia",
        "Historial previo de la cuenta: 2 alertas en los últimos 30 días"
    ],
    "historial_cuenta": [
        {"step": 120, "tipo": "TRANSFER", "monto": 200.00, "saldo": 1000.00, "resultado": "normal"},
        {"step": 115, "tipo": "PAYMENT", "monto": 50.00, "saldo": 1050.00, "resultado": "normal"},
        {"step": 110, "tipo": "CASH_OUT", "monto": 5000.00, "saldo": 6050.00, "resultado": "sospechoso"},
    ]
}

# Funciones para obtener datos como DataFrames
def get_historial_df():
    return pd.DataFrame(HISTORIAL_DATA)

def get_alertas_df():
    return pd.DataFrame(ALERTAS_DATA)

def get_transaction_types_df():
    return pd.DataFrame(list(TRANSACTION_TYPES.items()), columns=["tipo", "cantidad"])