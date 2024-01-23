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

############################# Main #########################
st.title("📝 Resume")

# st.write("[Click here if it's blocked by your browser](https://cognitiveclass.ai/)")

with open("Imagens/resume.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
  
