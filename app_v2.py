import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO PADRÃO OURO - INTERFACE IA-SENTINELA
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# ESTILO VISUAL BLINDADO
st.markdown("<style>.stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }</style>", unsafe_allow_html=True)

# CABEÇALHO PERSONALIZADO
st.title("🛡️ SISTEMA IA-SENTINELA")
st.subheader(f"Gestor Responsável: Sidney Almeida | EQI 2026")
st.divider()

# BARRA LATERAL - GESTÃO SINCRONIZADA
st.sidebar.header("🎯 Gestão de Rodadas")
doutor_nome = st.sidebar.selectbox("Selecione o Assessor/Unidade", ["EQI Matriz", "EQI Filial SP", "EQI Filial SC"])
investimento = st.sidebar.number_input("Investimento (R$)", value=5000.0)
custo_lead = st.sidebar.number_input("Custo por Lead (R$)", value=25.0)

# LÓGICA DE CÁLCULO SINCRONIZADA (Regras Padrão Ouro)
leads_totais = investimento / custo_lead
p_liberado = 100.0  # Substitui o texto pelo percentual real
p_pendente = 0.0    # Substitui o texto pelo percentual real

# MÉTRICAS COM TÍTULOS DINÂMICOS
c1, c2, c3 = st.columns(3)
with c1: st.metric("TOTAL DE LEADS", f"{int(leads_totais)}")
with c2: st.metric(f"LIBERADO ({p_liberado}%)", "OPERACIONAL", delta="Sincronizado")
with c3: st.metric(f"PENDENTE ({p_pendente}%)", "AÇÃO IMEDIATA", delta="Aguardando", delta_color="inverse")

# TABELA DA FAVELINHA E PROJEÇÃO (X determinado por rodada)
st.subheader("📊 Evolução da Projeção de Rodadas")
dados_rodada = pd.DataFrame({
    'Rodada': ['R1', 'R2', 'R3', 'R4'],
    'Projeção': [leads_totais*0.2, leads_totais*0.5, leads_totais*0.8, leads_totais],
    'Status': ['entra', 'entra', 'pula', 'não entra'] # Regra: entra/pula/não entra
})
st.line_chart(dados_rodada.set_index('Rodada')['Projeção'])

# EXIBIÇÃO DA TABELA DA FAVELINHA
st.markdown("### 📝 Tabela da Favelinha (Auditoria)")
st.table(dados_rodada)

# AÇÃO IMEDIATA (IA-SENTINELA rastreando o vácuo)
st.warning(f"Ação Imediata: {doutor_nome} deve focar na eliminação do vácuo.")

# BOTÃO DE DOWNLOAD (CONFIGURADO PARA CELULAR - SEM ERRO DE ACENTO)
csv = dados_rodada.to_csv(index=False).encode('utf-8-sig')
st.download_button(label="📥 Baixar Relatorio de Auditoria", data=csv, file_name=f'Relatorio_EQI.csv', mime='text/csv')
