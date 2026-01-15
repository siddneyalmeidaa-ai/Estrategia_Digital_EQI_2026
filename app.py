import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA 2026
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# BANDA DE BLINDAGEM (Oculta menus e cabeçalhos desnecessários)
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

# CRIAÇÃO DAS TRÊS ABAS (Filtros, Dashboard e Relatórios)
aba_filtro, aba_dash, aba_relatorio = st.tabs([
    "⚙️ FILTROS DE PROJEÇÃO", 
    "📊 DASHBOARD OPERACIONAL", 
    "📄 EXPORTAR RELATÓRIOS"
])

# Lógica de Dados (Inicialização)
if 'investimento' not in st.session_state:
    st.session_state.investimento = 5000.0
if 'custo_lead' not in st.session_state:
    st.session_state.custo_lead = 25.0

with aba_filtro:
    st.subheader("🎯 Configuração de Metas e Investimento")
    st.write("Ajuste os valores abaixo para atualizar automaticamente as projeções de novos clientes.")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.session_state.investimento = st.number_input(
            "Valor Total do Investimento (R$)", 
            value=st.session_state.investimento, 
            step=500.0
        )
    with col_f2:
        st.session_state.custo_lead = st.number_input(
            "Custo por Lead Estimado (R$)", 
            value=st.session_state.custo_lead, 
            step=1.0
        )
    
    leads_totais = st.session_state.investimento / st.session_state.custo_lead
    st.success(f"Configuração Salva: Projeção baseada em {int(leads_totais)} leads totais.")

# Cálculo para as outras abas
df_projecao = pd.DataFrame({
    'Rodada': ['R1', 'R2', 'R3', 'R4'],
    'Projeção': [leads_totais*0.2, leads_totais*0.5, leads_totais*0.8, leads_totais],
    'Status': ['entra', 'entra', 'pula', 'não entra']
})

with aba_dash:
    # MÉTRICAS SINCRONIZADAS
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("TOTAL DE LEADS", f"{int(leads_totais)}")
    with c2: st.metric("LIBERADO (100.0%)", "OPERACIONAL", delta="Sincronizado")
    with c3: st.metric("PENDENTE (0.0%)", "AÇÃO IMEDIATA", delta="Aguardando", delta_color="inverse")
    
    st.divider()
    st.subheader("📈 Gráfico de Evolução de Novos Clientes")
    st.line_chart(df_projecao.set_index('Rodada')['Projeção'])

with aba_relatorio:
    st.subheader("📝 Tabela da Favelinha (Auditoria)")
    st.table(df_projecao)
    
    st.divider()
    st.subheader("📥 Download do Relatório")
    csv = df_projecao.to_csv(index=False).encode('utf-8-sig')
    
    st.download_button(
        label="📥 BAIXAR RELATÓRIO COMPLETO (Excel/CSV)",
        data=csv,
        file_name=f'Relatorio_Auditoria_{datetime.now().strftime("%d_%m_%Y")}.csv',
        mime='text/csv'
    )
    
