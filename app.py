import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA 2026
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# BANDA DE BLINDAGEM SIDNEY ALMEIDA
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# CABEÇALHO FIXO
st.title("🛡️ SISTEMA IA-SENTINELA")
st.subheader(f"Gestor Responsável: Sidney Almeida | EQI 2026")

# ABAS DO SISTEMA
aba_filtro, aba_dash, aba_relatorio = st.tabs([
    "⚙️ FILTROS DE PROJEÇÃO", 
    "📊 DASHBOARD OPERACIONAL", 
    "📄 EXPORTAR RELATÓRIOS"
])

# Inicialização de variáveis
if 'investimento' not in st.session_state:
    st.session_state.investimento = 5000.0
if 'custo_lead' not in st.session_state:
    st.session_state.custo_lead = 25.0

with aba_filtro:
    st.subheader("🎯 Parâmetros da Operação")
    c_f1, c_f2 = st.columns(2)
    with c_f1:
        st.session_state.investimento = st.number_input("Investimento Total (R$)", value=st.session_state.investimento, step=500.0)
    with c_f2:
        st.session_state.custo_lead = st.number_input("Custo por Lead (R$)", value=st.session_state.custo_lead, step=1.0)
    
    leads_totais = st.session_state.investimento / st.session_state.custo_lead

# LÓGICA DE TERMINOLOGIA CORRETA (vácuo / entra / não entra)
# Regra: Termo 'vácuo' para a zona de morte rastreada pela IA-SENTINELA
df_base = pd.DataFrame({
    'Rodada': ['R1', 'R2', 'R3', 'R4'],
    '
    
