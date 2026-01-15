import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÃO MASTER
st.set_page_config(page_title="IA-SENTINELA | EQI PRO", layout="wide")

# 2. ESTILO VISUAL (MOLDURA PDF CORRIGIDA)
st.markdown("""
<style>
    [data-testid="stHeader"] {display: none;}
    .pdf-preview { 
        background: white !important; 
        color: #1a1a1a !important; 
        padding: 30px; 
        border-radius: 8px; 
        font-family: 'Courier New', monospace; 
        border-top: 15px solid #1e3a8a;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO
st.title("🛡️ SISTEMA IA-SENTINELA PRO")
st.write(f"**Gestor Responsável:** Sidney Almeida | EQI 2026")

# --- 🧠 BASE DE DADOS (A BASE QUE NÓS MANDAMOS) ---
dados_lideres = {
    "LIDERANÇA ALPHA": {"valor": 16000.0, "risco": 32, "status": "entra"},
    "LIDERANÇA BRAVO": {"valor": 22500.0, "risco": 45, "status": "vácuo"},
    "LIDERANÇA CHARLIE": {"valor": 45000.0, "risco": 18, "status": "não entra"}
}

# SELETOR UNIFICADO
lider_sel = st.selectbox("Selecione o Líder para Auditoria:", list(dados_lideres.keys()))
info = dados_lideres[lider_sel]

# --- 📈 CÁLCULOS SINCRONIZADOS ---
p_risco = info["risco"]
p_ok = 100 - p_risco
v_liberado = info["valor"] * (p_ok / 100)
v_pendente = info["valor"] * (p_risco / 100)

aba1, aba2, aba3 = st.tabs(["📊 DASHBOARD", "📈 GRÁFICO", "📄 RELATÓRIO (DOSSIÊ)"])

with aba1:
    st.markdown(f"### Análise: {lider_sel}")
    c1, c2 = st.columns(2)
    # Títulos com os percentuais corretos
    c1.metric(f"LIBERADO ({p_ok}%)", f"R$ {v_liberado:,.2f}")
    c2.metric(f"PENDENTE ({p_risco}%)", f"R$ {v_pendente:,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.divider()
    # TABELA DA FAVELINHA SINCRONIZADA COM O LÍDER
    st.write("### 📝 Tabela da Favelinha")
    df_favelinha = pd.DataFrame({
        "Indicador de Auditoria": ["Faturamento Analisado", "Volume Liberado", "Volume Pendente", "Status Sentinela"],
        "Valores Reais": [f"R$ {info['valor']:,.2f}", f"R$ {v_liberado:,.2f}", f"R$ {v_pendente:,.2f}", info['status'].upper()]
    })
    st.table(df_favelinha)

with aba3:
    # --- GERADOR DE RELATÓRIO BASEADO NO CÓDIGO ENVIADO ---
    if st.button("🔄 GERAR DOSSIÊ CONSOLIDADO"):
        
        # Estrutura de texto do Dossiê
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
            f"STATUS IA-SENTINELA: {info['status'].upper()}\n"
            "==========================================\n"
        )
        
        # Mostra o relatório na moldura branca
        st.markdown(f"""
        <div class="pdf-preview">
            <pre style="white-space: pre-wrap; color: #1a1a1a; background: transparent; border: none; font-size: 14px;">{relatorio_texto}</pre>
        </div>
        """, unsafe_allow_html=True)
        
        # Download configurado para evitar erro de acento no celular
        st.download_button(
            label="📥 BAIXAR RELATÓRIO OFICIAL",
            data=relatorio_texto.encode('utf-8-sig'),
            file_name=f"Dossie_{lider_sel.replace(' ', '_')}.txt",
            mime="text/plain"
        )

st.info(f"💡 **IA-SENTINELA:** O status '{info['status']}' identifica o vácuo (Death Zone) da liderança.")
