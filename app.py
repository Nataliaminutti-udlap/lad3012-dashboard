"""
Dashboard Superstore — Plantilla LAD3012 D09
========================================
Solo tienes que cambiar TU_NOMBRE y TU_ID antes de subir.
El INSIGHT lo escribes DESPUES de explorar tu dashboard publicado.
"""
import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================
# CONFIGURACION DE PAGINA
# ============================================================
st.set_page_config(
    page_title="Superstore Dashboard",
    page_icon="🛒",
    layout="wide"
)

# ============================================================
# PASO 1 — YA CAMBIASTE ESTAS DOS LINEAS
# ============================================================
TU_NOMBRE = "Natalia Minutti Jimenez"
TU_ID     = "179834"

# ============================================================
# PASO 2 — DEJA ESTO COMO ESTA. NO LO CAMBIES TODAVIA.
# ============================================================
TU_INSIGHT = """
Aun no he escrito mi insight. Lo agregare despues de explorar
los graficos y filtros de mi dashboard.
"""

# ============================================================
# CARGAR DATOS (con cache para velocidad)
# ============================================================
@st.cache_data
def cargar_datos():
    df = pd.read_csv("superstore.csv", encoding="latin-1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Year"]  = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
    return df

df = cargar_datos()

# ============================================================
# TITULO Y AUTOR
# ============================================================
st.title("🛒 Superstore — Dashboard Ejecutivo")
st.caption(f"Por **{TU_NOMBRE}** · ID {TU_ID} · LAD3012 · UDLAP Verano I 2026")
st.markdown("---")

# ============================================================
# FILTROS (sidebar)
# ============================================================
st.sidebar.header("🔍 Filtros")
regiones = st.sidebar.multiselect(
    "Region",
    options=sorted(df["Region"].unique()),
    d
