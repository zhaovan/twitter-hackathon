import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
import tokenizer

MAX_LENGTH = None
X_train_text = None
X_train = None
y_train = None
X_test_text = None
X_test = None
y_test = None


def textProcessing():
    df = pd.read_csv("dataset.csv")
    df.dropna(inplace=True)
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(df['text'])
    df['text'] = tokenizer.texts_to_sequences(df['text'])
    X_lens = [len(x) for x in df['text'].values]
    X_lens = np.array(X_lens)
    mean = np.mean(X_lens)
    std = np.std(X_lens)
    MAX_LENGTH = (std*2) + mean
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


def model():
    text_input = tf.keras.layers.Input(
        shape=(MAX_LENGTH,), name='article_body_input')
    text_embed = tf.keras.layers.Embedding(tokenizer.index_word + 1, 50, input_length=MAX_LENGTH,
                                           name='article_body_embedding')(text_input)
    text_conv = tf.keras.layers.Conv1D(
        256, 10, name='article_body_conv')(text_embed)
    text_pool = tf.keras.layers.GlobalMaxPool1D(
        name='article_body_pooling')(text_conv)
    vector_input = tf.keras.layers.Input(shape=(21,), name='twitter_input')
    concat = tf.keras.layers.concatenate([text_pool, vector_input])
    dense_100 = tf.keras.layers.Dense(100, activation='relu')(concat)
    dense_50 = tf.keras.layers.Dense(50, activation='relu')(dense_100)
    out_layer = tf.keras.layers.Dense(1, activation='sigmoid')(dense_50)
    model = tf.keras.models.Model(
        inputs=[text_input, vector_input], outputs=out_layer)
    model.summary()
    model.compile(optimizer=tf.keras.optimizers.Adam(0.0005),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])


def modelTrain():
    callback = tf.keras.callbacks.EarlyStopping(monitor='val_acc',
                                                patience=5,
                                                mode='max',
                                                restore_best_weights=True)
    history = model.fit([X_train_text, X_train],
                        y_train,
                        epochs=100,
                        batch_size=128,
                        validation_data=(
                            [X_test_text, X_test],
                            y_test
    ),
        callbacks=[callback])


textProcessing()
model()
modelTrain()
