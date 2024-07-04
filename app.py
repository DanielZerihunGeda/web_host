import streamlit as st
import base64

def main():
    st.set_page_config(
        page_title="HTML CSS Login Form",
        page_icon=":unlock:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Function to read and encode an image to base64
    def get_base64_image(file_path):
        with open(file_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    # Read and replace the base64 image placeholder
    img_base64 = get_base64_image("static/background.jpg")
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    html_code = html_code.replace("{{img_base64}}", img_base64)

    # Render HTML in Streamlit
    st.components.v1.html(html_code, height=800, scrolling=True)

if __name__ == "__main__":
    main()
