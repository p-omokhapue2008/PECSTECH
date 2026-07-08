import streamlit as st
import streamlit.components.v1 as com

st.set_page_config(
    page_title="PECSTECH",
    layout="wide"
)

st.title("Welcome to PECSTECH")
st.subheader("Empowering Innovation Through Technology")
st.image('./bustech/techtech.jpg')

st.write("""
At PECSTECH, we transform ideas into innovative digital solutions.
From modern websites to custom software and data-driven applications,
we help businesses and individuals embrace the future through technology.
""")

st.markdown("---")

st.header("Our Services")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Web Development")
    st.write("Responsive and modern websites built for businesses and organizations.")

with col2:
    st.subheader("Software Development")
    st.write("Custom software solutions designed to solve real-world problems.")

with col3:
    st.subheader("Data Analytics")
    st.write("Turn data into valuable insights for smarter decision-making.")

st.markdown("---")

st.header("Why Choose PECSTECH?")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Innovative Solutions")
    st.write("We use modern technologies to build scalable products.")

with col2:
    st.write("Customer Focus")
    st.write("Our clients are at the heart of every solution we create. We take constructive feedback aswell to ensure that we deliver the best solutions for you.")

with col3:
    st.write("Quality Delivery")
    st.write("We are committed to delivering reliable, high-quality softwares and visuals.")

st.markdown("---")

st.header("Our Mission")

st.write("""
To deliver innovative, reliable, and affordable technology solutions
that empower businesses and individuals through digital transformation.
""")

st.markdown("---")

st.header("Ready to Work With Us?")

st.write("""
Whether you're looking for a website or technology consulting,
PECSTECH is here to help bring your ideas to life.
""")

st.subheader("Contact Us")
st.write("Email: info@pecstech.com")
st.write("Phone: +234 768 667 9086")

st.markdown("---")

