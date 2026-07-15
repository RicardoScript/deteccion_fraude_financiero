import streamlit as st
from styles import apply_custom_styles

# Configurar página
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Aplicar estilos CSS
apply_custom_styles()

# ----------------------------
# HEADER
# ----------------------------
st.markdown("""
<div class="header">
    <h1>🔒 Detección de Fraude</h1>
    <span>v1.0</span>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# DOS COLUMNAS: FORMULARIO Y RESULTADO (SIMULADO)
# ----------------------------
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📋 Datos de la transacción")
        
        # Campos de entrada (solo visuales, sin función)
        st.number_input("Monto (€)", min_value=0.01, value=150.0, step=10.0, format="%.2f", key="amount")
        st.selectbox("Tipo de transacción", ['Pago', 'Transferencia', 'Retiro', 'Compra en línea'], key="type")
        st.selectbox("Categoría del comercio", ['Retail', 'Alimentación', 'Entretenimiento', 'Viajes', 'Tecnología', 'Salud'], key="category")
        
        col_hour, col_age = st.columns(2)
        with col_hour:
            st.slider("Hora (0-23)", 0, 23, 14, key="hour")
        with col_age:
            st.number_input("Antigüedad (días)", 0, value=365, key="age")
        
        st.slider("Frecuencia (última hora)", 0, 10, 1, key="freq")
        
        # Botón (solo visual, no hace nada)
        st.button("🔍 Analizar transacción", use_container_width=True, key="analyze")
        
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📊 Resultado del análisis")
        
        # Mostrar siempre un resultado de ejemplo
        # Probabilidad simulada
        prob = 0.78  # valor fijo para demostración
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 1rem;">
            <div style="font-size: 0.9rem; color: #64748b;">Probabilidad de fraude</div>
            <div style="font-size: 2.8rem; font-weight: 700; color: #0f172a;">{prob*100:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Gauge simulado con Plotly (estático)
        import plotly.graph_objects as go
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = prob * 100,
            title = {'text': "Riesgo"},
            domain = {'x': [0, 1], 'y': [0, 1]},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1},
                'bar': {'color': "rgba(59, 130, 246, 0.8)"},
                'steps': [
                    {'range': [0, 30], 'color': "lightgreen"},
                    {'range': [30, 70], 'color': "gold"},
                    {'range': [70, 100], 'color': "salmon"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 70
                }
            }
        ))
        fig.update_layout(height=250, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        # Etiqueta de fraude (simulada)
        st.markdown("""
        <div style="text-align: center;">
            <span class="fraud-tag true">⚠️ FRAUDE DETECTADO</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# GRÁFICOS ESTÁTICOS (simulados con datos de ejemplo)
# ----------------------------
st.markdown("---")
st.markdown("### 📈 Análisis exploratorio de datos")

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    # Gráfico de barras simulado
    import pandas as pd
    import numpy as np
    np.random.seed(42)
    data = pd.DataFrame({
        'amount': np.random.gamma(2, 50, 1000),
        'fraud': np.random.choice([0,1], 1000, p=[0.9,0.1])
    })
    fraud_data = data[data['fraud'] == 1]['amount']
    non_fraud_data = data[data['fraud'] == 0]['amount']
    fig_hist = go.Figure()
    fig_hist.add_trace(go.Histogram(x=non_fraud_data, name='No fraude', marker_color='#3b82f6', opacity=0.6))
    fig_hist.add_trace(go.Histogram(x=fraud_data, name='Fraude', marker_color='#ef4444', opacity=0.6))
    fig_hist.update_layout(
        barmode='overlay',
        title='Distribución de montos',
        xaxis_title='Monto (€)',
        yaxis_title='Frecuencia',
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation='h', y=1.1)
    )
    st.plotly_chart(fig_hist, use_container_width=True, config={'displayModeBar': False})

with col_chart2:
    # Gráfico de tipos de transacción
    tipos = ['Pago', 'Transferencia', 'Retiro', 'Compra en línea']
    counts = [400, 200, 100, 300]
    fraud_counts = [40, 50, 20, 30]
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(x=tipos, y=counts, name='No fraude', marker_color='#3b82f6', opacity=0.7))
    fig_bar.add_trace(go.Bar(x=tipos, y=fraud_counts, name='Fraude', marker_color='#ef4444', opacity=0.7))
    fig_bar.update_layout(
        barmode='group',
        title='Transacciones por tipo',
        xaxis_title='Tipo',
        yaxis_title='Cantidad',
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation='h', y=1.1)
    )
    st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})

# ----------------------------
# PIE DE PÁGINA
# ----------------------------
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #94a3b8; font-size: 0.8rem; border-top: 1px solid #e2e8f0; padding-top: 1rem;">
    Sistema de Detección de Fraude Financiero · Interfaz de demostración
</div>
""", unsafe_allow_html=True)