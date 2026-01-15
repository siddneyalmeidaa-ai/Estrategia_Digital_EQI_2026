import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA 2026
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# BANDA DE BLINDAGEM ATUALIZADA (Oculta apenas o desnecessário, mantém os campos)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    /* Ajuste para garantir que os campos de input apareçam */
    .stNumberInput, .stSelectbox { border-bottom: 1px solid #30363d; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# CABEÇALHO FIXO
st.title("🛡️ SISTEMA IA-SENTINELA")
st.subheader(f"Gestor Responsável: Sidney Almeida | EQI 2026")

# BARRA LATERAL (CONTROLE DE INVESTIMENTO)
with st.sidebar:
    st.header("🎯 CONFIGURAÇÃO DE BASE")
    doutor_nome = st.selectbox("Assessor/Unidade", ["EQI Matriz", "EQI Filial SP", "EQI Filial SC"])
    investimento = st.number_input("Valor de Investimento (R$)", value=5000.0, step=100.0)
    custo_lead = st.number_input("Custo Médio por Lead (R$)", value=25.0, step=1.0)
    leads_totais = investimento / custo_lead

# CRIAÇÃO DAS ABAS (NAVEGAÇÃO DO SISTEMA)
aba1, aba2 = st.tabs(["📊 DASHBOARD DE PROJEÇÃO", "📄 EXPORTAR RELATÓRIOS"])

with aba1:
    # MÉTRICAS SINCRONIZADAS COM % NO TÍTULO
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("TOTAL DE LEADS", f"{int(leads_totais)}")
    with c2: st.metric("LIBERADO (100.0%)", "OPERACIONAL", delta="Sincronizado")
    with c3: st.metric("PENDENTE (0.0%)", "AÇÃO IMEDIATA", delta="Aguardando", delta_color="inverse")
    
    # GRÁFICO DE PROJEÇÃO DE NOVOS CLIENTES
    st.divider()
    st.subheader("📈 Projeção Automatizada de Rodadas")
    df = pd.DataFrame({
        'Rodada': ['R1', 'R2', 'R3', 'R4'],
        'Projeção': [leads_totais*0.2, leads_totais*0.5, leads_totais*0.8, leads_totais],
        'Status': ['entra', 'entra', 'pula', 'não entra']
    })
    st.line_chart(df.set_index('Rodada')['Projeção'])

with aba2:
    st.subheader("📝 Tabela da Favelinha (Dados para Auditoria)")
    st.table(df) # Entrega visual sem blocos de código
    
    st.divider()
    # GERADOR DE RELATÓRIO BLINDADO
    st.subheader("📥 Download do Relatório Padrão Ouro")
    csv = df.to_csv(index=False).encode('utf-8-sig') # Sem erro de acento no celular
    
    st.download_button(
        label="📥 BAIXAR RELATÓRIO DE NOVOS CLIENTES",
        data=csv,
        file_name=f'Relatorio_Auditoria_{datetime.now().strftime("%d_%m_%Y")}.csv',
        mime='text/csv'
    )
    st.success("Relatório configurado para abertura direta no Excel Mobile.")
    
