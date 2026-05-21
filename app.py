import streamlit as st
st.title('Motor - Aluguel de carros')
st.sidebar.title('Escolha o seu modelo')
st.sidebar.image('logo.png')

carros = ('BMW', 'Audi', 'Skyline', 'Ferrari', 'Porsche', 'Mustang')

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')


dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?  ')
km = st.text_input(f'Quantos km você rodou com o {opcao}? ')

if opcao == 'BMW':
    diaria = 550 

elif opcao == 'Audi':
    diaria = 440

elif opcao == 'Skyline':
    diaria = 500

elif opcao == 'Ferrari':
    diaria = 600

elif opcao == 'Porsche':
    diaria = 500

elif opcao == 'Mustang':
    diaria = 500 

if st.button('Calcular'):
    dias = int(dias)
    km = float((km))

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st. warning(f'Você alugou o {opcao} por {dias} dias e rodou {km} km. O valor total do aluguel é: R${aluguel_total}')