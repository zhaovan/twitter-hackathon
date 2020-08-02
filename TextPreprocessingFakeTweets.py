import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score


def textProcessing():
    df = pd.read_csv("dataset.csv")
    df.dropna(inplace=True)
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(df['text'])
    df['text'] = tokenizer.texts_to_sequences(df['text'])
    #X_lens = [len(x) for x in df['text'].values]
    #X_lens = np.array(X_lens)
    #mean = np.mean(X_lens)
    #std = np.std(X_lens)
    MAX_LENGTH = 2986
    status = df.pop('status')
    X_train, X_test, y_train, y_test = train_test_split(df, status)
    X_train_text = X_train.pop('text')
    X_test_text = X_test.pop('text')
    X_train_text = tf.keras.preprocessing.sequence.pad_sequences(X_train_text,
                                                                 maxlen=MAX_LENGTH,
                                                                 padding='post',
                                                                 truncating='post')
    X_test_text = tf.keras.preprocessing.sequence.pad_sequences(X_test_text,
                                                                maxlen=MAX_LENGTH,
                                                                padding='post',
                                                                truncating='post')