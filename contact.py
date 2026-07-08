import streamlit as st

st.set_page_config(
    page_title="Contact Us | PECSTECH",
    layout="wide"
)

st.title("Contact Us")

st.write("""
If you have any questions or would like to discuss anything related to our services, feel free to reach out
        and fill out the form below or reach out using our contact information.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.header("Send Us a Message")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    subject = st.text_input("Subject")
    message = st.text_area("Description")

if st.button("Submit"):
        if name and email and subject and message:
            st.success("Thank you! Your message has been received.")
        else:
            st.fail("Please fill in all the fields before submitting.")

with col2:
    st.header("Our Contact Information")

    st.subheader("-Address:")
    st.write("Lekki, Lagos, Nigeria")

    st.subheader("-Email:")
    st.write("info@pecstech.com")

    st.subheader("-Phone Number:")
    st.write("+234 768 667 9086")

    st.subheader("-Business Hours:")
    st.write("""
    Monday - Thursday: 9:00 AM – 5:00 PM

    Saturday: CLOSED

    Sunday: 10:00 AM – 4:00 PM
    """)

st.markdown("---")




