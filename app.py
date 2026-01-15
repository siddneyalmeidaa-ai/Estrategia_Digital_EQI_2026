import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA 2026
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# BANDA DE BLINDAGEM E ESTÉTICA PREMIUM (Efeito PDF)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    
    .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    
    .pdf-container {
        background-color: white;
        color: #1a1a1a;
        padding: 30px;
        border-radius: 5px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        font-family: 'Arial', sans-serif;
        border-left: 10px solid #1e3a8a;
    }
    .pdf-header { border-bottom: 2px solid #1e3a8a; padding-bottom: 10px; margin-bottom: 20px; }
    .pdf-title { color: #1e3a8a; font-size: 22px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# CABEÇALHO DO SISTEMA
st.title("🛡️ SISTEMA IA-SENTINELA")
st.subheader("Gestor Responsável: Sidney Almeida | EQI 2026")

# ABAS DO SISTEMA
aba_filtro, aba_dash, aba_relatorio = st.tabs([
    "⚙️ FILTROS", 
    "📊 DASHBOARD", 
    "📄 PRÉVIA RELATÓRIO"
])

# Inicialização de variáveis
if 'investimento' not in st.session_state:
    st.session_state.investimento = 5
    
