import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA 2026
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# BANDA DE BLINDAGEM REVISADA (Esconde menus, mas MANTÉM OS DADOS VISÍVEIS)
st.markdown("""
    <style>
    /* Oculta apenas elementos de edição e menus superiores */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    
    /* Garante que o conteúdo principal e métricas fiquem visíveis */
    .main .block-container {padding-top: 2rem;}
    .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; opacity: 1 !important; }
    
    /* ESTÉTICA PDF NO FRONT-END */
    .pdf-container {
        background-color: white;
        color: #1a1a1a;
        padding: 25px;
        border-radius: 4px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        margin-top: 10px;
        font-family: 'Arial', sans-serif;
        border-top: 10px solid #1e3a8a;
    }
    .pdf-title { color: #1e3a8a; font-size: 20px; font-weight: bold; border-bottom: 2px solid #eee; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# CABEÇALHO FIXO (Garante que seu nome sempre apareça)
st.title("🛡️ SISTEMA IA-SENTINELA")
st.subheader("Gestor Responsável: Sidney Almeida | EQI 2026")

# ABAS DE NAVEGAÇÃO
aba_filtro, aba_dash, aba_relatorio = st.tabs([
    "⚙️ FILTROS", 
    "📊 DASHBOARD", 
    "📄 PRÉVIA RELATÓRIO"
])

# Inicialização de valores
if 'investimento' not in st.session_state:
    st.session_state.investimento = 5000.0
if 'custo_lead' not in st.session_state:
    st.session_state.custo_lead = 25.0

with aba_filtro:
    st.info("Ajuste os valores abaixo para atualizar os dados de captação.")
    st.session_state.investimento = st.number_input("Valor de Investimento (R$)", value=st.session_state.investimento, step=500.0)
    st.session_state.custo_lead = st.number_input("Custo por Lead (R$)", value=st.session_state.custo_lead, step=1.0)
    leads_totais = st.session_state.investimento / st.session_state.custo_lead

# CÁLCULO DA PROJEÇÃO E TERMINOLOGIA (vácuo)
df_base = pd.DataFrame({
    'Rodada': ['R1', 'R2', 'R3', 'R4'],
    'Projeção': [leads_totais*0.2, leads_totais*0.5, leads_totais*0.8, leads_totais],
    'Status': ['entra', 'entra', 'vácuo', 'não entra'] 
})

# FORMATAÇÃO DO RELATÓRIO DIDÁTICO
df_final = df_base.copy()
df_final['Investimento'] = df_final['Projeção'] * st.session_state.custo_lead
df_final['Investimento'] = df_final['Investimento'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
df_final['Novos Clientes'] = df_final['Projeção'].apply(lambda x: int(x * 0.05))
df_final = df_final[['Rodada', 'Investimento', 'Novos Clientes', 'Status']]

with aba_dash:
    # Retorno das Métricas Visíveis
    col1, col2, col3 = st.columns(3)
    col1.metric("TOTAL DE LEADS", f"{int(leads_totais)}")
    col2.metric("LIBERADO (100%)", "OPERACIONAL")
    col3.metric("PENDENTE (0%)", "AÇÃO IMEDIATA")
    
    st.divider()
    st.subheader("📈 Gráfico de Projeção")
    st.line_chart(df_base.set_index('Rodada')['Projeção'])

with aba_relatorio:
    # Pré-visualização Estilo PDF
    st.markdown(f"""
    <div class="pdf-container">
        <div class="pdf-title">RELATÓRIO DE AUDITORIA EXECUTIVA</div>
        <p style="color: #444; font-size: 14px; margin-top: 10px;">
            <b>Emissor:</b> Sidney Almeida<br>
            <b>Data de Referência:</b> {datetime.now().strftime('%d/%m/%Y')}<br>
            <b>Aporte Identificado:</b> R$ {st.session_state.investimento:,.2f}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Exibição da Tabela Formatada
    st.table(df_final)
    
    st.divider()
    # Botão de Download Configurado
    csv = df_final.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="📥 BAIXAR RELATÓRIO COMPLETO",
        data=csv,
        file_name=f'Auditoria_Sidney_{datetime.now().strftime("%d_%m_%Y")}.csv',
        mime='text/csv'
    )
    
