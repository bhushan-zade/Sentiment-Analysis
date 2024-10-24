import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize the stemmer
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))  # Store stopwords in a set for efficiency

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    # Filter out non-alphanumeric characters
    y = [i for i in text if i.isalnum()]

    # Remove stopwords and punctuation
    y = [i for i in y if i not in stop_words and i not in string.punctuation]

    # Stemming
    y = [ps.stem(i) for i in y]

    return " ".join(y)

# Load the TF-IDF vectorizer and model
tfidf = pickle.load(open('vectorizer1.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Sentiment Analysis - Movies Review")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    if input_sms:  # Check if there is input
        # 1. Preprocess
        transformed_sms = transform_text(input_sms)
        # 2. Vectorize
        vector_input = tfidf.transform([transformed_sms])
        # 3. Predict
        result = model.predict(vector_input)[0]
        # 4. Display
        if result == 1:
            st.header("Positive Sentiment")
        else:
            st.header("Negative Sentiment")  # Corrected typo
    else:
        st.warning("Please enter a message to analyze.")
