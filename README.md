<img src=https://img.shields.io/badge/build%20with-python-yellow><img src="https://img.shields.io/badge/-streamlit-orange"> <img src="https://img.shields.io/badge/deployed%20in-Streamlit Cloudu-blue"> <img src="https://img.shields.io/badge/domain-Web%20Scraping-orange%20.svg" ><img src="https://img.shields.io/badge/Machine%20Learning-orange.svg"><img src="https://img.shields.io/badge/Natural%20Language%20Processing-orange%20.svg">


# IMDB- Movies Sentiment Analyzer

Sentiment analysis (also known as opinion mining or emotion AI) refers to the use of natural language processing, text analysis, computational linguistics, and bio metrics to systematically identify, extract, quantify, and study affective states and subjective information. Sentiment analysis is widely applied to voice of the customer materials such as reviews and survey responses, online and social media, and healthcare materials for applications that range from marketing to customer service to clinical medicine. (source: Wikipedia)

Application of Sentiment analysis is done to know about public reaction of any product, service, movie and event. Based on sentiment of consumers organization is able to implement improvement, innovation even can take actions . Movie Sentiment analysis tells weather a particular movie review is positive or negative, that means a user basically enjoyed, loved the movie or not. 

This Project is divided into 3 major segments :

    1.Machine Learning Segment  
    2.Web Scraping Segment  
    3.Web Development & Deployment Segment.

1.Machine Learning: 
  Movie review data, available in kaggle , was treated as fuel for this project. Although a subset of the available data has been used for this project. There were several issues with the data which has been solved (known as data prepossessing) by removing the HTML tags, special characters, stop words & performing stemming on the 'review' column. One more important concept called Bag-Of-Words(BOW) model is used for feature extraction which is achieved through CountVectorizer, which provides a simple way to both tokenization, a collection of text documents and build a vocabulary of known words, but also to encode new documents using that vocabulary, has been used before applying machine learning algorithm. Naive Bayes algorithm has been used after performing above steps. Based on the performance of Bernoulli Naive Bayes has been selected among Gaussian Naive Bayes, Multinational Naive Bayes, Bernoulli Naive Bayes algorithms. 

Data Source : https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

Data Prepossessing & Machine Learning algorithm Demo : https://www.kaggle.com/code/bhu1111/sentiment-analysis-movies-review

Used Machine Learning Model : https://github.com/bhushan-zade/imdb_webscrapping_and_sentiment_analysis/blob/main/sentiment%20Analysis.ipynb

2.Web Scraping : 
  Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. Web scraping software may access the World Wide Web directly using the Hypertext Transfer Protocol, or through a web browser. While web scraping can be done manually by a software user, the term typically refers to automated processes implemented using a bot or web crawler. It is a form of copying, in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis. ( source : Wikipedia)

For this project, IMDB website has been scraped using Beautiful Soup, a Python library for pulling data out of HTML files. Scraped data has been used to build a web app which will be able to distinguish between positive and negative review of a movie. This web app has two sections, one where visitors can witness the sentiment of movie reviews available in IMDB and the second section encourage visitors to predict their sentiment by writing a movie review. 

Web Scraping File: https://github.com/bhushan-zade/imdb_webscrapping_and_sentiment_analysis/blob/main/Imdb_Scraping.ipynb

3.Web Development & Deployment: 
  Python, Streamlit framework has been used for web development and the site was hosted in Streamlit Cloud as well. 

  Visit The Web App : https://bhushan-zade-sentiment-analysis-app-s2holg.streamlit.app/
  
<img align="" alt="coding" width="600" src= "https://user-images.githubusercontent.com/118050962/214591808-ccb3d604-4d84-4a27-b62d-29759f66420a.PNG">
