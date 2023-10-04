import streamlit as st
from openai_utils import slide_title, slide_content
from ppt import create_presentation, download_link

def main():
    st.title("Generacion de presentaciones")

    topic = st.text_input("Escribe el tema de la presentacion:")
    generate_button = st.button("Crear presentacion")

    if generate_button and topic:
        st.info("Generando presentacion... Por favor espera.")
        slide_titles = slide_title(topic)
        filtered_slide_titles= [item for item in slide_titles if item.strip() != '']
        slide_contents = [slide_content(title) for title in filtered_slide_titles]
        create_presentation(topic, filtered_slide_titles, slide_contents)

        st.success("Presentacion generado correctamente!")
        st.markdown(download_link(topic), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
