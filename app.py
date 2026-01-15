import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÃO DE SEGURANÇA E TELA
st.set_page_config(page_title="IA-SENTINELA | EQI PRO", layout="wide")

# 2. ESTILO VISUAL (CSS) - INCLUINDO O NOVO MÓDULO DE RELATÓRIO PDF
st.markdown("""
<style>
    [data-testid="stHeader"] {display: none;}
    
    /* Moldura estilo Dossiê PDF */
    .pdf-preview { 
        background: white; 
        color: #1a1a1a; 
        padding: 30px; 
        border-radius: 8px; 
        font-family: 'Courier New', monospace; 
        font-size: 0.9rem; 
        border-top: 15px solid #1e3a8a;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        line-height: 1.4;
        margin-top: 20px;
    }
    
    /* Ajuste para as métricas no Dashboard */
    .stMetric { 
        background-color: #161b22; 
        border-radius: 10px; 
        padding: 15px; 
        border: 1px solid #30363d; 
    }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO FIXO
st.title("🛡️ SISTEMA IA-SENTINELA PRO")
st.write(f"**Gestor Responsável:** Sidney Almeida | EQI 2026")

# --- 🧠 BASE DE DADOS SINCRONIZADA POR LÍDERES ---
dados_lideres = {
    "LIDERANÇA ALPHA": {"valor": 16000.0, "risco": 32, "status": "entra"},
    "LIDERANÇA BRAVO": {"valor": 22500.0, "risco": 45, "status": "vácuo"},
    "LIDERANÇA CHARLIE": {"valor": 45000.0, "risco": 18, "status": "não entra"}
}

lider_sel = st.selectbox("Selecione o Líder para Auditoria:", list(dados_lideres.keys()))
info = dados_lideres[lider_sel]

# --- 📈 CÁLCULOS DINÂMICOS ---
p_risco = info["risco"]
p_ok = 100 - p_risco
v_liberado = info["valor"] * (p_ok / 100)
v_pendente = info["valor"] * (p_risco / 100)

aba1, aba2, aba3 = st.tabs(["📊 DASHBOARD", "📈 GRÁFICO", "📄 RELATÓRIO (DOSSIÊ)"])

with aba1:
    st.markdown(f"**Análise de Desempenho: {lider_sel}**")
    c1, c2 = st.columns(2)
    # Títulos agora são os percentuais conforme regra de ouro
    c1.metric(f"LIBERADO ({p_ok}%)", f"R$ {v_liberado:,.2f}")
    c2.metric(f"PENDENTE ({p_risco}%)", f"R$ {v_pendente:,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.divider()
    st.write("### 📝 Tabela da Favelinha (Liderança)")
    df_favelinha = pd.DataFrame({
        "Indicador": ["Faturamento Total", "Volume Liberado", "Volume Pendente", "Status Sentinela"],
        "Dados": [f"R$ {info['valor']:,.2f}", f"R$ {v_liberado:,.2f}", f"R$ {v_pendente:,.2f}", info['status'].upper()]
    })
    st.table(df_favelinha)

with aba2:
    st.markdown("<h4 style='text-align: center;'>Distribuição de Auditoria</h4>", unsafe_allow_html=True)
    df_p = pd.DataFrame({'Status': [f'{p_ok}%', f'{p_risco}%'], 'Perc': [p_ok, p_risco]})
    st.vega_lite_chart(df_p, {
        'width': 'container', 'height': 300,
        'mark': {'type': 'arc', 'innerRadius': 80, 'outerRadius': 120},
        'encoding': {
            'theta': {'field': 'Perc', 'type': 'quantitative'},
            'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#00d4ff', '#ff4b4b']}}
        }
    })

with aba3:
    # --- IMPLANTAÇÃO DA ESTRUTURA DE RELATÓRIO DO CÓDIGO ANTERIOR ---
    if st.button("🔄 GERAR DOSSIÊ CONSOLIDADO"):
        
        # Montagem do texto do Dossiê
        relatorio_texto = (
            "==========================================\n"
            "   DOSSIÊ DE AUDITORIA - IA-SENTINELA PRO \n"
            "==========================================\n"
            f"LIDERANÇA RESP. : {lider_sel}\n"
            f"DATA EMISSÃO    : {datetime.now().strftime('%d/%m/%Y')}\n"
            "------------------------------------------\n"
            f"Faturamento Total  : R$ {info['valor']:,.2f}\n"
            f"Percentual Correto : {p_ok}% (R$ {v_liberado:,.2f})\n"
            f"Percentual Risco   : {p_risco}% (R$ {v_pendente:,.2f})\n"
            "------------------------------------------\n"
            f"MOTIVO PRINCIPAL   : Análise de Fluxo Sentinela\n"
            f"STATUS IA-SENTINELA: {info['status'].upper()}\n"
            "==========================================\n"
        )
        
        # Renderização visual estilo PDF (Fundo Branco/Letra Preta)
        st.markdown(f"""
        <div class="pdf-preview">
            <pre style="white-space: pre-wrap; color: #1a1a1a; background: transparent; border: none;">{relatorio_texto}</pre>
        </div>
        """, unsafe_allow_html=True)
        
        # Botão de Download Sincronizado
        st.download_button(
            label="📥 BAIXAR RELATÓRIO OFICIAL (.TXT)",
            data=relatorio_texto.encode('utf-8-sig'),
            file_name=f"Dossie_{lider_sel.replace(' ', '_')}.txt",
            mime="text/plain"
        )

st.info("💡 **IA-SENTINELA:** O status 'vácuo' identifica a zona de morte monitorada pela Sentinela.")
