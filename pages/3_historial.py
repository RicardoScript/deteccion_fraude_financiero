import streamlit as st
from styles import apply_custom_styles
from utils.helpers import get_historial_df

st.set_page_config(page_title="Historial de cuenta", layout="wide")
apply_custom_styles()

st.markdown("""
<div class="header">
    <h1>📜 Historial de cuenta</h1>
    <span class="badge">Comportamiento anterior</span>
</div>
""", unsafe_allow_html=True)

# Buscadores
st.markdown("""
<div class="card">
    <h3>🔎 Buscar cuenta</h3>
    <div style="display:flex; flex-wrap:wrap; gap:1rem;">
        <div style="flex:1; min-width:200px;">
            <label>Cuenta origen</label>
            <input type="text" placeholder="Ej: C123456789" style="width:100%; padding:0.5rem; border-radius:8px; border:1px solid #cbd5e1;">
        </div>
        <div style="flex:1; min-width:200px;">
            <label>Cuenta destino</label>
            <input type="text" placeholder="Ej: M987654321" style="width:100%; padding:0.5rem; border-radius:8px; border:1px solid #cbd5e1;">
        </div>
        <div style="display:flex; align-items:flex-end;">
            <button style="background:#3b82f6; color:white; border:none; border-radius:40px; padding:0.5rem 2rem; font-weight:600;">Buscar</button>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Datos de historial (ejemplo)
df_historial = get_historial_df()

# Métricas adicionales
st.markdown("""
<div class="card">
    <h3>📊 Indicadores de la cuenta</h3>
    <div class="metrics-grid">
        <div class="metric-item"><div class="value">5</div><div class="label">Transacciones recientes</div></div>
        <div class="metric-item"><div class="value">€1,370</div><div class="label">Monto promedio</div></div>
        <div class="metric-item"><div class="value" style="color:#dc2626;">1</div><div class="label">Alertas anteriores</div></div>
        <div class="metric-item"><div class="value">TRANSFER</div><div class="label">Tipo más frecuente</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

# Tabla de transacciones
st.markdown("""
<div class="card">
    <h3>📋 Transacciones anteriores</h3>
    <div class="table-wrapper">
""", unsafe_allow_html=True)

# Mostrar tabla con estilo
st.dataframe(df_historial, use_container_width=True, hide_index=True)

# Últimas sospechosas
st.markdown("""
<h4 style="margin-top:1.5rem;">⚠️ Últimas transacciones sospechosas</h4>
""", unsafe_allow_html=True)
sospechosas = df_historial[df_historial["resultado"] == "sospechoso"]
if not sospechosas.empty:
    st.dataframe(sospechosas, use_container_width=True, hide_index=True)
else:
    st.info("No hay transacciones sospechosas recientes.")

st.markdown("</div>", unsafe_allow_html=True)