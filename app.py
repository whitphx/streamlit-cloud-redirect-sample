import streamlit as st

st.title("Redirect to Google after 5 seconds")

st.markdown("""
    <script>
    setTimeout(function() {
        window.location.href = 'https://www.google.com';
    }, 5000);
    </script>
""", unsafe_allow_html=True)
