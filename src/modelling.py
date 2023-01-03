import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Modelling:
    def __init__(self):
        nltk.download('punkt')
        self.vectorizer = TfidfVectorizer()

    def detect_language(self, text):
        # Create the vectorizer
        # Create the TF-IDF matrix
        tfidf_matrix = self.vectorizer.fit_transform(text)
        
        # Get the word indices
        word_indices = self.vectorizer.vocabulary_
        
        # Create a dictionary to store the TF-IDF scores
        tfidf_scores = {}
        
        # For each sentence, get the TF-IDF scores of the keywords
        for sentence in text:
            sentence_scores = {}
            sentence_tfidf = tfidf_matrix[text.index(sentence)].toarray()[0]
            for word in self.__extract_keywords(sentence):
                sentence_scores[word] = sentence_tfidf[word_indices[word]]
            
            tfidf_scores[sentence] = sentence_scores
        
        return tfidf_scores
    
    def __extract_keywords(self, sentence):
        words = word_tokenize(sentence)
        
        # Remove stop words
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word.lower() not in stop_words]
        
        # Extract keywords
        keywords = []
        for word in words:
            if word.isalpha():
                keywords.append(word.lower())
        
        return keywords

    def __rank_keywords(self, sentence):
        # Create the TF-IDF matrix for the single sentence
        tfidf_matrix = self.vectorizer.fit_transform([sentence])

        # Get the word indices
        word_indices = self.vectorizer.vocabulary_

        # Create a dictionary to store the TF-IDF scores
        tfidf_scores = {}

        # Get the TF-IDF scores of the keywords in the sentence
        sentence_tfidf = tfidf_matrix[0].toarray()[0]
        for word in self.__extract_keywords(sentence):
            tfidf_scores[word] = sentence_tfidf[word_indices[word]]

        return tfidf_scores

    def get_keywords(self, sentence):
        # Get the TF-IDF scores for the single sentence
        tfidf_scores = self.__rank_keywords(sentence)

        # Create a dictionary to store the keywords
        output = {sentence: sorted(tfidf_scores.items(), key=lambda x: x[1], reverse=True)}

        # Get the top 4 keywords in the sentence
        keywords = output[sentence]
        words = [t[0] for t in keywords]

        return words
