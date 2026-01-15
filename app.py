import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA 2026
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# ESTÉTICA PREMIUM (Efeito PDF Integrado)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    
    .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    
    .pdf-container {
        background-color: white;
        color: #1a1a1a;
        padding: 30px;
        border-radius: 4px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        font-family: 'Arial', sans-serif;
        border-top: 12px solid #1e3a8a;
    }
    .pdf-title { color: #1e3a8a; font-size: 22px; font-weight: bold; border-bottom: 2px solid #eee; padding-bottom: 10px; }
    /* Ajuste para a tabela dentro do PDF */
    .pdf-container table { color: black !important; }
    </style>
    """, unsafe_allow_html=True)
