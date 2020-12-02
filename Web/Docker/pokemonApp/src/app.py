from flask import Flask
import streamlit as st
from flask import render_template
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def main():
    st.title("Streamlit Pokemon")

if __name__ == '__main__':
    main()