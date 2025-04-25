import streamlit as st 
import plotly.express as px

st.header('Maiores valores')

if 'dados' not in st.session_state: 
    st.error('Dados não estão disponíveis')
else: 
    top_n = st.session_state.get('top_n', 10)
    dados = st.session_state['dados']

    col1, col2, col3 = st.columns(3)

    with col1: 

        m_empenho = dados.nlargest(top_n,'VALOREMPENHO')
        fig = px.bar(m_empenho, x='MUNICIPIO', y='VALOREMPENHO', title='Maiores empenhos')
        st.plotly_chart(fig, use_container_width=True)

    with col2: 

        m_pibs = dados.nlargest(top_n,'PIB')
        fig2 = px.pie(m_pibs, values='PIB', names='MUNICIPIO' , title='Maiores PIBS')
        st.plotly_chart(fig2, use_container_width=True)

    with col2: 

        m_prop = dados.nlargest(top_n,'PROPORCAO')
        fig3 = px.bar(m_prop, x='MUNICIPIO', y='PROPORCAO', title='Maiores gastos em proporção ao PIB')
        st.plotly_chart(fig3, use_container_width=True)