import streamlit as st
import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from stop_words import get_stop_words
from joblib import dump, load

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

@st.cache
def check_msg(text: str) -> str:
    """
    Check the offensivity level of a text

    Parameter:
    text (str): string to analyse

    Returns:
    str : level of offensivity
    """
    clf = load('clf.joblib')
    data_input=[re.sub("[^A-Za-z']+", ' ', text.lower())]
    predict=clf.predict(data_input)
    if predict==0:
        return "Your message contains : Hate speech."
    elif predict==1:
        return "Your message contains : Offensive language."
    else:
        return "Your message doesn't contain hate speech neither offensive language."
def main():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    df=pd.read_csv('Data/labels.csv', usecols=['class', 'tweet'])
    df['tweet'] = df['tweet'].apply(lambda tweet: re.sub("[^A-Za-z']+", ' ', tweet.lower()))
    

    st.title('Sentiment analysis on language - Detecting hate speech')

    # Showing an extract of the training dataset
    st.markdown("The algorithm was trained on a dataset containing more than 23 000 tweets. An extract of the dataset can be explored below.<br/> Their level of offensivity was rated on a 3-points scale.",unsafe_allow_html=True)
    st.markdown("- 0: Hate speech  \n - 1: Offensive language  \n - 2: Neither")

    exp_affichage=st.beta_expander("Training dataset", False)
    with exp_affichage :
        len_to_filter=exp_affichage.slider("Number of displayed rows",1,100,10)
        exp_affichage.table(df.head(len_to_filter))


    st.subheader('Word Cloud representation for the dataset')
    # Joining every tweet of the dataset
    text = " ".join(tweet for tweet in df.tweet)

    # Create and generate a word cloud image
    wordcloud = WordCloud(max_font_size=50, mode="RGBA", background_color="white", scale=10, colormap='inferno').generate(text)

    # Display the generated image
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


    st.pyplot()

    st.title('Now test it with your own message !')

    user_input = st.text_area("Your message :", "Type here")

    if st.button('Check it !'):
        st.write(check_msg(user_input))

    st.title('Do you want to check my other work ?')
    st.markdown("I'm an IT student and I develop applications as exercises and for fun.  \n If you want to know more about me, check the link below.")
    st.markdown('<a style="display:inline-block; margin:auto;padding:0px 15px;background-color:#fff;border:solid 1px; border-color:rgba(238, 240, 244); color:rgb(38, 39, 48); border-radius:5px; text-align:center;line-height:33px;text-decoration: none;" href="http://webapp-h3.herokuapp.com/" target="_blank">Click here</a>',unsafe_allow_html=True)
    
if __name__ == '__main__':
    main()