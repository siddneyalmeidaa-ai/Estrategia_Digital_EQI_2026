import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÃO MASTER
st.set_page_config(page_title="IA-SENTINELA | EQI PRO", layout="wide")

# 2. ESTILO VISUAL (CORREÇÃO PARA NÃO TRAVAR NO CELULAR)
st.markdown("""
<style>
    [data-testid="stHeader"] {display: none;}
    .pdf-frame {
        background-color: white !important;
        color: #1a1a1a !important;
        padding: 20px;
        border-radius: 8px;
        border-top: 10px solid #1e3a8a;
    }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO
st.title("🛡️ SISTEMA IA-SENTINELA")
st.write(f"**Gestor Responsável:** Sidney Almeida | EQI 2026")

# --- 🧠 BASE DE DADOS (CONFORME OS LÍDERES QUE MANDAMOS) ---
dados_lideres = {
    "LIDERANÇA ALPHA": {"valor": 16000.0, "custo_lead": 25.0, "risco": 32},
    "LIDERANÇA BRAVO": {"valor": 22500.0, "custo_lead": 30.0, "risco": 45},
    "LIDERANÇA CHARLIE": {"valor": 45000.0, "custo_lead": 22.0, "risco": 18}
}

lider_sel = st.selectbox("Selecione o Líder para Auditoria:", list(dados_lideres.keys()))
info = dados_lideres[lider_sel]

# --- 📈 CÁLCULOS DINÂMICOS DA ESTRATÉGIA ---
v_total = info["valor"]
leads_totais = v_total / info["custo_lead"]
p_risco = info["risco"]
p_ok = 100 - p_risco

# 4. A COLUNA DE STATUS DETALHADA (EXPLICAÇÃO DA METODOLOGIA)
fases = ["1. Início de Captação", "2. Escala Operacional", "3. Expansão Sentinela", "4. Consolidação"]
invest_fase = [v_total * 0.2, v_total * 0.5, v_total * 0.8, v_total]
leads_fase = [int(leads_totais * 0.2), int(leads_totais * 0.5), int(leads_totais * 0.8), int(leads_totais)]

# Aqui é onde o Status vira a explicação que o senhor pediu:
status_explicativo = [
    "✅ ENTRA: Captação saudável dentro do custo planejado.",
    "✅ ENTRA: Escala validada. Fluxo de leads operacional.",
    "⚠️ VÁCUO: Risco detectado! Custo alto na zona de morte.",
    "🚫 NÃO ENTRA: Bloqueio preventivo. Otimizar investimento."
]

df_favelinha = pd.DataFrame({
    "Fase Estratégica": fases,
    "Investimento (R$)": [f"R$ {x:,.2f}" for x in invest_fase],
    "Leads Esperados": leads_fase,
    "Status IA-SENTINELA": status_explicativo
})

aba1, aba2, aba3 = st.tabs(["📊 DASHBOARD", "📈 GRÁFICOS", "📄 RELATÓRIO"])

with aba1:
    st.markdown(f"### Análise Digital: {lider_sel}")
    c1, c2 = st.columns(2)
    c1.metric(f"LIBERADO ({p_ok}%)", f"R$ {v_total*(p_ok/100):,.2f}")
    c2.metric(f"PENDENTE ({p_risco}%)", f"R$ {v_total*(p_risco/100):,.2f}", delta=f"-{p_risco}%")
    
    st.divider()
    st.write("### 📝 Tabela da Favelinha (Explicação de Status)")
    st.table(df_favelinha)

with aba3:
    # RELATÓRIO FORMATADO COM A DESCRIÇÃO DOS CAMPOS
    st.markdown(f"""
    <div class="pdf-frame">
        <h2 style="color: #1e3a8a;">DOSSIÊ DE AUDITORIA EXECUTIVA</h2>
        <p><b>Liderança:</b> {lider_sel} | <b>Data:</b> {datetime.now().strftime('%d/%m/%Y')}</p>
        <hr>
        <p style="color: black;"><b>DETALHAMENTO DOS STATUS:</b></p>
        <p style="color: black; font-size: 13px;">
            - <b>ENTRA:</b> O custo do lead permite a continuidade do aporte.<br>
            - <b>VÁCUO:</b> Alerta de ineficiência técnica (Zona de Morte).<br>
            - <b>NÃO ENTRA:</b> Interrupção para proteção do capital do assessor.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.download_button("📥 BAIXAR RELATÓRIO", df_favelinha.to_csv(index=False).encode('utf-8-sig'), "Auditoria.csv")
    
