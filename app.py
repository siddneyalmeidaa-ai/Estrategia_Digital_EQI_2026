import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA 2026
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# BANDA DE BLINDAGEM SIDNEY ALMEIDA (Oculta buscas, menus e ferramentas)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            div.stActionButton {display: none;}
            button.st-emotion-cache-18ni7ap {visibility: hidden;}
            .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# CABEÇALHO EXCLUSIVO
st.title("🛡️ SISTEMA IA-SENTINELA")
st.subheader(f"Gestor Responsável: Sidney Almeida | EQI 2026")
st.divider()

# BARRA LATERAL - GESTÃO SINCRONIZADA
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
st.sidebar.header("🎯 Gestão de Rodadas")
doutor_nome = st.sidebar.selectbox("Assessor/Unidade", ["EQI Matriz", "EQI Filial SP", "EQI Filial SC"])
investimento = st.sidebar.number_input("Investimento (R$)", value=5000.0)
custo_lead = st.sidebar.number_input("Custo por Lead (R$)", value=25.0)

# LÓGICA DE CÁLCULO SINCRONIZADA
leads_totais = investimento / custo_lead
p_liberado = 100.0  
p_pendente = 0.0    

# MÉTRICAS COM PERCENTUAIS NOS TÍTULOS
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("TOTAL DE LEADS", f"{int(leads_totais)}")
with c2:
    st.metric(f"LIBERADO ({p_liberado}%)", "OPERACIONAL")
with c3:
    st.metric(f"PENDENTE ({p_pendente}%)", "AÇÃO IMEDIATA")

# TABELA DA FAVELINHA E PROJEÇÃO
st.subheader("📊 Evolução da Projeção de Rodadas")

# Nomenclatura Padrão Ouro: entra, pula, não entra
dados_rodada = pd.DataFrame({
    'Rodada': ['R1', 'R2', 'R3', 'R4'],
    'Projeção': [leads_totais*0.2, leads_totais*0.5, leads_totais*0.8, leads_totais],
    'Status': ['entra', 'entra', 'pula', 'não entra'] 
})

st.line_chart(dados_rodada.set_index('Rodada')['Projeção'])

# EXIBIÇÃO DA TABELA DA FAVELINHA
st.markdown("### 📝 Tabela da Favelinha (Auditoria)")
st.table(dados_rodada)

# AÇÃO IMEDIATA - FOCO NO VÁCUO
st.warning(f"Ação Imediata: {doutor_nome} deve focar na eliminação do vácuo rastreado pela IA-SENTINELA.")

# BOTÃO DE DOWNLOAD BLINDADO
csv = dados_rodada.to_csv(index=False).encode('utf-8-sig')
st.download_button(
    label="📥 Baixar Relatório de Auditoria",
    data=csv,
    file_name=f'Auditoria_EQI_{datetime.now().strftime("%d-%m-%Y")}.csv',
    mime='text/csv',
)
