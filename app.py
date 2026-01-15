import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÃO MASTER
st.set_page_config(page_title="IA-SENTINELA | EQI PRO", layout="wide")

# 2. ESTILO VISUAL (CORREÇÃO DE SINTAXE PARA NÃO DAR ERRO NO CELULAR)
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

# --- 🧠 BASE DE DADOS SINCRONIZADA ---
dados_lideres = {
    "LIDERANÇA ALPHA": {"valor": 16000.0, "custo_lead": 25.0, "risco": 32},
    "LIDERANÇA BRAVO": {"valor": 22500.0, "custo_lead": 30.0, "risco": 45},
    "LIDERANÇA CHARLIE": {"valor": 45000.0, "custo_lead": 22.0, "risco": 18}
}

lider_sel = st.selectbox("Selecione o Líder para Auditoria:", list(dados_lideres.keys()))
info = dados_lideres[lider_sel]

# --- 📈 CÁLCULOS DINÂMICOS ---
v_total = info["valor"]
leads_totais = v_total / info["custo_lead"]
p_risco = info["risco"]
p_ok = 100 - p_risco

# 4. DEFINIÇÃO DAS FASES E STATUS EXPLICATIVOS
fases = ["1. Início de Captação", "2. Escala Operacional", "3. Expansão Sentinela", "4. Consolidação"]
invest_fase = [v_total * 0.2, v_total * 0.5, v_total * 0.8, v_total]
leads_fase = [int(leads_totais * 0.2), int(leads_totais * 0.5), int(leads_totais * 0.8), int(leads_totais)]

# STATUS DETALHADOS CONFORME SOLICITADO
status_explicativo = [
    "✅ ENTRA: Captação saudável (Custo OK).",
    "✅ ENTRA: Escala validada operacionalmente.",
    "⚠️ VÁCUO: Risco detectado (Zona de Morte).",
    "🚫 NÃO ENTRA: Bloqueio preventivo de capital."
]

df_favelinha = pd.DataFrame({
    "Fase Estratégica": fases,
    "Investimento (R$)": [f"R$ {x:,.2f}" for x in invest_fase],
    "Leads": leads_fase,
    "Status IA-SENTINELA": status_explicativo
})

aba1, aba2, aba3 = st.tabs(["📊 DASHBOARD", "📈 GRÁFICOS", "📄 RELATÓRIO"])

with aba1:
    c1, c2 = st.columns(2)
    # Títulos com os percentuais sincronizados
    c1.metric(f"LIBERADO ({p_ok}%)", f"R$ {v_total*(p_ok/100):,.2f}")
    c2.metric(f"PENDENTE ({p_risco}%)", f"R$ {v_total*(p_risco/100):,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.divider()
    st.write("### 📝 Tabela da Favelinha (Status Detalhado)")
    st.table(df_favelinha)

with aba2:
    st.write("### 📈 Evolução da Captação (Leads por Fase)")
    # RESTAURAÇÃO DO GRÁFICO QUE SUMIU
    chart_data = pd.DataFrame({"Leads": leads_fase}, index=fases)
    st.line_chart(chart_data)
    
    st.write("### 📊 Saúde do Investimento")
    df_pizza = pd.DataFrame({'Status': ['Liberado', 'Pendente'], 'Valor': [p_ok, p_risco]})
    st.vega_lite_chart(df_pizza, {
        'mark': {'type': 'arc', 'innerRadius': 50},
        'encoding': {
            'theta': {'field': 'Valor', 'type': 'quantitative'},
            'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#1e3a8a', '#ff4b4b']}}
        }
    })

with aba3:
    st.markdown(f"""
    <div class="pdf-frame">
        <h2 style="color: #1e3a8a; margin: 0;">RELATÓRIO DE AUDITORIA EXECUTIVA</h2>
        <p><b>Líder:</b> {lider_sel} | <b>Data:</b> {datetime.now().strftime('%d/%m/%Y')}</p>
        <hr>
        <p style="color: black;"><b>Métricas Consolidadas:</b></p>
        <table style="width:100%; color: black; font-size: 14px;">
            <tr><td>Total Leads Projetados:</td><td style="text-align:right;">{int(leads_totais)}</td></tr>
            <tr><td>Volume em Vácuo:</td><td style="text-align:right; color: red;">R$ {v_total*(p_risco/100):,.2f}</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.download_button("📥 BAIXAR RELATÓRIO", df_favelinha.to_csv(index=False).encode('utf-8-sig'), f"Auditoria_{lider_sel}.csv")

st.info(f"💡 **IA-SENTINELA:** O status 'vácuo' identifica a zona de morte monitorada.")
