import streamlit as st

# Page config
st.set_page_config(page_title="Research Profile", page_icon="🎓", layout="wide")

# Header
st.title("🎓 Ben Maapea - Research Profile")
st.subheader("BSc Physics & Mathematics | Aspiring Data Scientist & AI Developer")

# About
st.header("👤 About Me")
st.write("""
I am a final-year BSc student majoring in **Physics and Mathematics** at North-West University.
I am passionate about **data science, artificial intelligence, machine learning, and scientific research**.
My goal is to build intelligent systems and contribute to impactful research.
""")

# Education
st.header("🎓 Education")
st.write("""
**BSc in Physics and Mathematics**  
North-West University  
2022 – 2025
""")

# Research Interests
st.header("🔬 Research Interests")
st.markdown("""
- Artificial Intelligence  
- Machine Learning  
- Data Science  
- Computational Physics  
- Scientific Computing  
- Quantum Physics  
""")

# Skills
st.header("🛠 Skills")
st.markdown("""
- Python  
- Streamlit  
- Pandas  
- NumPy  
- Data Analysis  
- Scientific Computing  
- Bash  
""")

# Projects
st.header("📂 Projects")
st.markdown("""
- **Matthew AI** – Personal AI assistant inspired by Jarvis  
- Data analysis projects using Python  
- Streamlit web applications  
- Physics simulations  
""")

# Contact
st.header("📧 Contact")
st.write("Email: your_email@example.com")
st.write("LinkedIn: https://linkedin.com")
st.write("GitHub: https://github.com")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")