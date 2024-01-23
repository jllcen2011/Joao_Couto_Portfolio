import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
from PIL import Image, ImageDraw
import base64

st.set_page_config(page_title="João Couto's CV", layout="wide", page_icon='🎓')


# -----------------  sidebar  ----------------- #

# Sidebar gradient color
css_style = """
[data-testid=stSidebar] {
    background-image: linear-gradient(#333333, #DAF7A6);
}
"""

st.markdown(f'<style>{css_style}</style>', unsafe_allow_html=True)

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

# -----------------  loading assets  ----------------- #

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# loading assets
python_lottie = load_lottieurl(
    "https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
my_sql_lottie = load_lottieurl(
    "https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl(
    "https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl(
    "https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")

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

# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    return f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">' \
           f'<span style="color:{color3};">{content1}</span><br>' \
           f'<span style="color:white;font-size:17px;">{content2}</span></h1>'

# Use the function and pass its return value to st.markdown
st.markdown(gradient('#333333', '#DAF7A6', '#ffffff', "Hi, I'm João Couto👋", 
             "Data Analyst | MBA in Data Science - Curious, disciplined and structured life-learner!"), 
             unsafe_allow_html=True)
st.write("")

text = "I am passionate about harnessing the power of data to solve real-world challenges. My approach combines structured learning, innovative problem-solving and a commitment to developing scalable and impactful data solutions."
color = "white"  # You can use color names or hex values like '#ff0000' for red

# Using HTML to style the text
html = f"""
<div style='text-align: center; color: {color};'>
    {text}
</div>
"""

# Displaying the styled text
st.markdown(html, unsafe_allow_html=True)
st.write("")

# ----------------- skillset ----------------- #
st.markdown("""""")
st.markdown("""""")
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70, width=70, key="python", speed=2.5)
    with col2:
        st_lottie(my_sql_lottie, height=70, width=70, key="mysql", speed=2.5)
    with col3:
        st_lottie(git_lottie, height=70, width=70, key="git", speed=2.5)
    with col4:
        st_lottie(github_lottie, height=50, width=50, key="github", speed=2.5)

    

# -----------------  powerbi  -----------------  #
with st.container():
    st.markdown("""""")
    st.markdown("""""")

    # PowerBI logo and title
    powerbilogo = "https://raw.githubusercontent.com/microsoft/PowerBI-Icons/main/SVG/Power-BI.svg"
    col5, col6 = st.columns([1, 30])
    with col5:
        st.markdown(
            f"<img src='{powerbilogo}' style='vertical-align: -webkit-baseline-middle; width:30px;'>", 
            unsafe_allow_html=True
        )
    with col6:
        st.subheader("Powerbi")

    # PowerBI Expander, to show the work
    col7, col8 = st.columns([0.95, 0.05])
    with col7:
        with st.expander('See the work'):
            power_bi_dashboard_html = """<iframe title="cv2" width="1024" height="1060" src="https://app.powerbi.com/view?r=eyJrIjoiODMwMTI2N2ItYWZkNy00NWUyLWFmZDEtNmJjZDY5YjYzZGMzIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>"""
            components.html(power_bi_dashboard_html, height=800, scrolling=True)

    st.markdown("""🔗 <a href='{}'><em>access to the link</em></a>""".format("https://app.powerbi.com/view?r=eyJrIjoiODMwMTI2N2ItYWZkNy00NWUyLWFmZDEtNmJjZDY5YjYzZGMzIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"), unsafe_allow_html=True)

st.markdown("""""")
st.markdown("""""")


# -----------------  streamlit  -----------------  #
with st.container():
    st.markdown("""""")

    # Streamlit logo and title
    streamlit_logo_url = "https://docs.streamlit.io/logo.svg"
    col9, col10 = st.columns([1, 18])  # Adjust the ratio as needed
    with col9:
        st.markdown(
            f"<img src='{streamlit_logo_url}' style='vertical-align: -webkit-baseline-middle; width:60px;'>", 
            unsafe_allow_html=True
        )
    with col10:
        st.subheader("Streamlit")
    
    # Streamlit Expander, to show the work
    col11, col12 = st.columns([0.95, 0.05])
    with col11:
        with st.expander('See the work'):
            st.markdown(
                f"""
                <iframe src="https://salestargetcouto.streamlit.app/?embedded=true" width="100%" height="1500" frameborder="0" scrolling="yes" allowFullScreen="true"></iframe>
                """,
                unsafe_allow_html=True
            )
    st.markdown("""🔗 <a href='{}'><em>access to the link</em></a>""".format("https://salestargetcouto.streamlit.app/"), unsafe_allow_html=True)


# -----------------  Medium  -----------------  #
st.markdown("""""")
st.markdown("""""")

embed_rss_1 = {
    'rss': """<div style="overflow-y: scroll; height:395px; background-color: #f0f7e4;"> 
    <div id="retainable-rss-embed" 
        data-rss="https://medium.com/feed/@jllcen2011"
        data-maxcols="1" 
        data-layout="grid"
        data-poststyle="inline" 
        data-readmore="Read the rest" 
        data-buttonclass="btn btn-primary" 
        data-offset="0">
    </div></div> 
    <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""
}


with st.container():
    st.subheader('✍️ Medium Posts')
    col13, col14 = st.columns([0.95, 0.05])
    with col13:
        with st.expander('Display my latest posts'):
            components.html(embed_rss_1['rss'], height=400)

    # Link to your Medium profile
    st.markdown("""🔗 <a href='{}'><em>access to the link</em></a>""".format("https://medium.com/@jllcen2011/data-science-mba-final-project-81b3b07ef34f"), unsafe_allow_html=True)

# -------------- sidebar links to linkedin and github ------------#
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


# -------------- header and footer ---------------- #
# Retirando a fita colorida na parte de cima do streamlit e o rodapé escrito Made with Streamlit
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
# st.markdown(hide_st_style, unsafe_allow_html=True)