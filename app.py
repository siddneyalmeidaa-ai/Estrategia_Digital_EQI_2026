import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA 2026
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# BANDA DE BLINDAGEM (Oculta cabeçalhos, buscas e menus)
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

# CRIAÇÃO DAS ABAS
aba1, aba2 = st.tabs(["📊 DASHBOARD OPERACIONAL", "📄 RELATÓRIOS & AUDITORIA"])

# BARRA LATERAL (CONFIGURAÇÃO)
with st.sidebar:
    st.header("🎯 Parâmetros")
    investimento = st.number_input("Investimento (R$)", value=5000.0)
    custo_lead = st.number_input("Custo por Lead (R$)", value=25.0)
    leads_totais = investimento / custo_lead

with aba1:
    # MÉTRICAS SINCRONIZADAS
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("TOTAL DE LEADS", f"{int(leads_totais)}")
    with c2: st.metric("LIBERADO (100.0%)", "OPERACIONAL")
    with c3: st.metric("PENDENTE (0.0%)", "AÇÃO IMEDIATA")
    
    # GRÁFICO DE PROJEÇÃO
    st.divider()
    st.subheader("Evolução da Projeção de Rodadas")
    df = pd.DataFrame({
        'Rodada': ['R1', 'R2', 'R3', 'R4'],
        'Projeção': [leads_totais*0.2, leads_totais*0.5, leads_totais*0.8, leads_totais],
        'Status': ['entra', 'entra', 'pula', 'não entra']
    })
    st.line_chart(df.set_index('Rodada')['Projeção'])

with aba2:
    st.subheader("📝 Tabela da Favelinha")
    st.table(df) # Exibe a tabela sem blocos de programação
    
    st.divider()
    # GERADOR DE RELATÓRIO (CORREÇÃO DE DOWNLOAD)
    st.subheader("📥 Gerar Relatório de Auditoria")
    csv = df.to_csv(index=False).encode('utf-8-sig') # UTF-8-SIG para evitar erro de acento no celular
    
    st.download_button(
        label="Clique aqui para Baixar Relatório (CSV)",
        data=csv,
        file_name=f'Relatorio_Sidney_Almeida_{datetime.now().strftime("%d_%m_%Y")}.csv',
        mime='text/csv'
    )
    st.info("O relatório acima gera a auditoria completa das rodadas para exportação.")
            
