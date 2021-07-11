
# coding: utf-8

# In[145]:



import keras
import pandas as pd
from keras.layers import Embedding
import MeCab


# In[146]:


from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np


# In[147]:


import os


# In[148]:


Data=pd.read_excel('C:\\Users\\qri\\model\\depressionO.xlsx', header=None)


# In[149]:


Data2=pd.read_excel('C:\\Users\\qri\\model\\depressionX.xlsx', header=None)


# In[150]:


texts_temp =list(Data[0])+list(Data2[0])


# In[151]:


labels = []
# 우울 0 우울아님 1
for i in range(len(Data)):
    labels.append(0)
for i in range(len(Data2)):
    labels.append(1)


# In[152]:


len(labels)


# In[153]:


m=MeCab.Tagger()


# In[154]:


texts=[]
for i in range(len(texts_temp)):
    texts.append([x.split("\t")[0] for x in m.parse(texts_temp[i]).split("\n") if not x =="EOS" and not x==""])


# In[155]:


len(texts)


# In[156]:


maxlen = 10  # 10개 단어 이후는 버립니다
training_samples = 1800  # 훈련 샘플은 1800개입니다
validation_samples = 500  # 검증 샘플은 500개입니다
max_words = 3000  # 데이터셋에서 가장 빈도 높은 3,000개의 단어만 사용합니다

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

word_index = tokenizer.word_index


# In[157]:


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


# In[174]:


data.shape


# In[163]:


len(x_train[10])


# In[121]:


glove_dir = ' -- '

embeddings_index = {}
f = open(os.path.join(glove_dir, 'glove.txt'), encoding="utf8")
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('%s개의 단어 벡터를 찾았습니다.' % len(embeddings_index))


# In[122]:


embedding_dim = 100
embedding_matrix = np.zeros((max_words, embedding_dim))
for word, i in word_index.items():
    embedding_vector = embeddings_index.get(word)
    if i < max_words:
        if embedding_vector is not None:
            # 임베딩 인덱스에 없는 단어는 모두 0이 됩니다.
            embedding_matrix[i] = embedding_vector


# In[123]:



from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
from keras.layers import GRU

model = Sequential()
model.add(Embedding(max_words, embedding_dim, input_length=maxlen))
model.add(GRU(32))
model.add(Dense(1, activation='relu'))
model.summary()


# In[124]:



model.layers[0].set_weights([embedding_matrix])
model.layers[0].trainable = False


# In[125]:


model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['acc'])
history = model.fit(x_train, y_train,
                    epochs=100,
                    batch_size=32,
                    validation_data=(x_val, y_val))


# In[126]:


##### 그래프 #####

import matplotlib.pyplot as plt


# In[127]:


acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('GRU Model : Training and validation accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('GRU Model : Training and validation loss')
plt.legend()

plt.show()

##### 그래프 #####
# In[133]:


# 정확도는 90프로 정도 나옴
#GRU(16) 인 경우 89 & 변화폭이 큼
#GRU(64) 인 경우 87~90 변화폭이 큼

# In[134]:


# 실제 테스트 해보기 # 우울이면 0 우울아니면 1 출력


# In[192]:


# 중첩 리스트 하나의 리스트로 변환하는 함수
def flatten(l): 
    flatList = [] 
    for elem in l: 
        if type(elem) == list: 
            for e in elem: 
                flatList.append(e) 
        else: 
            flatList.append(elem) 
    return flatList


# In[206]:


test_sentence="부모님과 산책을 다녀온 날이다. 날씨가 매우 좋아서 기분이 상쾌하였다."


# In[207]:


test_sentence=[x.split("\t")[0] for x in m.parse(test_sentence).split("\n") if not x =="EOS" and not x==""]


# In[208]:


test_sentence2="비가 오늘 날이다. 기분이 꿀꿀하다. 술이 생각난다."


# In[209]:


test_sentence2=[x.split("\t")[0] for x in m.parse(test_sentence2).split("\n") if not x =="EOS" and not x==""]


# In[210]:


test=[]
test.append(test_sentence)
test.append(test_sentence2)


# In[213]:


model.predict_classes(pad_sequences((tokenizer.texts_to_sequences(test)),maxlen=maxlen)) # 출력결과 정답!

