import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÃO MASTER - PADRÃO OURO EQI 2026
st.set_page_config(page_title="IA-SENTINELA | EQI PRO", layout="wide")

# 2. ESTILO VISUAL (CORREÇÃO DE SINTAXE)
st.markdown("""
<style>
    [data-testid="stHeader"] {display: none;}
    .pdf-frame {
        background-color: white !important;
        color: #1a1a1a !important;
        padding: 25px;
        border-radius: 8px;
        border-top: 12px solid #1e3a8a;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO
st.title("🛡️ SISTEMA IA-SENTINELA")
st.write(f"**Gestor Responsável:** Sidney Almeida | EQI 2026")

# --- 🧠 BASE DE DADOS SINCRONIZADA (METODOLOGIA EQI) ---
dados_lideres = {
    "LIDERANÇA ALPHA": {"valor": 16000.0, "custo_lead": 25.0, "risco": 32, "status": "entra"},
    "LIDERANÇA BRAVO": {"valor": 22500.0, "custo_lead": 30.0, "risco": 45, "status": "vácuo"},
    "LIDERANÇA CHARLIE": {"valor": 45000.0, "custo_lead": 22.0, "risco": 18, "status": "não entra"}
}

lider_sel = st.selectbox("Selecione o Líder para Auditoria:", list(dados_lideres.keys()))
info = dados_lideres[lider_sel]

# --- 📈 CÁLCULOS DINÂMICOS (RESTAURAÇÃO DOS GRÁFICOS) ---
v_total = info["valor"]
leads_totais = v_total / info["custo_lead"]
p_risco = info["risco"]
p_ok = 100 - p_risco
v_liberado = v_total * (p_ok / 100)
v_pendente = v_total * (p_risco / 100)

# Projeção de Captação (Tabela da Favelinha)
fases = ["1. Início de Captação", "2. Escala Operacional", "3. Expansão Sentinela", "4. Consolidação"]
invest_fase = [v_total * 0.2, v_total * 0.5, v_total * 0.8, v_total]
leads_fase = [int(leads_totais * 0.2), int(leads_totais * 0.5), int(leads_totais * 0.8), int(leads_totais)]
status_fase = ["entra", "entra", "vácuo", "não entra"]

aba1, aba2, aba3 = st.tabs(["📊 DASHBOARD", "📈 GRÁFICOS", "📄 RELATÓRIO"])

with aba1:
    st.markdown(f"### Análise: {lider_sel}")
    c1, c2 = st.columns(2)
    # Títulos com percentuais sincronizados
    c1.metric(f"LIBERADO ({p_ok}%)", f"R$ {v_liberado:,.2f}")
    c2.metric(f"PENDENTE ({p_risco}%)", f"R$ {v_pendente:,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.divider()
    st.write("### 📝 Tabela da Favelinha (Projeção)")
    df_favelinha = pd.DataFrame({
        "Fase Estratégica": fases,
        "Investimento (R$)": [f"R$ {x:,.2f}" for x in invest_fase],
        "Leads Esperados": leads_fase,
        "Status": status_fase
    })
    st.table(df_favelinha)

with aba2:
    st.write("### 📈 Evolução da Captação")
    # Gráfico de Linha para Leads
    chart_data = pd.DataFrame({"Leads": leads_fase}, index=fases)
    st.line_chart(chart_data)
    
    st.write("### 📊 Distribuição de Risco")
    # Gráfico de Pizza/Donut para Risco
    df_pizza = pd.DataFrame({'Status': ['Liberado', 'Pendente'], 'Valor': [p_ok, p_risco]})
    st.vega_lite_chart(df_pizza, {
        'mark': {'type': 'arc', 'innerRadius': 50},
        'encoding': {
            'theta': {'field': 'Valor', 'type': 'quantitative'},
            'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#00d4ff', '#ff4b4b']}}
        }
    })

with aba3:
    # --- RELATÓRIO PDF (CORREÇÃO DO ERRO DE ASPAS) ---
    st.markdown(f"""
    <div class="pdf-frame">
        <h2 style="color: #1e3a8a; margin: 0;">RELATÓRIO DE AUDITORIA EXECUTIVA</h2>
        <p><b>Data:</b> {datetime.now().strftime('%d/%m/%Y')} | <b>Líder:</b> {lider_sel}</p>
        <hr>
        <p>Aporte Identificado: <b>R$ {v_total:,.2f}</b></p>
        <table style="width:100%; color: black;">
            <tr style="background-color: #f2f2f2;">
                <th style="text-align:left;">MÉTRICA</th>
                <th style="text-align:right;">RESULTADO</th>
            </tr>
            <tr>
                <td>Leads Projetados</td>
                <td style="text-align:right;">{int(leads_totais)}</td>
            </tr>
            <tr>
                <td>Eficiência ({p_ok}%)</td>
                <td style="text-align:right; color: green;">R$ {v_liberado:,.2f}</td>
            </tr>
            <tr>
                <td><b>STATUS</b></td>
                <td style="text-align:right;"><b>{info['status'].upper()}</b></td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    # Botão de Download Sincronizado
    txt = f"AUDITORIA EQI\nLIDER: {lider_sel}\nTOTAL: R$ {v_total}\nSTATUS: {info['status']}"
    st.download_button("📥 BAIXAR RELATÓRIO", txt.encode('utf-8-sig'), f"{lider_sel}.txt")

st.info(f"💡 **IA-SENTINELA:** O status '{info['status']}' identifica a zona de vácuo (Death Zone).")
    
