import streamlit as st
from styles import apply_custom_styles
from utils.helpers import LOGS_ETL, RESUMEN
import pandas as pd

st.set_page_config(page_title="Pipeline ETL", layout="wide")
apply_custom_styles()

st.markdown("""
<div class="header">
    <h1>⚙️ Pipeline ETL</h1>
    <span class="badge">Extracción · Transformación · Carga</span>
</div>
""", unsafe_allow_html=True)

# Diagrama en texto (puedes reemplazar por imagen o Mermaid)
st.markdown("""
<div class="card">
    <h3>📐 Arquitectura del pipeline</h3>
    <pre style="background:#f1f5f9; padding:1rem; border-radius:8px; font-size:0.9rem; line-height:1.6;">
    Fuente (CSV)  →  Extract (Bronze)  →  Transform (Silver → Gold)  →  Load (Parquet + Snappy)
    PaySim1        Validación inicial     T1: Limpieza de duplicados    Particionado por type
    6.362.620      Columnas esperadas     T2: Tipos y estandarización   Ruta: FaseII_Fraude_Procesado_Parquet
    11 columnas    Reporte de nulos       T3: Feature Engineering
                   Duplicados: 0          T4: Normalización
                                          T5: Variables de dominio
    </pre>
</div>
""", unsafe_allow_html=True)

# Tabla de logs
st.markdown("""
<div class="card">
    <h3>📋 Registro de transformaciones (ETL Logs)</h3>
""", unsafe_allow_html=True)

# Convertir LOGS_ETL a DataFrame para mostrarlo bonito
df_logs = pd.DataFrame(LOGS_ETL, columns=["Paso", "Filas antes", "Filas después", "Diferencia", "Columnas antes", "Columnas después", "Detalle"])
st.dataframe(df_logs, use_container_width=True, hide_index=True)

st.markdown("</div>", unsafe_allow_html=True)

# Resumen de transformaciones en tarjetas
st.markdown("""
<div class="card">
    <h3>📈 Detalle de transformaciones</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px,1fr)); gap:1rem;">
""", unsafe_allow_html=True)

for paso in LOGS_ETL:
    nombre = paso[0]
    detalle = paso[6]
    st.markdown(f"""
    <div style="background:#f8fafc; border-radius:12px; padding:1rem; border-left:4px solid #3b82f6;">
        <strong>{nombre}</strong>
        <div style="font-size:0.9rem; color:#475569; margin-top:0.3rem;">{detalle}</div>
        <div style="font-size:0.8rem; color:#64748b; margin-top:0.3rem;">Filas: {paso[1]:,} → {paso[2]:,} · Columnas: {paso[4]} → {paso[5]}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# Métricas de almacenamiento
st.markdown(f"""
<div class="card">
    <h3>💾 Almacenamiento final</h3>
    <div style="display: flex; flex-wrap: wrap; gap: 2rem;">
        <div><span class="metric-label">Formato</span><br><strong>Parquet + Snappy</strong></div>
        <div><span class="metric-label">Particiones</span><br><strong>{RESUMEN['particiones']}</strong> (por type)</div>
        <div><span class="metric-label">Tiempo de escritura</span><br><strong>{RESUMEN['tiempo_escritura']} seg</strong></div>
        <div><span class="metric-label">Integridad</span><br><span class="green">✅ Filas escritas = filas leídas</span></div>
    </div>
</div>
""", unsafe_allow_html=True)