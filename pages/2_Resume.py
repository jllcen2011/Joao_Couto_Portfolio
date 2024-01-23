import streamlit as st
import base64
from PIL import Image, ImageDraw

st.set_page_config(page_title="João Couto's CV", layout="wide", page_icon='🎓')

###################### sidebar ##########################3
css_style_1 = """
[data-testid=stSidebar] {
    background-image: linear-gradient(#333333, #DAF7A6);
}
"""


st.markdown(f'<style>{css_style_1}</style>', unsafe_allow_html=True)

st.markdown("""
    <style>
    .st-emotion-cache-10trblm {
            color: white
            }
    .st-emotion-cache-1dtefog {
            color: white
            }
    .st-emotion-cache-1hf5x7j {
            background-color: #bedb8a
            }
    .st-emotion-cache-1d3srhg p {
            color: white
            }
    .st-emotion-cache-fblp2m {
            color: white
            }
    .st-emotion-cache-lobgos {
            border-radius: 10px;
            border-style: solid;
            border-width: 1px;
            border-color: white;
    }
    .st-emotion-cache-pkbazv {
            color: white;
            }
    .st-emotion-cache-17lntkn {
            color: white;
            }       
    </style>
""",
            unsafe_allow_html=True
            )


# Foto
def create_circular_image(path, corner_offset=(100, -50)):
    img = Image.open(path)
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)

    # Calculate bottom right corner based on the offset
    bottom_right_corner = (img.size[0] - corner_offset[0], img.size[0] - corner_offset[1])

    draw.ellipse((100, 100) + bottom_right_corner, fill=180)
    mask = mask.resize(img.size, Image.Resampling.LANCZOS)
    img.putalpha(mask)

    return img

logotipo = create_circular_image('Imagens/foto2.jpeg')
st.sidebar.image(logotipo)

# links to linkedin and github
st.sidebar.markdown("""""")
st.sidebar.markdown("""""")
st.sidebar.markdown("""""")
st.sidebar.markdown("""""")
st.sidebar.markdown("""""")
st.sidebar.markdown("""""")

def get_image_as_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Encode your images
linkedin_image_base64 = get_image_as_base64("Imagens/linkedin_logo.png")
github_image_base64 = get_image_as_base64("Imagens/github_logo.png")

# URLs
linkedin_url = "https://www.linkedin.com/in/joaocouto1990/"
github_url = "https://github.com/jllcen2011?tab=repositories"

# HTML for clickable images
linkedin_html = f'<a href="{linkedin_url}" target="_blank"><img src="data:image/png;base64,{linkedin_image_base64}" width="40px"></a>'
github_html = f'<a href="{github_url}" target="_blank"><img src="data:image/png;base64,{github_image_base64}" width="40px"></a>'

# Use markdown to display HTML
with st.container():
    col15, col16, col17, col18 = st.sidebar.columns([0.3, 0.2, 0.2, 0.3])
    col16.markdown(linkedin_html, unsafe_allow_html=True)
    col17.markdown(github_html, unsafe_allow_html=True)

############################# Main #########################
st.title("📝 Resume")

st.write("Click here if it's blocked by your browser: ")

# File path to your PDF
pdf_file_path = "Imagens/resume.pdf"

# Set a label for the download button and the file name for the downloaded file
download_button_label = "Download Resume"
downloaded_file_name = "João Couto CV.pdf"

# Read the PDF file in binary mode
with open(pdf_file_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

# Create a download button and offer the PDF for download
st.download_button(label=download_button_label,
                   data=pdf_bytes,
                   file_name=downloaded_file_name,
                   mime="application/octet-stream")

with open("Imagens/resume.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
