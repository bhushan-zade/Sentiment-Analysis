import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Function to check and download NLTK resources if they are not found
def download_nltk_resources():
    try:
        nltk.data.find('tokenizers/punkt')
        st.write("Punkt tokenizer found.")
    except LookupError:
        st.write("Punkt tokenizer not found, downloading...")
        nltk.download('punkt')

    try:
        nltk.data.find('corpora/stopwords')
        st.write("Stopwords found.")
    except LookupError:
        st.write("Stopwords not found, downloading...")
        nltk.download('stopwords')

# Call the function to check and download resources
download_nltk_resources()

# Initialize PorterStemmer
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)  # This line uses the punkt tokenizer

    y = []
    for i in text: 
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load the TF-IDF vectorizer and model
tfidf = pickle.load(open('vectorizer1.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Set the title of the app
st.title("Sentiment Analysis - Movies Review")

# Input text area for the user
input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # 1. Preprocess the input
    transformed_sms = transform_text(input_sms)
    # 2. Vectorize the input
    vector_input = tfidf.transform([transformed_sms])
    # 3. Predict sentiment
    result = model.predict(vector_input)[0]
    # 4. Display the result
    if result == 1:
        st.header("Positive Sentiment")
    else:
        st.header("Negative Sentiment")
