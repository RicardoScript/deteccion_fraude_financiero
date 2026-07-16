import streamlit as st
from styles import apply_custom_styles
from utils.helpers import SAMPLE_TRANSACTION
import plotly.graph_objects as go

st.set_page_config(page_title="Análisis de transacción", layout="wide")
apply_custom_styles()

st.markdown("""
<div class="header">
    <h1>🔍 Análisis de transacción</h1>
    <span class="badge">Ingreso manual</span>
</div>
""", unsafe_allow_html=True)

# Formulario
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📋 Datos de la transacción")

    col1, col2 = st.columns(2)
    with col1:
        tx_id = st.text_input("ID de transacción", value=SAMPLE_TRANSACTION["id"])
        tx_type = st.selectbox("Tipo de transacción", ["TRANSFER", "CASH_OUT", "PAYMENT", "CASH_IN", "DEBIT"], index=0)
        amount = st.number_input("Monto (€)", min_value=0.01, value=SAMPLE_TRANSACTION["amount"], step=100.0, format="%.2f")
        name_orig = st.text_input("Cuenta origen", value=SAMPLE_TRANSACTION["nameOrig"])
        oldbalance_orig = st.number_input("Saldo inicial origen (€)", min_value=0.0, value=SAMPLE_TRANSACTION["oldbalanceOrg"], step=100.0, format="%.2f")
        newbalance_orig = st.number_input("Saldo final origen (€)", min_value=0.0, value=SAMPLE_TRANSACTION["newbalanceOrig"], step=100.0, format="%.2f")
    with col2:
        name_dest = st.text_input("Cuenta destino", value=SAMPLE_TRANSACTION["nameDest"])
        oldbalance_dest = st.number_input("Saldo inicial destino (€)", min_value=0.0, value=SAMPLE_TRANSACTION["oldbalanceDest"], step=100.0, format="%.2f")
        newbalance_dest = st.number_input("Saldo final destino (€)", min_value=0.0, value=SAMPLE_TRANSACTION["newbalanceDest"], step=100.0, format="%.2f")
        step = st.number_input("Step (hora simulada)", min_value=0, value=SAMPLE_TRANSACTION["step"], step=1)

    # Botón de análisis (simulado)
    if st.button("📊 Analizar transacción", use_container_width=True):
        # Simulación de resultado (fijo para demo)
        prob = 0.87  # probabilidad alta para ejemplo
        riesgo = "Alto"
        recomendacion = "Bloquear temporalmente"
        if prob > 0.7:
            prediccion = "Posible fraude"
            clase = "fraude"
        else:
            prediccion = "Transacción normal"
            clase = "normal"

        # Mostrar resultado
        st.markdown("---")
        st.markdown("### 📊 Resultado del análisis")

        col_res1, col_res2 = st.columns([1, 2])
        with col_res1:
            st.markdown(f"""
            <div style="text-align:center; padding:1rem;">
                <div style="font-size:0.9rem; color:#64748b;">Predicción</div>
                <div style="font-size:1.6rem; font-weight:700; margin:0.5rem 0;">
                    <span class="status-badge {clase}">{prediccion}</span>
                </div>
                <div style="font-size:0.9rem; color:#64748b;">Nivel de riesgo</div>
                <div style="font-size:1.6rem; font-weight:700; margin:0.5rem 0;">
                    <span class="status-badge risk-{riesgo.lower()}">{riesgo}</span>
                </div>
                <div style="font-size:0.9rem; color:#64748b;">Probabilidad de fraude</div>
                <div style="font-size:1.6rem; font-weight:700;">{prob*100:.1f}%</div>
                <div style="font-size:0.9rem; color:#64748b; margin-top:1rem;">Recomendación</div>
                <div style="font-size:1.2rem; font-weight:600; background:#f1f5f9; border-radius:40px; padding:0.3rem 1rem; display:inline-block;">{recomendacion}</div>
            </div>
            """, unsafe_allow_html=True)

        with col_res2:
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

    st.markdown('</div>', unsafe_allow_html=True)

# Nota
st.info("ℹ️ Esta es una demostración visual. Los resultados son simulados para ilustrar la interfaz.")