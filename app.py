import streamlit as st
import streamlit.components.v1 as components

st.title("Redirect to Google after 5 seconds")

components.html(
    """
    <script>
    setTimeout(function() {
        window.location.href = 'https://www.google.com';
    }, 5000);
    </script>
    """,
    height=0,
)
