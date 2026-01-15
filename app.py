import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA 2026
st.set_page_config(page_title="IA-SENTINELA | SIDNEY ALMEIDA", layout="wide")

# ESTÉTICA PREMIUM E CORREÇÃO DE VISIBILIDADE
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    
    /* Garante que os números e textos apareçam no modo escuro/claro */
    .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; color: white !important; }
    
    /* ESTÉTICA DO RELATÓRIO PDF NO FRONT */
    .pdf-frame {
        background-color: white;
        color: #1a1a1a;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        margin-bottom: 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        border-top: 15px solid #1e3a8a;
    }
    .pdf-header { border-bottom: 2px solid #eee; margin-bottom: 20px; padding-bottom: 10px; }
    .pdf-title { color: #1e3a8a; font-size: 24px; font-weight: bold; text-transform: uppercase; }
    
    /* Forçar a tabela a respeitar o fundo branco do PDF */
    div[data-testid
    
