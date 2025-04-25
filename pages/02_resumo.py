import streamlit as st 

st.header('Resumo dos dados')

if 'dados' not in st.session_state: 
    st.error('Dados não estão disponíveis')
else: 
    dados = st.session_state['dados'].describe().reset_index()
    st.write(dados)
    