import streamlit as st

def main():
    st.title("Streamlit Uygulaması")
    st.write("Hoş geldiniz! Bu, bir Streamlit uygulamasının başlangıç noktasıdır.")
    
    # Kullanıcı arayüzü bileşenleri burada tanımlanabilir
    user_input = st.text_input("Bir şey yazın:")
    if user_input:
        st.write(f"Girdiğiniz: {user_input}")

if __name__ == "__main__":
    main()