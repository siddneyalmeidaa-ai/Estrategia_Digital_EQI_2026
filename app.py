import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# ESTILO VISUAL (CSS) - CORRIGIDO PARA NÃO CORTAR A TABELA
st.markdown("""
<style>
    [data-testid="stHeader"] {display: none;}
    .report-card {
        background-color: white;
        color: #1a1a1a;
        padding: 25px;
        border-radius: 8px 8px 0 0;
        border-top: 10px solid #1e3a8a;
        font-family: sans-serif;
    }
    /* Força o fundo branco a acompanhar o tamanho da tabela */
    div[data-testid="stTable"] { 
        background-color: white !important; 
        margin-top: -1px;
        padding: 0 25px;
    }
    .footer-card {
        background-color: white;
        color: #1a1a1a;
        padding: 10px 25px 25px 25px;
        border-radius: 0 0 8px 8px;
    }
</style>
""", unsafe_allow_html=True)

# CABEÇALHO DO SISTEMA
st.title("🛡️ SISTEMA IA-SENTINELA")
st.write(f"**Gestor Responsável:** Sidney Almeida | EQI 2026")

tab1, tab2, tab3 = st.tabs(["⚙️ CONFIGURAÇÃO", "📊 MONITORAMENTO", "📄 RELATÓRIO FINAL"])

# INICIALIZAÇÃO E FILTROS
if 'invest' not in st.session_state: st.session_state.invest = 5000.0
if 'c_lead' not in st.session_state: st.session_state.c_lead = 25.0

with tab1:
    st.session_state.invest = float(st.number_input("Investimento Total (R$)", value=float(st.session_state.invest), step=500.0))
    st.session_state.c_lead = float(st.number_input("Custo por Lead (R$)", value=float(st.session_state.c_lead), step=1.0))
    total_leads = st.session_state.invest / st.session_state.c_lead

# CÁLCULO DAS FASES (DIDÁTICA EQI)
dados_fases = {
    "Fase Estratégica": ["1. Início de Captação", "2. Escala Operacional", "3. Expansão de Carteira", "4. Consolidação"],
    "Investimento (R$)": [st.session_state.invest * 0.2, st.session_state.invest * 0.5, st.session_state.invest * 0.8, st.session_state.invest],
    "Leads Esperados": [int(total_leads * 0.2), int(total_leads * 0.5), int(total_leads * 0.8), int(total_leads)],
    "Status": ["entra", "entra", "vácuo", "não entra"]
}
df = pd.DataFrame(dados_fases)
df_visual = df.copy()
df_visual["Investimento (R$)"] = df_visual["Investimento (R$)"].map("R$ {:,.2f}".format)

with tab2:
    c1, c2, c3 = st.columns(3)
    c1.metric("TOTAL DE LEADS", f"{int(total_leads)}")
    c2.metric("LIBERADO (100.0%)", "OPERACIONAL")
    c3.metric("PENDENTE (0.0%)", "AÇÃO IMEDIATA")
    st.divider()
    st.line_chart(df.set_index("Fase Estratégica")["Leads Esperados"])

with tab3:
    # 1. TOPO DO RELATÓRIO
    st.markdown(f"""
    <div class="report-card">
        <h2 style="color: #1e3a8a; margin-top: 0;">RELATÓRIO DE AUDITORIA EXECUTIVA</h2>
        <p><b>Data:</b> {datetime.now().strftime('%d/%m/%Y')} | <b>Ref:</b> EQI-2026</p>
        <p>Projeção detalhada por fases para o aporte de <b>R$ {st.session_state.invest:,.2f}</b>.</p>
        <hr style="border: 0.5px solid #eee;">
    </div>
    """, unsafe_allow_html=True)

    # 2. TABELA (AQUI ELA NÃO SERÁ MAIS CORTADA)
    st.table(df_visual)

    # 3. RODAPÉ DO RELATÓRIO (LEGENDA)
    st.markdown("""
    <div class="footer-card">
        <hr style="border: 0.5px solid #eee;">
        <p style="font-size: 13px; border-left: 4px solid #1e3a8a; padding-left: 10px;">
            <b>Legenda de Auditoria:</b> O status 'vácuo' indica a zona de 1.00x monitorada pela IA-SENTINELA.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # BOTÃO DE DOWNLOAD
    csv = df_visual.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="📥 BAIXAR RELATÓRIO COMPLETO",
        data=csv,
        file_name=f"Auditoria_Sidney_{datetime.now().strftime('%d_%m_%Y')}.csv",
        mime="text/csv"
    )
    
