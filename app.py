import streamlit as st
import pandas as pd 
from dados import df, faturamento,topBuyers
from personal_functions import format_number as fn

st.set_page_config(layout='wide')
st.title('Dashboard Revenue')

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Faturamento Total',value=fn(sum(faturamento),'R$'), )
    with col2:
        st.metric('Último mês', value=fn(faturamento[-1],prefix='R$'), delta=(fn(faturamento[-1]-faturamento[-2],prefix='R$')), delta_color='off')

st.header('Faturamento por mês', divider='rainbow')
st.line_chart(faturamento)

st.header('Compras por cliente', divider='rainbow')
st.bar_chart(topBuyers, x='EmpresaID', y='Data')

