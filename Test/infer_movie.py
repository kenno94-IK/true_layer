#!/usr/bin/python3
import sys
import nltk
import pickle
import os
import numpy as np
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
tf.get_logger().setLevel('FATAL')
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.python.keras.backend import reset_uids
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

args = sys.argv[1].split(' ')

try:
    title_index = args.index('--title')

except:
    print('--title tag not provided')
    exit()

try:
    description_index = args.index('--description')

except:
    print('--description tag not provided')
    exit()

title = ' '.join(args[1:description_index]).strip(' ')
description = ' '.join(args[description_index+1:]).strip(' ')

input = title + ' keywords ' + description

data = [[input]]

input = pd.DataFrame(data, columns=['Input'])

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [lemmatizer.lemmatize(token) for token in text.split(" ")]
    text = [word for word in text if not word in stop_words]
    text = " ".join(text)
    return text

input['Input'] = input.Input.apply(lambda x: clean_text(x))

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

encoded_docs = tokenizer.texts_to_sequences(input['Input'])

X = pad_sequences(encoded_docs, maxlen=193, padding='post')

model = tf.keras.models.load_model("movie_genre_model")

prediction = model.predict(X)

argmax = np.argmax(prediction)
argmax = np.array([argmax])

with open('Label_encoder.pickle', 'rb') as handle:
    le = pickle.load(handle)

result = le.inverse_transform(argmax)

print(result[0])