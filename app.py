import streamlit as st

st.title("Redirect to Google after 5 seconds")

st.markdown("""
<div>
    <p>Lorem ipsum</p>
    <script>
    console.log("The JavaScript code is executed!");

    setTimeout(function() {
        window.location.href = 'https://www.google.com';
    }, 5000);
    </script>
</div>
""", unsafe_allow_html=True)
