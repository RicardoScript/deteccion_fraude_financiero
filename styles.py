import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* Reset y fuente */
        * {
            box-sizing: border-box;
        }
        body {
            font-family: 'Inter', 'Segoe UI', sans-serif;
            background-color: #f8fafc;
            margin: 0;
            padding: 0;
        }
        .main {
            padding: 1.5rem 2rem;
        }
        /* Encabezado */
        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid #e2e8f0;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }
        .header h1 {
            font-size: 1.8rem;
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
            white-space: nowrap;
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
            font-size: 2rem;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.2;
        }
        .metric-label {
            font-size: 0.85rem;
            color: #64748b;
            margin-bottom: 0.2rem;
        }
        .metric-change {
            font-size: 0.8rem;
            font-weight: 500;
            margin-top: 0.3rem;
        }
        .green { color: #16a34a; }
        .red { color: #dc2626; }
        .blue { color: #2563eb; }
        .yellow { color: #ca8a04; }
        /* Etiquetas de estado */
        .status-badge {
            display: inline-block;
            padding: 0.2rem 0.8rem;
            border-radius: 40px;
            font-size: 0.8rem;
            font-weight: 600;
        }
        .status-badge.pendiente { background: #fef9c3; color: #854d0e; }
        .status-badge.revisada { background: #dcfce7; color: #166534; }
        .status-badge.bloqueada { background: #fee2e2; color: #b91c1c; }
        .status-badge.descartada { background: #e5e7eb; color: #374151; }
        .status-badge.fraude { background: #fee2e2; color: #b91c1c; }
        .status-badge.normal { background: #dcfce7; color: #166534; }
        .risk-low { background: #dcfce7; color: #166534; }
        .risk-medium { background: #fef9c3; color: #854d0e; }
        .risk-high { background: #fee2e2; color: #b91c1c; }
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
        .stButton button:active {
            transform: translateY(0);
        }
        /* Inputs */
        .stTextInput, .stSelectbox, .stNumberInput, .stSlider {
            margin-bottom: 0.5rem;
        }
        label {
            font-weight: 500;
            color: #334155;
            font-size: 0.9rem;
        }
        /* Tablas */
        .dataframe {
            font-size: 0.9rem;
        }
        .dataframe th {
            background-color: #f1f5f9;
            font-weight: 600;
        }
        /* Divider */
        hr {
            margin: 2rem 0;
            border: 0;
            border-top: 1px solid #e2e8f0;
        }
        /* Sidebar */
        .css-1d391kg {
            background-color: #f1f5f9;
        }
        .css-1d391kg .css-1aumxhk {
            background-color: #f1f5f9;
        }
        /* Responsive */
        @media (max-width: 768px) {
            .main {
                padding: 1rem;
            }
            .header h1 {
                font-size: 1.4rem;
            }
            .card {
                padding: 1rem;
            }
            .metric-value {
                font-size: 1.6rem;
            }
        }
        /* Ocultar footer de Streamlit */
        footer {visibility: hidden;}
        /* Scroll horizontal para tablas */
        .table-wrapper {
            overflow-x: auto;
        }
        /* Grid de métricas */
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
        }
        .metrics-grid .metric-item {
            background: #f8fafc;
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
        }
        .metrics-grid .metric-item .value {
            font-size: 1.8rem;
            font-weight: 700;
            color: #0f172a;
        }
        .metrics-grid .metric-item .label {
            font-size: 0.8rem;
            color: #64748b;
        }
        /* Accesos rápidos */
        .quick-access {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 1rem;
        }
        .quick-access a {
            background: #3b82f6;
            color: white;
            padding: 0.5rem 1.5rem;
            border-radius: 40px;
            text-decoration: none;
            font-weight: 500;
            transition: background 0.2s;
            display: inline-block;
            font-size: 0.9rem;
        }
        .quick-access a:hover {
            background: #2563eb;
        }
        .quick-access a.secondary {
            background: #1e293b;
        }
        .quick-access a.secondary:hover {
            background: #0f172a;
        }
        .quick-access a.outline {
            background: transparent;
            color: #1e293b;
            border: 1px solid #cbd5e1;
        }
        .quick-access a.outline:hover {
            background: #f1f5f9;
        }
    </style>
    """, unsafe_allow_html=True)