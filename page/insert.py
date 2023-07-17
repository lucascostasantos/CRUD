import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados')
    especializacao = ['Python', 'JavaScript', 'C#', 'PHP', 'C++']
    
    with st.form(key='insert'):
        input_name = st.text_input(label='Insira o nome:')
        input_email = st.text_input(label='Insira seu email')
        input_job = st.selectbox(label='Insira sua linguagem de desenvolvimento', options=especializacao)
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_name, input_email, input_job)
            st.success('Programador incluido com sucesso')