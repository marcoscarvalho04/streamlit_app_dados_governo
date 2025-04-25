import streamlit as st 
import plotly.express as px

st.header('Distribuição dos dados')

if 'dados' not in st.session_state: 
    st.error('Dados não estão disponíveis')
else: 
    dados = st.session_state['dados'].describe().reset_index()
    col_empenho, col_pib= st.columns(2)

    with col_empenho: 
        fig1 = px.histogram(dados, x='VALOREMPENHO', title='Histograma do valor de empenho')
        st.plotly_chart(fig1, use_container_width=True)
        
        fig2 = px.box(dados, x='VALOREMPENHO', title='BoxPlot do valor de empenho')
        st.plotly_chart(fig2, use_container_width=True)

    with col_pib:
        fig3 = px.histogram(dados, x='PIB', title='Histograma do valor do PIB')
        st.plotly_chart(fig3, use_container_width=True)

        fig4 = px.box(dados, x='PIB', title='BoxPlot do valor do PIB')
        st.plotly_chart(fig4, use_container_width=True)        


