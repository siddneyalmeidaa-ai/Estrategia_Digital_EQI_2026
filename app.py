import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÃO MASTER
st.set_page_config(page_title="IA-SENTINELA | ESTRATÉGIA EQI", layout="wide")

# 2. ESTILO VISUAL (PADRÃO OURO)
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

# --- 🧠 BASE DE DADOS (LIDERANÇAS) ---
dados_lideres = {
    "LIDERANÇA ALPHA": {"valor": 16000.0, "custo_lead": 25.0, "risco": 15},
    "LIDERANÇA BRAVO": {"valor": 22500.0, "custo_lead": 30.0, "risco": 45},
    "LIDERANÇA CHARLIE": {"valor": 45000.0, "custo_lead": 22.0, "risco": 10}
}

lider_sel = st.selectbox("Selecione a Liderança para Auditoria:", list(dados_lideres.keys()))
info = dados_lideres[lider_sel]

# --- 📈 CÁLCULOS DINÂMICOS ---
v_total = info["valor"]
leads_totais = v_total / info["custo_lead"]
p_risco = info["risco"]
p_ok = 100 - p_risco

# CONFIGURAÇÃO DA COLUNA DE STATUS COM A EXPLICAÇÃO QUE VOCÊ PEDIU
fases = ["1. Início", "2. Escala", "3. Expansão", "4. Consolidação"]
invest_fase = [v_total * 0.2, v_total * 0.5, v_total * 0.8, v_total]
leads_fase = [int(leads_totais * 0.2), int(leads_totais * 0.5), int(leads_totais * 0.8), int(leads_totais)]

# STATUS DETALHADO (A LÓGICA QUE VOCÊ SOLICITOU)
status_detalhado = [
    "✅ ENTRA: Métrica saudável. Captação liberada e operacional.",
    "✅ ENTRA: Escala validada. Fluxo de leads constante.",
    "⚠️ VÁCUO: Alerta Sentinela! Risco de custo alto. Atenção imediata.",
    "🚫 NÃO ENTRA: Bloqueio de segurança. Otimizar fase anterior."
]

df_favelinha = pd.DataFrame({
    "Fase Estratégica": fases,
    "Investimento (R$)": [f"R$ {x:,.2f}" for x in invest_fase],
    "Leads Esperados": leads_fase,
    "Status IA-SENTINELA": status_detalhado
})

aba1, aba2, aba3 = st.tabs(["📊 DASHBOARD", "📈 GRÁFICOS", "📄 RELATÓRIO EXECUTIVO"])

with aba1:
    st.markdown(f"### Auditoria de Performance: {lider_sel}")
    c1, c2 = st.columns(2)
    c1.metric(f"LIBERADO ({p_ok}%)", f"R$ {v_total*(p_ok/100):,.2f}")
    c2.metric(f"PENDENTE ({p_risco}%)", f"R$ {v_total*(p_risco/100):,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.divider()
    st.write("### 📝 Tabela da Favelinha (Detalhada)")
    # Exibindo a tabela com a explicação completa no Status
    st.table(df_favelinha)

with aba2:
    st.write("### 📈 Evolução de Leads por Fase")
    st.line_chart(pd.DataFrame({"Leads": leads_fase}, index=fases))

with aba3:
    # RELATÓRIO PDF COM A EXPLICAÇÃO NOS STATUS
    st.markdown(f"""
    <div class="pdf-frame">
        <h2 style="color: #1e3a8a; margin: 0;">DOSSIÊ DE AUDITORIA - EQI 2026</h2>
        <p><b>Liderança:</b> {lider_sel} | <b>Data:</b> {datetime.now().strftime('%d/%m/%Y')}</p>
        <hr>
        <p><b>Resumo da Coluna de Status:</b></p>
        <ul style="color: black; font-size: 14px;">
            <li><b>ENTRA:</b> Indica que a captação está dentro do custo planejado.</li>
            <li><b>VÁCUO:</b> Detectado desvio no custo por lead (Zona de Morte).</li>
            <li><b>NÃO ENTRA:</b> Interrupção preventiva para evitar queima de caixa.</li>
        </ul>
        <table style="width:100%; border-collapse: collapse; color: black; font-size: 12px;">
            <tr style="background-color: #f2f2f2;">
                <th style="padding: 8px; text-align: left;">FASE</th>
                <th style="padding: 8px; text-align: left;">STATUS DETALHADO</th>
            </tr>
            {"".join([f"<tr><td style='border-bottom: 1px solid #eee; padding: 8px;'>{fases[i]}</td><td style='border-bottom: 1px solid #eee; padding: 8px;'>{status_detalhado[i]}</td></tr>" for i in range(len(fases))])}
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    # Download seguro
    txt_relatorio = df_favelinha.to_csv(index=False).encode('utf-8-sig')
    st.download_button("📥 BAIXAR DOSSIÊ COMPLETO", txt_relatorio, f"Auditoria_{lider_sel}.csv
                      
