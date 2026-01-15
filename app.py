import streamlit as st
import pandas as pd

# Configuração Padrão Ouro do SCO
st.set_page_config(page_title="IA-SENTINELA | EQI 2026", layout="wide")

st.title("🛡️ Monitoramento de Leads & ROI - EQI 2026")
st.markdown("---")

# Barra Lateral de Controle
st.sidebar.header("⚙️ Parâmetros do Projeto")
investimento = st.sidebar.number_input("Verba de Anúncios (R$)", value=2000.0)
custo_lead = st.sidebar.number_input("Custo por Lead (R$)", value=20.0)
taxa_conversao = st.sidebar.slider("Taxa de Conversão (%)", 1, 10, 4)

# Cálculos Táticos
leads_totais = investimento / custo_lead
conversao_real = leads_totais * (taxa_conversao / 100)

# Exibição das Métricas
c1, c2, c3 = st.columns(3)
c1.metric("Total de Leads", f"{int(leads_totais)}")
c2.metric("Conversão Estimada", f"{int(conversao_real)}")
c3.metric("Status Operacional", "LIBERADO", delta="100%")

st.divider()

# Gráfico de Projeção para evitar o Vácuo
st.subheader("📊 Evolução da Captação (Projeção Mensal)")
dados_grafico = pd.DataFrame({
    'Semana': ['S1', 'S2', 'S3', 'S4'],
    'Leads': [leads_totais*0.1, leads_totais*0.3, leads_totais*0.6, leads_totais]
})
st.line_chart(dados_grafico.set_index('Semana'))

st.info("Sistema IA-SENTINELA: Monitorando o ROI para evitar vácuo de atendimento.")
