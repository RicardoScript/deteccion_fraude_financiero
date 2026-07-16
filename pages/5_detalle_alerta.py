import streamlit as st
from styles import apply_custom_styles
from utils.helpers import DETALLE_ALERTA

st.set_page_config(page_title="Detalle de alerta", layout="wide")
apply_custom_styles()

st.markdown("""
<div class="header">
    <h1>🔎 Detalle de alerta</h1>
    <span class="badge">Análisis de sospecha</span>
</div>
""", unsafe_allow_html=True)

# Datos de la alerta (ejemplo)
alerta = DETALLE_ALERTA

# Datos completos de la transacción
st.markdown("""
<div class="card">
    <h3>📋 Datos completos de la transacción</h3>
""", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <table style="width:100%; border-collapse:collapse;">
        <tr><td><strong>ID Alerta</strong></td><td>{alerta['id']}</td></tr>
        <tr><td><strong>Fecha / Step</strong></td><td>{alerta['fecha']} (step {alerta['step']})</td></tr>
        <tr><td><strong>Tipo</strong></td><td>{alerta['tipo']}</td></tr>
        <tr><td><strong>Monto</strong></td><td>€{alerta['monto']:,.2f}</td></tr>
        <tr><td><strong>Cuenta origen</strong></td><td>{alerta['origen']}</td></tr>
        <tr><td><strong>Saldo origen (antes)</strong></td><td>€{alerta['saldo_orig_antes']:,.2f}</td></tr>
        <tr><td><strong>Saldo origen (después)</strong></td><td>€{alerta['saldo_orig_despues']:,.2f}</td></tr>
    </table>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <table style="width:100%; border-collapse:collapse;">
        <tr><td><strong>Cuenta destino</strong></td><td>{alerta['destino']}</td></tr>
        <tr><td><strong>Saldo destino (antes)</strong></td><td>€{alerta['saldo_dest_antes']:,.2f}</td></tr>
        <tr><td><strong>Saldo destino (después)</strong></td><td>€{alerta['saldo_dest_despues']:,.2f}</td></tr>
        <tr><td><strong>Probabilidad de fraude</strong></td><td>{alerta['probabilidad']*100:.1f}%</td></tr>
        <tr><td><strong>Nivel de riesgo</strong></td><td><span class="status-badge risk-{alerta['riesgo'].lower()}">{alerta['riesgo']}</span></td></tr>
        <tr><td><strong>Estado actual</strong></td><td><span class="status-badge {alerta['estado'].lower()}">{alerta['estado']}</span></td></tr>
    </table>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Factores de riesgo
st.markdown("""
<div class="card">
    <h3>⚠️ Factores de riesgo detectados</h3>
    <ul>
""", unsafe_allow_html=True)
for factor in alerta['factores_riesgo']:
    st.markdown(f"<li>{factor}</li>", unsafe_allow_html=True)
st.markdown("</ul></div>", unsafe_allow_html=True)

# Historial de la cuenta
st.markdown("""
<div class="card">
    <h3>📜 Historial de la cuenta origen</h3>
    <div class="table-wrapper">
""", unsafe_allow_html=True)
import pandas as pd
df_hist = pd.DataFrame(alerta['historial_cuenta'])
st.dataframe(df_hist, use_container_width=True, hide_index=True)
st.markdown("</div></div>", unsafe_allow_html=True)

# Acciones del analista
st.markdown("""
<div class="card">
    <h3>🛠️ Acciones del analista</h3>
    <div style="display:flex; flex-wrap:wrap; gap:0.8rem; margin-top:0.5rem;">
        <button style="background:#16a34a; color:white; border:none; border-radius:40px; padding:0.5rem 1.5rem; font-weight:600;">✅ Aprobar</button>
        <button style="background:#dc2626; color:white; border:none; border-radius:40px; padding:0.5rem 1.5rem; font-weight:600;">🚫 Marcar fraude</button>
        <button style="background:#ca8a04; color:white; border:none; border-radius:40px; padding:0.5rem 1.5rem; font-weight:600;">🔒 Bloquear temporalmente</button>
        <button style="background:#2563eb; color:white; border:none; border-radius:40px; padding:0.5rem 1.5rem; font-weight:600;">📩 Enviar a revisión</button>
    </div>
    <div style="margin-top:1rem;">
        <label>Agregar observación</label>
        <textarea style="width:100%; border-radius:8px; border:1px solid #cbd5e1; padding:0.5rem; min-height:80px;"></textarea>
        <button style="background:#1e293b; color:white; border:none; border-radius:40px; padding:0.5rem 2rem; font-weight:600; margin-top:0.5rem;">Guardar observación</button>
    </div>
</div>
""", unsafe_allow_html=True)