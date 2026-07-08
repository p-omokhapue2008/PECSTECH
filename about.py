import streamlit as st

st.title("About PECSTECH")

st.markdown("---")


st.header("Who We Are")

st.write("""
PECSTECH is a technology company dedicated to delivering innovative digital solutions
that help businesses and individuals succeed in today's digital world.

We specialize in website development, software development, data analytics,
UI/UX design, cloud solutions, and cybersecurity. Our goal is to transform
ideas into practical, reliable, and scalable technology solutions.
""")

col1, col2 , col3 = st.columns(3)
with col1:
   st.image('./bustech/cybersec.jpg')

with col2:
    st.image('./bustech/aithing.jpg')

with col3:
    st.image('./bustech/webdev.jpg')

st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    st.subheader("Our Mission")
    st.write("""
    To provide innovative, reliable, and affordable technology solutions
    that empower businesses and individuals through digital transformation.
    """)

with col2:
    st.subheader("Our Vision")
    st.write("""
    To become a trusted technology company recognized for innovation,
    excellence, and quality digital solutions.
    """)

st.markdown("---")

st.header("Our Services")

services = [
    "Website Development",
    "Software Development",
    "Data Analytics",
    "Cloud Solutions",
    "UI/UX Design",
    "Cybersecurity Consulting",
    "AI-Powered Solutions"
]

for service in services:
    st.write(f"- {service}")

st.markdown("---")

st.header("Why Choose PECSTECH?")
st.image('./bustech/whychooseus.jpg', width=400)


col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Innovation")
    st.write("We create modern and scalable digital solutions.")

with col2:
    st.subheader("Customer Focus")
    st.write("Every project is designed with our clients' needs in mind.")

with col3:
    st.subheader("Quality")
    st.write("We are committed to delivering reliable and high-quality services.")


st.markdown("---")

st.header("Our Core Values")

values = [
    "Innovation",
    "Integrity",
    "Excellence",
    "Collaboration",
    "Continuous Learning",
    "Customer Satisfaction"
]

for value in values:
    st.write(f"- {value}")

st.markdown("---")

st.write(
    "At PECSTECH, we believe technology should solve problems, inspire innovation, "
    "and create opportunities for businesses and communities."
)

st.markdown("---")
