import streamlit as st

import controller.cliente as cliente


def excluir():
    st.title('Deletar Dados')
    
    with st.form(key='delete'):
        input_email = st.text_input(label='Insira o email:')
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.deletar(input_email)
            st.success('Programador excluido com sucesso')