import streamlit as st

def to_bold(text):
    # LinkedIn uses Unicode characters for bold text
    bold_text = ''.join(chr(ord(c) + 119743) if 'a' <= c <= 'z' else c for c in text.lower())
    return bold_text

st.title('LinkedIn Text Formatter')

input_text = st.text_area("Input your text here...")

if st.button('Convert to Bold'):
    bold_text = to_bold(input_text)
    st.text_area("Bold Text", value=bold_text, height=200)
