import streamlit as st
from styles import apply_custom_styles
from utils.helpers import DASHBOARD_METRICS, TRANSACTION_TYPES
import plotly.graph_objects as go

st.set_page_config(
    page_title="Dashboard - Detección de Fraude",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_styles()

# Encabezado
st.markdown("""
<div class="header">
    <h1>📊 Dashboard de Fraude Financiero</h1>
    <span class="badge">Sistema de Alerta Temprana</span>
</div>
""", unsafe_allow_html=True)

# Métricas principales
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <div class="metric-label">Total transacciones</div>
        <div class="metric-value">{DASHBOARD_METRICS['total_transacciones']:,}</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <div class="metric-label">Normales</div>
        <div class="metric-value" style="color:#16a34a;">{DASHBOARD_METRICS['normales']:,}</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <div class="metric-label">Sospechosas</div>
        <div class="metric-value" style="color:#ca8a04;">{DASHBOARD_METRICS['sospechosas']:,}</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <div class="metric-label">Fraudes confirmados</div>
        <div class="metric-value" style="color:#dc2626;">{DASHBOARD_METRICS['fraudes_confirmados']:,}</div>
    </div>
    """, unsafe_allow_html=True)
with col5:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <div class="metric-label">Alertas pendientes</div>
        <div class="metric-value" style="color:#2563eb;">{DASHBOARD_METRICS['alertas_pendientes']}</div>
    </div>
    """, unsafe_allow_html=True)

# Gráfico de transacciones por tipo
st.markdown("""
<div class="card">
    <h3>📈 Transacciones por tipo</h3>
""", unsafe_allow_html=True)

tipos = list(TRANSACTION_TYPES.keys())
cantidades = list(TRANSACTION_TYPES.values())
colores = ['#ef4444' if t in ['TRANSFER','CASH_OUT'] else '#3b82f6' for t in tipos]

fig = go.Figure(data=[go.Bar(x=tipos, y=cantidades, marker_color=colores)])
fig.update_layout(
    xaxis_title="Tipo de transacción",
    yaxis_title="Cantidad",
    height=300,
    margin=dict(l=20, r=20, t=20, b=20),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#1e293b')
)
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
st.markdown("</div>", unsafe_allow_html=True)

# Accesos rápidos
st.markdown("""
<div class="card">
    <h3>⚡ Accesos rápidos</h3>
    <div class="quick-access">
        <a href="/An%C3%A1lisis_de_transacci%C3%B3n" target="_self">🔍 Analizar transacción</a>
        <a href="/Carga_masiva" target="_self" class="secondary">📤 Cargar archivo</a>
        <a href="/Alertas" target="_self" class="outline">🚨 Ver alertas sospechosas</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Pie de página
st.markdown("""
<div style="text-align:center; color:#94a3b8; font-size:0.8rem; border-top:1px solid #e2e8f0; padding-top:1rem; margin-top:1rem;">
    Sistema de Detección de Fraude Financiero · Interfaz de demostración
</div>
""", unsafe_allow_html=True)