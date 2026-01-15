import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÃO MASTER
st.set_page_config(page_title="IA-SENTINELA | AUDITORIA EQI", layout="wide")

# 2. ESTILO VISUAL (CORREÇÃO TOTAL DE SINTAXE)
st.markdown("""
<style>
    [data-testid="stHeader"] {display: none;}
    .pdf-frame {
        background-color: white !important;
        color: #1a1a1a !important;
        padding: 25px;
        border-radius: 8px;
        border-top: 15px solid #1e3a8a;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO
st.title("🛡️ SISTEMA IA-SENTINELA PRO")
st.write(f"**Gestor Responsável:** Sidney Almeida | EQI 2026")

# --- 🧠 INTELIGÊNCIA DE DIAGNÓSTICO E DIRECIONAMENTO ---
dados_lideres = {
    "LIDERANÇA ALPHA": {
        "valor": 16000.0, "custo_lead": 25.0, "risco": 32,
        "motivo": "Fadiga de criativos e saturação de público nas redes sociais.",
        "direcionamento": "Trocar as artes dos anúncios e testar novos públicos de interesse."
    },
    "LIDERANÇA BRAVO": {
        "valor": 22500.0, "custo_lead": 30.0, "risco": 45,
        "motivo": "Demora no tempo de resposta (LTV) entre o lead chegar e ser atendido.",
        "direcionamento": "Ativar resposta automática no WhatsApp para reduzir o vácuo."
    },
    "LIDERANÇA CHARLIE": {
        "valor": 45000.0, "custo_lead": 22.0, "risco": 18,
        "motivo": "Baixa taxa de conversão na Landing Page (página de captura).",
        "direcionamento": "Simplificar o formulário da página para aumentar a entrada de leads."
    }
}

lider_sel = st.selectbox("Selecione o Líder para Auditoria:", list(dados_lideres.keys()))
info = dados_lideres[lider_sel]

# --- 📈 CÁLCULOS DINÂMICOS (CORREÇÃO DO NAMEERROR) ---
v_total = info["valor"]
p_risco = info["risco"]
p_ok = 100 - p_risco
v_liberado = v_total * (p_ok / 100) # Variável corrigida
v_pendente = v_total * (p_risco / 100)
leads_totais = v_total / info["custo_lead"]

# Fases da Metodologia EQI
fases = ["1. Início", "2. Escala", "3. Expansão", "4. Consolidação"]
invest_fase = [v_total * 0.2, v_total * 0.5, v_total * 0.8, v_total]
leads_fase = [int(leads_totais * 0.2), int(leads_totais * 0.5), int(leads_totais * 0.8), int(leads_totais)]

aba1, aba2, aba3 = st.tabs(["📊 DASHBOARD", "📈 GRÁFICOS", "📄 RELATÓRIO"])

with aba1:
    st.markdown(f"### Auditoria: {lider_sel}")
    c1, c2 = st.columns(2)
    c1.metric(f"LIBERADO ({p_ok}%)", f"R$ {v_liberado:,.2f}")
    c2.metric(f"PENDENTE ({p_risco}%)", f"R$ {v_pendente:,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.divider()
    st.write("### 📝 Tabela da Favelinha (Diagnóstico)")
    df_f = pd.DataFrame({
        "Fase": fases,
        "Investimento": [f"R$ {x:,.2f}" for x in invest_fase],
        "Leads": leads_fase,
        "Status Sentinela": ["entra", "entra", "vácuo", "não entra"]
    })
    st.table(df_f)

with aba2:
    st.write("### 📈 Evolução da Captação")
    st.line_chart(pd.DataFrame({"Leads": leads_fase}, index=fases)) # Gráfico Restaurado

with aba3:
    # --- RELATÓRIO COM MOTIVO E DIRECIONAMENTO ---
    st.markdown(f"""
    <div class="pdf-frame">
        <h2 style="color: #1e3a8a; margin: 0;">RELATÓRIO DE AUDITORIA EXECUTIVA</h2>
        <p><b>Líder:</b> {lider_sel} | <b>Data:</b> {datetime.now().strftime('%d/%m/%Y')}</p>
        <hr>
        <p style="color: black;"><b>🔍 MOTIVO DO PENDENTE:</b><br>{info['motivo']}</p>
        <p style="color: black;"><b>🚀 DIRECIONAMENTO (AÇÃO IMEDIATA):</b><br>{info['direcionamento']}</p>
        <hr>
        <table style="width:100%; color: black;">
            <tr><td>Total Leads Projetados:</td><td style="text-align:right;">{int(leads_totais)}</td></tr>
            <tr><td>Volume em Vácuo:</td><td style="text-align:right; color: red;">R$ {v_pendente:,.2f}</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.download_button("📥 BAIXAR RELATÓRIO", df_f.to_csv(index=False).encode('utf-8-sig'), f"{lider_sel}.csv")

st.info("💡 IA-SENTINELA: Auditoria de conformidade para assessores EQI.")
                
