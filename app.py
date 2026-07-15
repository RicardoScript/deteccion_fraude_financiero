import streamlit as st
from styles import apply_custom_styles
from utils.helpers import RESUMEN
import plotly.graph_objects as go

st.set_page_config(
    page_title="Detección de Fraude Financiero",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

apply_custom_styles()

# Encabezado
st.markdown("""
<div class="header">
    <h1>🔒 Detección de Fraude Financiero</h1>
</div>
""", unsafe_allow_html=True)

# Métricas principales en fila
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="metric-label">Filas procesadas</div>
        <div class="metric-value">{RESUMEN['filas_salida']:,}</div>
        <div class="metric-change green">✓ Sin pérdida</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="metric-label">Columnas finales</div>
        <div class="metric-value">{RESUMEN['columnas_salida']}</div>
        <div class="metric-change blue">+{RESUMEN['columnas_salida'] - RESUMEN['columnas_entrada']} nuevas</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="metric-label">Fraudes detectados</div>
        <div class="metric-value">{RESUMEN['fraudes']:,}</div>
        <div class="metric-change red">{RESUMEN['porcentaje_fraude']:.2f}% del total</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="card">
        <div class="metric-label">Particiones (Parquet)</div>
        <div class="metric-value">{RESUMEN['particiones']}</div>
        <div class="metric-change blue">por tipo</div>
    </div>
    """, unsafe_allow_html=True)

# Gráfico de fraude por tipo
fraudes_por_tipo = RESUMEN['fraudes_por_tipo']
tipos = list(fraudes_por_tipo.keys())
cantidades = list(fraudes_por_tipo.values())

fig = go.Figure(data=[
    go.Bar(x=tipos, y=cantidades, marker_color=['#ef4444' if t in ['TRANSFER','CASH_OUT'] else '#94a3b8' for t in tipos])
])
fig.update_layout(
    title="Fraudes por tipo de transacción",
    xaxis_title="Tipo",
    yaxis_title="Número de fraudes",
    height=300,
    margin=dict(l=20, r=20, t=40, b=20),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#1e293b')
)
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# Descripción del proyecto
st.markdown("""
<div class="card">
    <h3>📌 Resumen del proyecto</h3>
    <p>Este proyecto implementa un <strong>pipeline ETL distribuido</strong> sobre el dataset <strong>PaySim</strong> (6.362.620 transacciones) 
    para la detección de fraude financiero. Los datos se limpian, transforman y enriquecen con variables de dominio, 
    y se almacenan en formato <strong>Parquet con compresión Snappy</strong>, particionado por tipo de transacción.</p>
    <p><strong>Arquitectura:</strong> Raw Data → Bronze → Silver → Gold → Storage.</p>
    <p><strong>Resultado:</strong> 22 columnas finales (11 nuevas), sin pérdida de registros, y preparado para Machine Learning (Fase III).</p>
</div>
""", unsafe_allow_html=True)

# Navegación rápida
st.markdown("""
<div style="display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center; margin-top: 1rem;">
    <a href="/Pipeline" target="_self" style="background:#3b82f6; color:white; padding:0.5rem 1.5rem; border-radius:40px; text-decoration:none; font-weight:500;">▶ Ver Pipeline ETL</a>
    <a href="/Datos" target="_self" style="background:#1e293b; color:white; padding:0.5rem 1.5rem; border-radius:40px; text-decoration:none; font-weight:500;">📊 Explorar Datos</a>
    <a href="/Modelo" target="_self" style="background:#0f172a; color:white; padding:0.5rem 1.5rem; border-radius:40px; text-decoration:none; font-weight:500;">🤖 Simular Modelo</a>
</div>
""", unsafe_allow_html=True)