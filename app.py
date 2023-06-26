import streamlit as st

st.title("Redirect to Google after 5 seconds")

st.markdown("""
[Click this link](https://www.google.com)
""")

st.markdown("""
[Click this link](https://www.google.com){:target="_blank" rel="noreferrer noopener"}
""")

st.markdown("""
<a href="https://www.google.com" target="_blank" rel="noreferrer noopener">Click this link</a>
""", unsafe_allow_html=True)

st.markdown("""
<div onload="alert('foo')">
    <p>Lorem ipsum</p>
    <script>
    console.log("The JavaScript code is executed!");

    setTimeout(function() {
        window.location.href = 'https://www.google.com';
    }, 5000);
    </script>
</div>
""", unsafe_allow_html=True)
