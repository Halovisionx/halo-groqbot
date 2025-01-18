import streamlit as st

def main():
    st.title("My Streamlit App")
    st.write("Hoş geldiniz! Bu uygulama veri yükleme, görselleştirme ve etkileşimli bileşenler içerir.")

    uploaded_file = st.file_uploader("Bir dosya yükleyin", type=["csv", "xlsx"])
    if uploaded_file is not None:
        # Dosya yüklendiğinde yapılacak işlemler
        st.success("Dosya yüklendi!")

if __name__ == "__main__":
    main()