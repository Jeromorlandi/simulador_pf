# archivo: simulador_plazo_fijo.py

import streamlit as st

def simulador_plazo_fijo(capital, dias, tna):
    tasa_diaria = tna / 100 / 365
    interes_ganado = capital * tasa_diaria * dias
    tasa_mensual = tasa_diaria * 30 * 100  # en porcentaje
    return tasa_mensual, interes_ganado

# --------------------- Interfaz ---------------------

st.set_page_config(page_title="Simulador de Plazo Fijo", page_icon="💰")
st.title("📈 Simulador de Plazo Fijo")

st.markdown("""
Ingresá los datos de tu inversión para calcular el interés ganado y la tasa mensual estimada.
""")

# Inputs del usuario
capital = st.number_input("💵 Capital ($)", min_value=0.0, value=1000000.0, step=10000.0, format="%.2f")
dias = st.number_input("📅 Plazo en días", min_value=1, max_value=365, value=31)
tna = st.number_input("📊 TNA (Tasa Nominal Anual %)", min_value=0.0, max_value=100.0, value=28.0, step=0.1)

# Botón para calcular
if st.button("Calcular"):
    tasa_mensual, interes = simulador_plazo_fijo(capital, dias, tna)
    
    st.success(f"✅ Interés ganado: ${interes:,.2f}")
    st.info(f"📉 Tasa mensual estimada: {tasa_mensual:.2f}%")
