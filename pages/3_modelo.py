import streamlit as st
from styles import apply_custom_styles
import plotly.graph_objects as go

st.set_page_config(page_title="Simulación de Modelo", layout="wide")
apply_custom_styles()

st.markdown("""
<div class="header">
    <h1>🤖 Simulación de Modelo</h1>
    <span class="badge">Clasificación</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>📋 Datos de la transacción (simulados)</h3>
    <p>Complete los campos para obtener una predicción de fraude <strong>(solo visual, sin lógica real)</strong>.</p>
""", unsafe_allow_html=True)

# Formulario simulado
col1, col2 = st.columns(2)
with col1:
    monto = st.number_input("Monto (€)", min_value=0.01, value=1500.0, step=100.0, format="%.2f")
    tipo = st.selectbox("Tipo de transacción", ["TRANSFER", "CASH_OUT", "PAYMENT", "CASH_IN", "DEBIT"])
    hora = st.slider("Hora del día", 0, 23, 14)
with col2:
    antiguedad = st.number_input("Antigüedad de la cuenta (días)", min_value=0, value=365)
    frecuencia = st.slider("Frecuencia (última hora)", 0, 10, 2)
    saldo_orig = st.number_input("Saldo origen (€)", min_value=0.0, value=5000.0, step=100.0)

# Botón de predicción simulado
if st.button("🔍 Analizar transacción", use_container_width=True):
    # Simular resultado (fijo para demo)
    prob = 0.78 if tipo in ["TRANSFER", "CASH_OUT"] else 0.12
    pred = prob > 0.5

    # Mostrar resultados
    st.markdown("""
    <div class="card" style="margin-top:1rem;">
        <h3>📊 Resultado del análisis</h3>
    """, unsafe_allow_html=True)

    col_res1, col_res2 = st.columns([1, 1])
    with col_res1:
        st.markdown(f"""
        <div style="text-align:center;">
            <div style="font-size:0.9rem; color:#64748b;">Probabilidad de fraude</div>
            <div style="font-size:2.8rem; font-weight:700; color:#0f172a;">{prob*100:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

        # Gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prob*100,
            title={'text': "Riesgo"},
            gauge={
                'axis': {'range': [None, 100]},
                'steps': [
                    {'range': [0, 30], 'color': 'lightgreen'},
                    {'range': [30, 70], 'color': 'gold'},
                    {'range': [70, 100], 'color': 'salmon'}
                ],
                'threshold': {'line': {'color': 'red', 'width': 4}, 'thickness': 0.75, 'value': 70}
            }
        ))
        fig.update_layout(height=250, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    with col_res2:
        if pred:
            st.markdown('<div style="text-align:center;"><span class="fraud-tag true">⚠️ FRAUDE DETECTADO</span></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="text-align:center;"><span class="fraud-tag false">✅ TRANSACCIÓN SEGURA</span></div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="margin-top:1rem; text-align:center; color:#475569;">
            <strong>Monto:</strong> {monto:.2f} €<br>
            <strong>Tipo:</strong> {tipo}<br>
            <strong>Hora:</strong> {hora}:00
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("👆 Complete los datos y presione el botón para ver una predicción de ejemplo.")

st.markdown("</div>", unsafe_allow_html=True)
