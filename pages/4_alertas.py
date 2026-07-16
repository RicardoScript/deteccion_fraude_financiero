import streamlit as st
from styles import apply_custom_styles
from utils.helpers import get_alertas_df

st.set_page_config(page_title="Alertas sospechosas", layout="wide")
apply_custom_styles()

st.markdown("""
<div class="header">
    <h1>🚨 Alertas sospechosas</h1>
    <span class="badge">Listado de posibles fraudes</span>
</div>
""", unsafe_allow_html=True)

# Filtros
st.markdown("""
<div class="card">
    <h3>🔍 Filtrar alertas</h3>
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px,1fr)); gap:1rem;">
        <div>
            <label>Nivel de riesgo</label>
            <select style="width:100%; padding:0.4rem; border-radius:8px; border:1px solid #cbd5e1;">
                <option>Todos</option>
                <option>Alto</option>
                <option>Medio</option>
                <option>Bajo</option>
            </select>
        </div>
        <div>
            <label>Tipo de transacción</label>
            <select style="width:100%; padding:0.4rem; border-radius:8px; border:1px solid #cbd5e1;">
                <option>Todos</option>
                <option>TRANSFER</option>
                <option>CASH_OUT</option>
                <option>PAYMENT</option>
                <option>CASH_IN</option>
                <option>DEBIT</option>
            </select>
        </div>
        <div>
            <label>Estado</label>
            <select style="width:100%; padding:0.4rem; border-radius:8px; border:1px solid #cbd5e1;">
                <option>Todos</option>
                <option>Pendiente</option>
                <option>Revisada</option>
                <option>Bloqueada</option>
                <option>Descartada</option>
            </select>
        </div>
        <div>
            <label>Monto mínimo</label>
            <input type="number" placeholder="0" style="width:100%; padding:0.4rem; border-radius:8px; border:1px solid #cbd5e1;">
        </div>
        <div>
            <label>Monto máximo</label>
            <input type="number" placeholder="10000" style="width:100%; padding:0.4rem; border-radius:8px; border:1px solid #cbd5e1;">
        </div>
    </div>
    <button style="background:#3b82f6; color:white; border:none; border-radius:40px; padding:0.5rem 2rem; font-weight:600; margin-top:1rem;">Aplicar filtros</button>
</div>
""", unsafe_allow_html=True)

# Tabla de alertas
df_alertas = get_alertas_df()

st.markdown("""
<div class="card">
    <h3>📋 Alertas generadas</h3>
    <div class="table-wrapper">
""", unsafe_allow_html=True)

# Mostrar tabla con estilos de estado
st.dataframe(
    df_alertas,
    use_container_width=True,
    hide_index=True,
    column_config={
        "estado": st.column_config.TextColumn("Estado", help="Estado de revisión"),
        "riesgo": st.column_config.TextColumn("Riesgo"),
        "probabilidad": st.column_config.ProgressColumn("Probabilidad", format="%.0f%%", min_value=0, max_value=1),
    }
)

st.markdown("</div>", unsafe_allow_html=True)

# Botón Ver detalle (simulado, redirige a la página de detalle con parámetro)
if st.button("🔍 Ver detalle de alerta (ejemplo)", use_container_width=True):
    st.switch_page("pages/5_detalle_alerta.py")