import streamlit as st
from styles import apply_custom_styles
import pandas as pd
import io

st.set_page_config(page_title="Carga masiva", layout="wide")
apply_custom_styles()

st.markdown("""
<div class="header">
    <h1>📤 Carga masiva de transacciones</h1>
    <span class="badge">Archivo CSV</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>📄 Subir archivo CSV</h3>
    <p>El archivo debe contener las siguientes columnas obligatorias:</p>
    <ul>
        <li><code>step</code></li>
        <li><code>type</code></li>
        <li><code>amount</code></li>
        <li><code>nameOrig</code></li>
        <li><code>oldbalanceOrg</code></li>
        <li><code>newbalanceOrig</code></li>
        <li><code>nameDest</code></li>
        <li><code>oldbalanceDest</code></li>
        <li><code>newbalanceDest</code></li>
    </ul>
""", unsafe_allow_html=True)

# Subida de archivo
uploaded_file = st.file_uploader("Selecciona un archivo CSV", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Archivo cargado correctamente")

        # Vista previa
        st.markdown("### 👁️ Vista previa (primeras 5 filas)")
        st.dataframe(df.head(), use_container_width=True)

        # Validación de columnas
        columnas_obligatorias = ["step", "type", "amount", "nameOrig", "oldbalanceOrg", "newbalanceOrig", "nameDest", "oldbalanceDest", "newbalanceDest"]
        columnas_faltantes = [col for col in columnas_obligatorias if col not in df.columns]
        if columnas_faltantes:
            st.error(f"❌ Faltan columnas obligatorias: {', '.join(columnas_faltantes)}")
        else:
            st.success("✅ Todas las columnas obligatorias están presentes")

            # Botón procesar (simulado)
            if st.button("⚙️ Procesar archivo", use_container_width=True):
                # Simulación de procesamiento
                total = len(df)
                normales = int(total * 0.85)
                sospechosas = int(total * 0.10)
                errores = total - normales - sospechosas

                st.markdown("---")
                st.markdown("### 📊 Resultado del procesamiento")
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total procesadas", total)
                with col2:
                    st.metric("Normales", normales, delta="")
                with col3:
                    st.metric("Sospechosas", sospechosas, delta="")
                with col4:
                    st.metric("Errores", errores, delta="")

                # Descarga de resultados
                resultado_df = df.copy()
                resultado_df["prediccion"] = ["normal"] * normales + ["sospechoso"] * sospechosas + ["error"] * errores
                # Ajustar longitud (solo demo)
                if len(resultado_df) > total:
                    resultado_df = resultado_df.head(total)
                # Añadir columna de resultado
                resultado_df["prediccion"] = ["normal"] * normales + ["sospechoso"] * sospechosas + ["error"] * errores
                resultado_df = resultado_df.head(total)  # truncar si es necesario

                csv = resultado_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Descargar resultados procesados (CSV)",
                    data=csv,
                    file_name="resultados_procesados.csv",
                    mime="text/csv",
                    use_container_width=True
                )
    except Exception as e:
        st.error(f"❌ Error al leer el archivo: {e}")
else:
    st.info("👆 Selecciona un archivo CSV para comenzar")

st.markdown("</div>", unsafe_allow_html=True)