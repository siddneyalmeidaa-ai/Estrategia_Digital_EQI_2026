import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# ESTILO VISUAL (CSS) - BLINDADO PARA EVITAR ERROS DE SINTAXE
st.markdown("""
<style>
    [data-testid="stHeader"] {display: none;}
    .report-card {
        background-color: white;
        color: #1a1a1a;
        padding: 25px;
        border-radius: 8px;
        border-top: 10px solid #1e3a8a;
        font-family: sans-serif;
        margin-bottom: 20px;
    }
    .metric-box {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
    }
</style>
""", unsafe_allow_html=True)

# CABEÇALHO PRINCIPAL
st.title("🛡️ SISTEMA IA-SENTINELA")
st.write(f"**Gestor Responsável:** Sidney Almeida | EQI 2026")

# ABAS DIDÁTICAS
tab1, tab2, tab3 = st.tabs(["⚙️ CONFIGURAÇÃO", "📊 MONITORAMENTO", "📄 RELATÓRIO FINAL"])

# INICIALIZAÇÃO DE DADOS (EVITA ERRO DE MIXED TYPES)
if 'invest' not in st.session_state:
    st.session_state.invest = 5000.0
if 'c_lead' not in st.session_state:
    st.session_state.c_lead = 25.0

with tab1:
    st.subheader("🎯 Ajuste de Parâmetros")
    # Forçamos o uso de float para evitar o erro MixedNumericTypes
    st.session_state.invest = float(st.number_input("Investimento Total (R$)", value=float(st.session_state.invest), step=500.0))
    st.session_state.c_lead = float(st.number_input("Custo por Lead (R$)", value=float(st.session_state.c_lead), step=1.0))
    
    total_leads = st.session_state.invest / st.session_state.c_lead

# DEFINIÇÃO DAS FASES (DIDÁTICA SOLICITADA)
# Status Padrão: entra, vácuo, não entra
dados_fases = {
    "Fase Estratégica": ["1. Início de Captação", "2. Escala Operacional", "3. Expansão de Carteira", "4. Consolidação"],
    "Investimento (R$)": [st.session_state.invest * 0.2, st.session_state.invest * 0.3, st.session_state.invest * 0.4, st.session_state.invest],
    "Leads Esperados": [int(total_leads * 0.2), int(total_leads * 0.5), int(total_leads * 0.8), int(total_leads)],
    "Status": ["entra", "entra", "vácuo", "não entra"]
}
df = pd.DataFrame(dados_fases)

with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("TOTAL DE LEADS", f"{int(total_leads)}")
    with col2:
        st.metric("STATUS", "OPERACIONAL", delta="100%")
    with col3:
        st.metric("PENDÊNCIA", "NENHUMA", delta="0%")
    
    st.divider()
    st.subheader("📈 Evolução por Etapa")
    st.line_chart(df.set_index("Fase Estratégica")["Leads Esperados"])

with tab3:
    # BLOCO DE RELATÓRIO ESTILO PDF
    st.markdown(f"""
    <div class="report-card">
        <h2 style="color: #1e3a8a; margin-top: 0;">RELATÓRIO DE AUDITORIA EXECUTIVA</h2>
        <p><b>Data:</b> {datetime.now().strftime('%d/%m/%Y')} | <b>Ref:</b> EQI-2026</p>
        <hr>
        <p>Projeção detalhada por fases para o aporte de <b>R$ {st.session_state.invest:,.2f}</b>.</p>
    </div>
    """, unsafe_allow_html=True)

    # TABELA FORMATADA (Abaixo do cabeçalho do relatório)
    # Formatando valores para ficarem bonitos no relatório
    df_visual = df.copy()
    df_visual["Investimento (R$)"] = df_visual["Investimento (R$)"].map("R$ {:,.2f}".format)
    
    st.table(df_visual)

    st.info("💡 **Legenda de Auditoria:** 'vácuo' indica zona de monitoramento técnico da IA-SENTINELA.")
    
    # BOTÃO DE DOWNLOAD
    csv = df_visual.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="📥 BAIXAR RELATÓRIO PARA EXCEL",
        data=csv,
        file_name=f"Auditoria_EQI_{datetime.now().strftime('%d_%m_%Y')}.csv",
        mime="text/csv"
    )
    
