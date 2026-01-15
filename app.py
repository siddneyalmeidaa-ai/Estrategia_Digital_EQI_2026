import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÃO MASTER
st.set_page_config(page_title="IA-SENTINELA | AUDITORIA EQI", layout="wide")

# 2. ESTILO VISUAL (CORREÇÃO DE SINTAXE)
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
    .status-box {
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO
st.title("🛡️ SISTEMA IA-SENTINELA PRO")
st.write(f"**Gestor Responsável:** Sidney Almeida | EQI 2026")

# --- 🧠 INTELIGÊNCIA DE DIAGNÓSTICO (O MOTIVO DO PENDENTE) ---
dados_lideres = {
    "LIDERANÇA ALPHA": {
        "valor": 16000.0, "custo_lead": 25.0, "risco": 32,
        "motivo_pendente": "Filtro de qualificação muito rígido no funil de conversão.",
        "direcionamento": "Ajustar segmentação de público no Meta Ads para ampliar o topo do funil."
    },
    "LIDERANÇA BRAVO": {
        "valor": 22500.0, "custo_lead": 30.0, "risco": 45,
        "motivo_pendente": "Lead Time elevado entre captura e primeiro contato do assessor.",
        "direcionamento": "Implementar automação de WhatsApp imediata para reduzir o vácuo de atendimento."
    },
    "LIDERANÇA CHARLIE": {
        "valor": 45000.0, "custo_lead": 22.0, "risco": 18,
        "motivo_pendente": "Saturação de criativos nas redes sociais (fadiga de imagem).",
        "direcionamento": "Renovar materiais educativos e mini-cursos para manter o engajamento."
    }
}

lider_sel = st.selectbox("Selecione o Líder para Auditoria:", list(dados_lideres.keys()))
info = dados_lideres[lider_sel]

# --- 📈 CÁLCULOS SINCRONIZADOS ---
v_total = info["valor"]
p_risco = info["risco"]
p_ok = 100 - p_risco
v_liber
