import streamlit as st

st.set_page_config(
    page_title="Research Profile | Ben Maapea",
    page_icon="🎓",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Profile", "Projects", "CV", "Contact"])

# -------------------- HOME --------------------
if page == "Home":
    st.title("🎓 Research Profile Web App")
    st.subheader("Ben Maapea | Physics & Mathematics Graduate")

    st.write("""
    Welcome to my **Research Profile Web Application** built using **Streamlit**.
    
    This platform showcases my academic background, research interests, skills, 
    and career aspirations in an interactive format.
    """)

    st.success("🚀 Fully deployed on Streamlit Cloud")

# -------------------- PROFILE --------------------
elif page == "Profile":
    st.title("👤 Profile")

    st.markdown("""
    **Name:** Ben Maapea  
    **Qualification:** BSc in Physics & Mathematics  
    **Career Goal:** Data Scientist / Quantitative Analyst  

    ### 🎓 Academic Background
    - BSc in Physics & Mathematics
    - Strong foundation in problem solving, modelling, and computation

    ### 🔬 Research Interests
    - Machine Learning
    - Data Science & Analytics
    - Computational Physics
    - Scientific Programming

    ### 🧠 Technical Skills
    - Python
    - Streamlit
    - Pandas
    - JupyterLab
    - Git & GitHub
    - Linux / Bash
    """)

# -------------------- PROJECTS --------------------
elif page == "Projects":
    st.title("📊 Projects Portfolio")

    st.markdown("""
    ### 🧪 Streamlit Research Profile App
    - Built an interactive academic portfolio using Streamlit
    - Deployed publicly using Streamlit Cloud
    - Implemented UI navigation and responsive design

    ### 📈 Data Science Mini Projects
    - Exploratory Data Analysis (EDA)
    - Machine Learning classification models
    - Data visualization dashboards

    *(More projects coming soon...)*
    """)

# -------------------- CV --------------------
elif page == "CV":
    st.title("📄 Curriculum Vitae")

    st.info("Click below to download my CV")

    with open("assets/Ben_Maapea_CV.pdf", "rb") as file:
        st.download_button(
            label="📥 Download CV",
            data=file,
            file_name="Ben_Maapea_CV.pdf",
            mime="application/pdf"
        )

# -------------------- CONTACT --------------------
elif page == "Contact":
    st.title("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Message")

        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success("Thank you! Your message has been received.")