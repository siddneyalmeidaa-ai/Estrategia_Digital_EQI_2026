import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA 2026
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# BANDA DE BLINDAGEM (Oculta menus e cabeçalhos)
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
    st.info(f"Base de cálculo: {int(leads_totais)} leads projetados.")

# PROCESSAMENTO DO RELATÓRIO DIDÁTICO
# Aqui criamos a lógica de Reais e Número de Clientes
df_base = pd.DataFrame({
    'Rodada': ['R1', 'R2', 'R3', 'R4'],
    'Projeção Bruta': [leads_totais*0.2, leads_totais*0.5, leads_totais*0.8, leads_totais],
    'Status': ['entra', 'entra', 'pula', 'não entra']
})

# Formatação para o Relatório Excel/CSV
df_relatorio = df_base.copy()
df_relatorio['Investimento Estimado'] = df_relatorio['Projeção Bruta'] * st.session_state.custo_lead
df_relatorio['Investimento Estimado'] = df_relatorio['Investimento Estimado'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
df_relatorio['Novos Clientes (Qtd)'] = df_relatorio['Projeção Bruta'].apply(lambda x: int(x * 0.05)) # Exemplo: 5% de conversão
df_relatorio = df_relatorio[['Rodada', 'Investimento Estimado', 'Novos Clientes (Qtd)', 'Status']]

with aba_dash:
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("TOTAL DE LEADS", f"{int(leads_totais)}")
    with c2: st.metric("LIBERADO (100.0%)", "OPERACIONAL")
    with c3: st.metric("PENDENTE (0.0%)", "AÇÃO IMEDIATA")
    
    st.divider()
    st.subheader("📈 Evolução Visual")
    st.line_chart(df_base.set_index('Rodada')['Projeção Bruta'])

with aba_relatorio:
    st.markdown("### 📝 Tabela da Favelinha (Formatada em Reais)")
    st.write("Abaixo, a projeção didática com valores em Reais e estimativa de fechamento:")
    st.table(df_relatorio)
    
    st.divider()
    st.subheader("📥 Exportação para Auditoria")
    csv = df_relatorio.to_csv(index=False).encode('utf-8-sig')
    
    st.download_button(
        label="📥 BAIXAR RELATÓRIO EM REAIS (CSV/EXCEL)",
        data=csv,
        file_name=f'Auditoria_Sidney_Almeida_{datetime.now().strftime("%d_%m_%Y")}.csv',
        mime='text/csv'
    )
    
