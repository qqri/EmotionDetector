import keras
import pandas as pd
from keras.layers import Embedding
import MeCab
import warnings
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
from keras.layers import GRU
import os
import sys

from model.model_LSTM import tokenizer

warnings.filterwarnings('ignore')
sys.path.append('ml')


class MLModel():

    def __init__(self):
        self.n_frame_seconds = 3
        self.duration_load_audio = 6

    # coding: utf-8
    Data = pd.read_excel('\\', header=None)
    Data2 = pd.read_excel('C:\\Users\\qri\\model\\depressionX.xlsx', header=None)
    texts_temp = list(Data[0]) + list(Data2[0])

    labels = []
    # 부정 0 긍정 1
    for i in range(len(Data)):
        labels.append(0)
    for i in range(len(Data2)):
        labels.append(1)

    len(labels)

    m = MeCab.Tagger()

    texts = []
    for i in range(len(texts_temp)):
        texts.append([x.split("\t")[0] for x in m.parse(texts_temp[i]).split("\n") if not x == "EOS" and not x == ""])

    len(texts)

    maxlen = 10  # 10개 단어 이후는 버립니다
    training_samples = 1800  # 훈련 샘플은 2000개입니다
    validation_samples = 500  # 검증 샘플은 500개입니다
    max_words = 3000  # 데이터셋에서 가장 빈도 높은 3,000개의 단어만 사용합니다

    tokenizer = Tokenizer(num_words=max_words)
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)

    word_index = tokenizer.word_index

    print('%s개의 고유한 토큰을 찾았습니다.' % len(word_index))

    data = pad_sequences(sequences, maxlen=maxlen)

    labels = np.asarray(labels)
    print('데이터 텐서의 크기:', data.shape)
    print('레이블 텐서의 크기:', labels.shape)

    indices = np.arange(data.shape[0])
    np.random.shuffle(indices)
    data = data[indices]
    labels = labels[indices]

    x_train = data[:training_samples]
    y_train = labels[:training_samples]
    x_val = data[training_samples: training_samples + validation_samples]
    y_val = labels[training_samples: training_samples + validation_samples]

    data.shape

    len(x_train[10])

    glove_dir = '\\'

    embeddings_index = {}
    f = open(os.path.join(glove_dir, '\\'), encoding="utf8")
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs
    f.close()

    print('%s개의 단어 벡터를 찾았습니다.' % len(embeddings_index))

    embedding_dim = 100
    embedding_matrix = np.zeros((max_words, embedding_dim))
    for word, i in word_index.items():
        embedding_vector = embeddings_index.get(word)
        if i < max_words:
            if embedding_vector is not None:
                # 임베딩 인덱스에 없는 단어는 모두 0이 됩니다.
                embedding_matrix[i] = embedding_vector

    model = Sequential()
    model.add(Embedding(max_words, embedding_dim, input_length=maxlen))
    model.add(GRU(32))
    model.add(Dense(1, activation='relu'))

    model.summary()
    model.layers[0].set_weights([embedding_matrix])
    model.layers[0].trainable = False

    model.compile(optimizer='rmsprop',
                  loss='binary_crossentropy',
                  metrics=['acc'])
    history = model.fit(x_train, y_train,
                        epochs=100,
                        batch_size=32,
                        validation_data=(x_val, y_val))


    def flatten(l):
        flatList = []
        for elem in l:
            if type(elem) == list:
                for e in elem:
                    flatList.append(e)
            else:
                flatList.append(elem)
        return flatList

    def predict(sentence):
            test[]
            sentence = [x.split("\t")[0] for x in m.parse(sentence).split("\n") if
                          not x == "EOS" and not x == ""]
            model.predict_classes(pad_sequences((tokenizer.texts_to_sequences(test)), maxlen=maxlen))  # 출력결과 정답!


