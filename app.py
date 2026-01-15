import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÃO DE ALTO NÍVEL
st.set_page_config(page_title="IA-SENTINELA | EQI 2026", layout="wide")

# 2. ESTILO PARA NÃO CORTAR NADA NO CELULAR
st.markdown("""
<style>
    [data-testid="stHeader"] {display: none;}
    .card-relatorio {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 8px solid #1e3a8a;
        margin-bottom: 15px;
        color: #1a1a1a;
    }
    .valor-destaque {
        color: #1e3a8a;
        font-weight: bold;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO
st.title("🛡️ SISTEMA IA-SENTINELA")
st.write(f"**Gestor:** Sidney Almeida | EQI 2026")

tab1, tab2, tab3 = st.tabs(["⚙️ CONFIGURAÇÃO", "📊 MONITORAMENTO", "📄 RELATÓRIO EXECUTIVO"])

# 4. LÓGICA DE DADOS (BLINDADA)
if 'invest' not in st.session_state: st.session_state.invest = 5000.0
if 'c_lead' not in st.session_state: st.session_state.c_lead = 25.0

with tab1:
    st.session_state.invest = float(st.number_input("Definir Investimento Total (R$)", value=float(st.session_state.invest), step=500.0))
    st.session_state.c_lead = float(st.number_input("Custo por Lead (R$)", value=float(st.session_state.c_lead), step=1.0))
    total_leads = st.session_state.invest / st.session_state.c_lead

# PROJEÇÕES DIDÁTICAS
fases = ["Fase 1: Setup", "Fase 2: Escala", "Fase 3: Expansão", "Fase 4: Consolidação"]
invests = [st.session_state.invest * 0.2, st.session_state.invest * 0.5, st.session_state.invest * 0.8, st.session_state.invest]
leads = [int(total_leads * 0.2), int(total_leads * 0.5), int(total_leads * 0.8), int(total_leads)]
status = ["entra", "entra", "vácuo", "não entra"]

with tab2:
    c1, c2, c3 = st.columns(3)
    c1.metric("LEADS TOTAIS", f"{int(total_leads)}")
    c2.metric("LIBERADO", "100%", delta="OPERACIONAL")
    c3.metric("PENDENTE", "0%", delta="SINCORNIZADO", delta_color="normal")
    st.divider()
    df_chart = pd.DataFrame({"Fase": fases, "Leads": leads})
    st.line_chart(df_chart.set_index("Fase"))

with tab3:
    # CABEÇALHO DO RELATÓRIO
    st.markdown(f"""
    <div style="background-color: white; padding: 20px; border-radius: 10px; color: black; border: 1px solid #eee;">
        <h2 style="color: #1e3a8a;">RELATÓRIO DE AUDITORIA</h2>
        <p><b>Data:</b> {datetime.now().strftime('%d/%m/%Y')} | <b>Investimento Base:</b> R$ {st.session_state.invest:,.2f}</p>
    </div>
    <br>
    """, unsafe_allow_html=True)

    # NOVO FORMATO: CARTÕES ESTRATÉGICOS (Não corta e é fácil de ler)
    for i in range(len(fases)):
        st.markdown(f"""
        <div class="card-relatorio">
            <span style="font-size: 20px;"><b>{fases[i]}</b></span><br>
            Aporte sugerido: <span class="valor-destaque">R$ {invests[i]:,.2f}</span> | 
            Leads: <span class="valor-destaque">{leads[i]}</span><br>
            <b>Status:</b> {status[i].upper()}
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background-color: #e1e8f5; padding: 15px; border-radius: 5px; color: #1e3a8a; font-size: 13px;">
        ⚠️ <b>Nota IA-SENTINELA:</b> O status 'vácuo' indica zona de monitoramento técnico
    
