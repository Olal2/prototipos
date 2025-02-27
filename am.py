import streamlit as st
from datetime import datetime
import pandas as pd

st.title('TABLA AMORTIZACION')
fechafin = datetime.today().date()
st.write(f'Fecha: {fechafin}')
valorcasa = st.number_input('Ingresa el valor de la propiedad:', min_value=0.0, format="%.2f")
eng = st.number_input('Porcentaje para enganchar:', min_value=0.0, max_value=100.0, format="%.2f") / 100
enganche = valorcasa * eng
st.write(f'Enganche a dar: ${enganche:,.2f}')
tasaanual=st.number_input('Tasa anual (%):', min_value=0.0, format="%.2f") / 100
periodoanos=st.number_input('Años: ', min_value=1,step=1)
valormort=valorcasa-enganche
tasamens=tasaanual/12
nper=periodoanos*12
if tasamens>0:
    pagomens=valormort/((1-(1/(1+tasamens)**nper))/tasamens)
else:
    valormort/nper
st.subheader(f'Pago mensual: ${pagomens:,.2f}')

balance=valormort
data = []
for mes in range(1, nper + 1):
    interes = balance * tasamens  # Interés del mes
    interes=interes
    principal = pagomens - interes  # Pago a capital
    balance_final = balance - principal  # Nuevo saldo
    data.append([mes, balance, pagomens, interes, principal, balance_final])
    balance = balance_final  # El balance final se convierte en el inicial del siguiente mes

df = pd.DataFrame(data,columns=["Mes","Balance Inicial","Pago mensual","  Interes  ","Principal","Balance Final"])
st.write("Tabla de pagos por mes:")
st.dataframe(df)

