import streamlit as st
from styles import apply_custom_styles

st.set_page_config(page_title="Dashboard", layout="wide")
apply_custom_styles()

st.markdown("""
<div class="header">
    <h1>📊 Dashboard de Fraude</h1>
    <span>Estadísticas</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>Resumen de transacciones</h3>
    <p>Aquí podrías mostrar métricas como total de transacciones, porcentaje de fraude, etc.</p>
    <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
        <div><strong>Total transacciones:</strong> 8,000</div>
        <div><strong>Fraudes detectados:</strong> 320 (4%)</div>
        <div><strong>Monto promedio:</strong> €245.50</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Puedes añadir más gráficos estáticos aquí