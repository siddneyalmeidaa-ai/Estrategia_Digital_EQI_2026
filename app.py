import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÃO DE SEGURANÇA
st.set_page_config(page_title="IA-SENTINELA | EQI", layout="wide")

# 2. ESTILO VISUAL (CSS) - SIMPLIFICADO PARA MOBILE
st.markdown("""
<style>
    [data-testid="stHeader"] {display: none;}
    .bloco-branco {
        background-color: white;
        color: black;
        padding: 20px;
        border-radius: 10px;
        border-top: 8px solid #1e3a8a;
        margin-bottom: 10px;
    }
    .tabela-container {
        background-color: white !important;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO FIXO
st.title("🛡️ SISTEMA IA-SENTINELA")
st.write(f"**Gestor Responsável:** Sidney Almeida | EQI 2026")

aba1, aba2, aba3 = st.tabs(["⚙️ AJUSTES", "📊 DASHBOARD", "📄 RELATÓRIO"])

# 4. ENTRADA DE DADOS (PROTEÇÃO CONTRA ERROS NUMÉRICOS)
if 'v_invest' not in st.session_state: st.session_state.v_invest = 5000.0
if 'v_custo' not in st.session_state: st.session_state.v_custo = 25.0

with aba1:
    st.session_state.v_invest = float(st.number_input("Investimento Total (R$)", value=float(st.session_state.v_invest), step=500.0))
    st.session_state.v_custo = float(st.number_input("Custo por Lead (R$)", value=float(st.session_state.v_custo), step=1.0))
    leads_totais = st.session_state.v_invest / st.session_state.v_custo

# 5. CÁLCULO DAS PROJEÇÕES (DIDÁTICA SOLICITADA)
# Status: entra, vácuo, não entra
fases = ["1. Início de Captação", "2. Escala Operacional", "3. Expansão Sentinela", "4. Consolidação"]
valores = [st.session_state.v_invest * 0.2, st.session_state.v_invest * 0.5, st.session_state.v_invest * 0.8, st.session_state.v_invest]
leads_fase = [int(leads_totais * 0.2), int(leads_totais * 0.5), int(leads_totais * 0.8), int(leads_totais)]
status_fase = ["entra", "entra", "vácuo", "não entra"]

df_favelinha = pd.DataFrame({
    "Fase Estratégica": fases,
    "Investimento (R$)": [f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") for x in valores],
    "Leads": leads_fase,
    "Status": status_fase
})

with aba2:
    c1, c2, c3 = st.columns(3)
    c1.metric("TOTAL DE LEADS", f"{int(leads_totais)}")
    c2.metric("LIBERADO (100%)", "OPERACIONAL")
    c3.metric("PENDENTE (0%)", "AÇÃO IMEDIATA")
    st.divider()
    st.line_chart(pd.DataFrame({"Leads": leads_fase}, index=fases))

with aba3:
    # CABEÇALHO DO RELATÓRIO (BLOCO 1)
    st.markdown(f"""
    <div class="bloco-branco">
        <h2 style="color: #1e3a8a; margin: 0;">RELATÓRIO DE AUDITORIA</h2>
        <p style="margin: 5px 0;"><b>Emissor:</b> Sidney Almeida | <b>Data:</b> {datetime.now().strftime('%d/%m/%Y')}</p>
        <p style="margin: 5px 0;"><b>Aporte Identificado:</b> R$ {st.session_state.v_invest:,.2f}</p>
    </div>
    """, unsafe_allow_html=True)

    # TABELA DA FAVELINHA (BLOCO 2 - FORA DO HTML PARA NÃO CORTAR)
    st.write("### 📝 Tabela da Favelinha (Projeção)")
    st.table(df_favelinha)

    # LEGENDA E BOTÃO (BLOCO 3)
    st.info(f"💡 **IA-SENTINELA:** O status 'vácuo' identifica a zona de morte monitorada.")
    
    csv = df_favelinha.to_csv(index=False).encode('utf-8-sig')
    st.download_button("📥 BAIXAR RELATÓRIO COMPLETO", csv, "Auditoria_Sidney.csv", "text/csv")
    
