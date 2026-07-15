import streamlit as st
from styles import apply_custom_styles
from utils.helpers import RESUMEN, MUESTRA_DATOS
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Datos", layout="wide")
apply_custom_styles()

st.markdown("""
<div class="header">
    <h1>📊 Exploración de datos</h1>
    <span class="badge">Dataset procesado</span>
</div>
""", unsafe_allow_html=True)

# Muestra de datos
st.markdown("""
<div class="card">
    <h3>📋 Muestra de transacciones (5 registros)</h3>
""", unsafe_allow_html=True)
df_muestra = pd.DataFrame(MUESTRA_DATOS)
st.dataframe(df_muestra, use_container_width=True, hide_index=True)
st.markdown("</div>", unsafe_allow_html=True)

# Distribución de la variable objetivo
st.markdown("""
<div class="card">
    <h3>🎯 Distribución de la variable objetivo (isFraud)</h3>
""", unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    fig_pie = go.Figure(data=[go.Pie(
        labels=['No fraude', 'Fraude'],
        values=[RESUMEN['no_fraudes'], RESUMEN['fraudes']],
        marker=dict(colors=['#3b82f6', '#ef4444']),
        hole=0.4,
        textinfo='percent+label'
    )])
    fig_pie.update_layout(height=300, margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig_pie, use_container_width=True, config={'displayModeBar': False})

with col2:
    st.markdown(f"""
    <div style="display: flex; flex-direction: column; justify-content: center; height:100%;">
        <div><strong>Total transacciones:</strong> {RESUMEN['filas_salida']:,}</div>
        <div><strong>No fraude:</strong> {RESUMEN['no_fraudes']:,} ({100 - RESUMEN['porcentaje_fraude']:.2f}%)</div>
        <div><strong>Fraude:</strong> {RESUMEN['fraudes']:,} ({RESUMEN['porcentaje_fraude']:.2f}%)</div>
        <div style="margin-top:0.5rem; color:#64748b;">⚠️ Dataset altamente desbalanceado</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Gráfico de montos (simulado)
st.markdown("""
<div class="card">
    <h3>💰 Distribución de montos</h3>
""", unsafe_allow_html=True)
# Generar datos de ejemplo para el histograma
import numpy as np
np.random.seed(42)
amounts = np.random.gamma(2, 50, 1000)
fraud_amounts = np.random.gamma(3, 100, 100)
fig_hist = go.Figure()
fig_hist.add_trace(go.Histogram(x=amounts, name='No fraude', marker_color='#3b82f6', opacity=0.6, nbinsx=30))
fig_hist.add_trace(go.Histogram(x=fraud_amounts, name='Fraude', marker_color='#ef4444', opacity=0.6, nbinsx=30))
fig_hist.update_layout(
    barmode='overlay',
    xaxis_title='Monto (€)',
    yaxis_title='Frecuencia',
    height=300,
    margin=dict(l=20, r=20, t=20, b=20),
    legend=dict(orientation='h', y=1.1)
)
st.plotly_chart(fig_hist, use_container_width=True, config={'displayModeBar': False})
st.markdown("</div>", unsafe_allow_html=True)

# Columnas creadas
st.markdown("""
<div class="card">
    <h3>🧩 Nuevas columnas añadidas</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px,1fr)); gap:0.8rem;">
        <div style="background:#f1f5f9; padding:0.5rem; border-radius:8px;"><strong>hour_of_day</strong><br>Hora simulada (0-23)</div>
        <div style="background:#f1f5f9; padding:0.5rem; border-radius:8px;"><strong>simulation_day</strong><br>Día simulado</div>
        <div style="background:#f1f5f9; padding:0.5rem; border-radius:8px;"><strong>avg_amount_by_type</strong><br>Promedio de monto por tipo</div>
        <div style="background:#f1f5f9; padding:0.5rem; border-radius:8px;"><strong>ratio_amount_vs_type_avg</strong><br>Ratio vs promedio</div>
        <div style="background:#f1f5f9; padding:0.5rem; border-radius:8px;"><strong>amount_to_oldbalanceOrig_ratio</strong><br>Proporción del saldo</div>
        <div style="background:#f1f5f9; padding:0.5rem; border-radius:8px;"><strong>amount_log</strong><br>Log1p(amount)</div>
        <div style="background:#f1f5f9; padding:0.5rem; border-radius:8px;"><strong>amount_norm</strong><br>Min-Max normalizado</div>
        <div style="background:#f1f5f9; padding:0.5rem; border-radius:8px;"><strong>balance_error_orig</strong><br>Error de balance origen</div>
        <div style="background:#f1f5f9; padding:0.5rem; border-radius:8px;"><strong>balance_error_dest</strong><br>Error de balance destino</div>
        <div style="background:#f1f5f9; padding:0.5rem; border-radius:8px;"><strong>high_risk_type</strong><br>TRANSFER/CASH_OUT</div>
        <div style="background:#f1f5f9; padding:0.5rem; border-radius:8px;"><strong>is_merchant_dest</strong><br>Destinatario comercio</div>
    </div>
    <div style="margin-top:1rem; color:#64748b;">Total: 11 columnas nuevas → 22 columnas finales</div>
</div>
""", unsafe_allow_html=True)