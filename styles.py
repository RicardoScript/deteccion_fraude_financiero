import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* Reset y fuente */
        body {
            font-family: 'Inter', 'Segoe UI', sans-serif;
            background-color: #f8fafc;
        }
        .main {
            padding: 1.5rem 2rem;
        }
        /* Encabezado global */
        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid #e2e8f0;
            margin-bottom: 2rem;
        }
        .header h1 {
            font-size: 2rem;
            font-weight: 600;
            color: #0f172a;
            margin: 0;
            letter-spacing: -0.02em;
        }
        .header .badge {
            background: #3b82f6;
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
        }
        /* Tarjetas */
        .card {
            background: white;
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);
            margin-bottom: 1.5rem;
            border: 1px solid #f1f5f9;
            transition: all 0.2s;
        }
        .card:hover {
            box-shadow: 0 8px 12px -2px rgba(0,0,0,0.08);
        }
        .card h3 {
            font-weight: 500;
            color: #1e293b;
            margin-top: 0;
            margin-bottom: 1rem;
            font-size: 1.1rem;
            letter-spacing: -0.01em;
        }
        .metric-value {
            font-size: 2.2rem;
            font-weight: 700;
            color: #0f172a;
        }
        .metric-label {
            font-size: 0.9rem;
            color: #64748b;
        }
        .metric-change {
            font-size: 0.85rem;
            font-weight: 500;
        }
        .green {
            color: #16a34a;
        }
        .red {
            color: #dc2626;
        }
        .blue {
            color: #2563eb;
        }
        /* Etiquetas de fraude */
        .fraud-tag {
            display: inline-block;
            padding: 0.3rem 1.2rem;
            border-radius: 40px;
            font-weight: 600;
            font-size: 1rem;
            margin-top: 0.5rem;
        }
        .fraud-tag.true {
            background: #fee2e2;
            color: #b91c1c;
        }
        .fraud-tag.false {
            background: #dcfce7;
            color: #166534;
        }
        .fraud-tag.warning {
            background: #fef9c3;
            color: #854d0e;
        }
        /* Botones */
        .stButton button {
            background: #3b82f6;
            color: white;
            font-weight: 600;
            border: none;
            border-radius: 40px;
            padding: 0.6rem 2rem;
            transition: all 0.2s;
            width: 100%;
            box-shadow: 0 4px 6px -1px rgba(59,130,246,0.2);
        }
        .stButton button:hover {
            background: #2563eb;
            box-shadow: 0 6px 8px -1px rgba(59,130,246,0.3);
            transform: translateY(-1px);
        }
        /* Sidebar (si se usa) */
        .css-1d391kg {
            background-color: #f1f5f9;
        }
        /* Responsive */
        @media (max-width: 768px) {
            .main {
                padding: 1rem;
            }
            .header h1 {
                font-size: 1.5rem;
            }
            .card {
                padding: 1rem;
            }
            .metric-value {
                font-size: 1.8rem;
            }
        }
        /* Ocultar footer de Streamlit */
        footer {visibility: hidden;}
        /* Tablas */
        .dataframe {
            font-size: 0.9rem;
        }
        .dataframe th {
            background-color: #f1f5f9;
        }
        /* Dividers */
        hr {
            margin: 2rem 0;
            border: 0;
            border-top: 1px solid #e2e8f0;
        }
    </style>
    """, unsafe_allow_html=True)