import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA 2026
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# BANDA DE BLINDAGEM E ESTÉTICA PREMIUM (Efeito PDF)
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
        padding: 40px;
        border-radius: 2px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        margin: 20px auto;
        max-width: 850px;
        font-family: 'Arial', sans-serif;
        border-top: 12px solid #1e3a8a;
    }
    .pdf-header { border-bottom: 2px solid #eee; padding-bottom: 15px; margin-bottom: 25px; }
    
