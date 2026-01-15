import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA 2026
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# 2. BANDA DE BLINDAGEM E ESTÉTICA PDF (CSS CORRIGIDO)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    
    /* Estilo das Métricas */
    .stMetric { 
        background-color: #161b22; 
        border-radius: 10px; 
        padding: 15px; 
        border: 1px solid #30363d; 
    }

    /* MOLDURA DO RELATÓRIO PDF */
    .pdf-box {
        background-color: white;
        color: #1a1a1a;
        padding: 30px;
        border-radius: 5px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        margin-bottom: 20px;
        font-family: 'Arial', sans-serif;
        border-top: 15px solid #1e3a8a;
    }
    .pdf-header { border-bottom: 2px solid #eee; margin-bottom: 20px; padding-bottom: 10px; }
    .pdf-title { color: #1e3a8a; font-size: 22px; font-weight: bold; }
    
    /* Forçar visibilidade da tabela no fundo branco */
    .stTable { background-color: white !important; color: black !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABEÇALHO FIXO
st.title("🛡️ SISTEMA IA-SENTINELA")
st.subheader("Gestor Responsável: Sidney Almeida | EQI 2026")

# 4. NAVEGAÇÃO POR ABAS
aba_filtro, aba_dash, aba_relatorio = st.tabs(["⚙️ FILTROS", "📊 DASHBOARD", "📄 RELATÓRIO PDF"])

# Inicialização de valores para evitar erro de tipo
if 'investimento' not in st.session_state:
    st.session_state.investimento = 5000.0
if 'custo_lead' not in st.session_state:
    st.session_state.custo_lead = 25.0

with aba_filtro:
    st.info("Configure os valores para atualizar a auditoria.")
    st.
    
