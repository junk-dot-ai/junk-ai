import os
import re
import string
import nltk
import numpy as np
import pickle
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS


nltk.download('punkt')
nltk.download('wordnet')


# ------ Preprocess: per email ------

def remove_hyperlink(email):
    return  re.sub(r"http\S+", "", email)

def to_lower(email):
    result = email.lower()
    return result

def remove_number(email):
    result = re.sub(r'\d+', '', email)
    return result

def remove_punctuation(email):
    result = email.translate(str.maketrans(dict.fromkeys(string.punctuation)))
    return result

def remove_whitespace(email):
    result = email.strip()
    return result

def replace_newline(email):
    return email.replace('\n',' ')

def clean_up_pipeline(sentence):
    cleaning_utils = [remove_hyperlink,
                      replace_newline,
                      to_lower,
                      remove_number,
                      remove_punctuation,
                      remove_whitespace]
    for o in cleaning_utils:
        sentence = o(sentence)
    return sentence


# ------ Preprocess: per word ------

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def remove_stop_words(words):
    result = [i for i in words if i not in ENGLISH_STOP_WORDS]
    return result

def word_stemmer(words):
    return [stemmer.stem(o) for o in words]

def word_lemmatizer(words):
    return [lemmatizer.lemmatize(o) for o in words]

def clean_token_pipeline(words):
    cleaning_utils = [remove_stop_words, word_stemmer, word_lemmatizer]
    for o in cleaning_utils:
        words = o(words)
    return words


# ------ Preprocess and Predict ------

def preprocess(text, tokenizer):

    text = clean_up_pipeline(text)
    text = word_tokenize(text)
    text = clean_token_pipeline(text)

    text_features = np.array(tokenizer.texts_to_sequences([text]))
    text_features = pad_sequences(text_features, maxlen=2000)

    return text_features


def predict_junk(text):
    model_load_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "my_model.pb")
    model = load_model(model_load_path)

    tokenizer_open_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tokenizer.pickle")
    with open(tokenizer_open_path, 'rb') as handle:
        tokenizer = pickle.load(handle)

    [[pred]] = model.predict(preprocess(text, tokenizer))
    return pred