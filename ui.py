import streamlit as st

def render_ui(functions:dict)->None:
    st.title("MaoMao")
    function = st.selectbox("Выберите тип входных данных",functions.keys())
    input_str = st.text_input("Введите входные данные")
    if st.button('Старт'):
        try:
            fu = functions[function]
            st.code(fu(input_str))
        except Exception as e:
            st.error(f"Произошла ошибка:\n\n{e}") 

   
