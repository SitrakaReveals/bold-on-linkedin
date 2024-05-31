import streamlit as st

def to_bold(text):
    # LinkedIn uses Unicode characters for bold text
    bold_text = ''
    for char in text:
        if 'a' <= char <= 'z':
            bold_text += chr(ord(char) + 119743)
        elif 'A' <= char <= 'Z':
            bold_text += chr(ord(char) + 119737)
        else:
            bold_text += char
    return bold_text

st.title('LinkedIn Text Formatter')

input_text = st.text_area("Input your text here...")

if st.button('Convert to Bold'):
    bold_text = to_bold(input_text)
    st.text_area("Bold Text", value=bold_text, height=200)

