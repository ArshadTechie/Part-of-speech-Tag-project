import streamlit as st
import pickle
from keras.utils import pad_sequences
from keras.models import load_model
import numpy as np
import os

st.set_page_config(page_title="POS Tagger", page_icon="📖", layout="centered")
st.title("📖 Parts of Speech Tagger")

# Sidebar for page navigation
with st.sidebar:
    st.header("Navigation")
    pages = st.radio('Pages', ['Home', 'Individual Word'])

# Global variables to store input and POS results
if 'inp_list' not in st.session_state:
    st.session_state['inp_list'] = []
if 'pos_result_list' not in st.session_state:
    st.session_state['pos_result_list'] = []

# Define the path to the GIF file
# Use a relative path if 'please-wait.gif' is in the same directory as this script
# If it's in a different directory, use the correct absolute path
gif_path = "please-wait.gif"

def home():
    st.subheader("Enter a sentence to tag the parts of speech:")
    
    examples = ["The quick brown fox jumps over the lazy dog.", "Streamlit makes data apps easy to build.", "Natural Language Processing is fascinating."]
    example = st.selectbox("Choose an example:", examples)
    inp = st.text_input("Or enter your own string", example)
    
    submit_btn = st.button("Submit", key='submit_btn')  # Added key to force refresh
    
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #4CAF50; /* Green background */
            color: white; /* White text */
            font-size: 16px; /* Increase font size */
        }
        </style>
        """, unsafe_allow_html=True)
    
    if submit_btn and inp:
        model = pickle.load(open(r"C:\Users\arsha\Downloads\pos tagging project\model.pkl", "rb"))
        tk_x = pickle.load(open(r"C:\Users\arsha\Downloads\pos tagging project\tok_x.pkl", "rb"))
        tk_y = pickle.load(open(r"C:\Users\arsha\Downloads\pos tagging project\tok_y.pkl", "rb"))

        with st.spinner("Tagging parts of speech..."):
            st.image(gif_path, width=300)  # Display please-wait.gif with larger size

            def pos_tags(inp):
                seq = tk_x.texts_to_sequences([inp])
                text = tk_x.sequences_to_texts(seq)[0].split()  # Get list of tokens
                st.markdown("<h3 style='font-size:24px'>Tokenized input:</h3>", unsafe_allow_html=True)
                st.markdown(", ".join(text), unsafe_allow_html=True)  # Display tokens separated by comma with space
                x = pad_sequences(seq, maxlen=271, padding='post')
                seqs = np.argmax(model.predict(x)[0], axis=1)[np.argmax(model.predict(x)[0], axis=1) != 0]
                pos = tk_y.sequences_to_texts([seqs])[0].split()  # Get list of POS tags
                return list(zip(text, pos))  # Combine tokens and POS tags

            pos_results = pos_tags(inp)
        
        st.markdown("<h3 style='font-size:24px'>POS TAGS:</h3>", unsafe_allow_html=True)
        for token, pos_tag in pos_results:
            st.markdown(f"<span style='font-size:18px'><strong>{token}</strong> - <strong>{pos_tag}</strong></span>", unsafe_allow_html=True)

        st.session_state['inp_list'] = inp.split()  # Store the input list in the session state
        st.session_state['pos_result_list'] = pos_results  # Store the POS results in the session state

def individual_word():
    st.subheader("Check POS Tag for an Individual Word:")
    
    if st.session_state['inp_list']:
        st.markdown("Enter a word from the sequence you input on the Home page:")
        word = st.text_input("Word")
        sub_btn = st.button("Submit", key='sub_btn')  # Added key to force refresh
        
        st.markdown(
            """
            <style>
            .stButton>button {
                background-color: #4CAF50; /* Green background */
                color: white; /* White text */
                font-size: 16px; /* Increase font size */
            }
            </style>
            """, unsafe_allow_html=True)

        if word and sub_btn:
            if word in st.session_state['inp_list']:
                i = st.session_state['inp_list'].index(word)
                pos_tag = st.session_state['pos_result_list'][i][1]
                st.markdown(f"<h3 style='font-size:24px'>{word} - {pos_tag}</h3>", unsafe_allow_html=True)
            else:
                st.markdown("<h3 style='font-size:24px; color: red;'>The word is not in the input sequence. Please try another word.</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='font-size:24px; color: red;'>Go to the Home page and input a sequence first.</h3>", unsafe_allow_html=True)

if pages == 'Home':
    home()

if pages == 'Individual Word':
    individual_word()
