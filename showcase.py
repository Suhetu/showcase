import streamlit as st
from streamlit_option_menu import option_menu
import nbformat
from nbconvert import HTMLExporter
import base64

with st.sidebar:

    # st.title('📃 Directory')

    # Specifying sidebar menu options
    selected = option_menu(
        menu_title = 'Directory',
        options = ['Home', 'Climate & Earthquakes', 'SkyGuardian', 'PantryPal', 'S.D.O.H', 'AutoML', 'FormAnalyst', 'GenAI'],
        default_index = 0
    )

if selected == 'Home':

    st.title('Welcome,')

    st.subheader(':rainbow[Thank you] for taking time to visit! You can browse a few of my works via the tab over 👈🏻')

    st.write("")
    st.write("")

    st.image("https://files.realpython.com/media/Documenting-Python-Projects-With-Sphinx-and-Read-The-Docs_Watermarked.483b54b59fe0.jpg", caption="Python is FUN")

if selected == 'Climate & Earthquakes':

    st.title("Climate🌦️ & Earthquakes🌏")
    st.write("By **Suhetu Ring**")

    # Path to your notebook file
    notebook_path = "DATA 601 Endgame.ipynb"

    # Convert the notebook to HTML
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_content = nbformat.read(f, as_version=4)

    html_exporter = HTMLExporter()
    (html_body, resources) = html_exporter.from_notebook_node(notebook_content)

    # Display notebook HTML
    st.components.v1.html(html_body, height=800, scrolling=True)

if selected == 'SkyGuardian':

    st.title("SkyGuardian🌠")
    st.write("By **Suhetu Ring**")

    # Path to your notebook file
    notebook_path = "PHA Detection (Project ML).ipynb"

    # Convert the notebook to HTML
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_content = nbformat.read(f, as_version=4)

    html_exporter = HTMLExporter()
    (html_body, resources) = html_exporter.from_notebook_node(notebook_content)

    # Display notebook HTML
    st.components.v1.html(html_body, height=800, scrolling=True)

if selected == 'PantryPal':

    st.title("PantryPal😋")
    st.write("By **Suhetu Ring**")

    # Path to your notebook file
    notebook_path = "PantryPal.ipynb"

    # Convert the notebook to HTML
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_content = nbformat.read(f, as_version=4)

    html_exporter = HTMLExporter()
    (html_body, resources) = html_exporter.from_notebook_node(notebook_content)

    # Display notebook HTML
    st.components.v1.html(html_body, height=800, scrolling=True)

if selected == 'S.D.O.H':

    st.title("S.D.O.H🧑🏻‍⚕️")
    st.write("By **Suhetu Ring**")

    st.subheader("Discover the social and environmental factors that shape community health—just enter your ZIP code and get a complete snapshot of your neighborhood’s health indicators.")

    st.caption("This project was meant to be added as an extension to any doctor's EHR system. So a doctor would get SDOH details along with medical details for a patient.")

    st.write('You can have a hands on experience by visiting the following demo. Make sure to select SDOH in the webapp, and enter any zip code in California.')

    st.write('https://cloudleap-sdi.streamlit.app/')

if selected == 'AutoML':

    st.title("AutoML🧑🏻‍💻")
    st.write("By **Suhetu Ring**")

    def display_pdf(file_path):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    st.subheader("Project Summarization")
    display_pdf("Model Summary AutoML App-a-thon.pdf")

    st.subheader('We even won the FDA challenge, beating huge corporations like IBM!')

    st.image('AutoML_Cert.png')

if selected == 'FormAnalyst':

    st.title("FormAnalyst📄")
    st.write("By **Suhetu Ring**")

    st.subheader("This project extracts user filled information from a Customs and Border Protection form CBP-6059B and enables officers to query that data via a custom LLM build on that data, plus added functionalities.")

    st.write("")

    st.video('form_webapp.mp4')

if selected == 'GenAI':

    st.title("GenAI🤖")
    st.write("By **Suhetu Ring**")

    st.subheader("This project involves building a chatbot that uses an Agentic RAG Model built on custom data provided LLM. We can build AI agents in a similar manner on any data we have! The data input for this specific use case were a lot of FDA approved pdfs related to cosmetics.")

    st.write("")

    st.write('FDA Challenge: https://precision.fda.gov/challenges/34/intro')

    st.write("")

    st.video('genai.mp4')