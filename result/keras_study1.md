# keras

### 모듈화

모델은 독립적이고 완전히 설정 가능한 모듈을 선형적으로 연결하거나 그래프로 구성한것. 가능한 최소한의 제한으로 함께연결한다. 

->  신경 계층(neural layers), 비용 함수(cost functions), 최적화기(optimizers), 초기화 스킴(initialization schemes), 활성화 함수(activation functions), 정규화 스킴(regularization schemes)은 모두 독립적인 모듈로, 새로운 모델을 생성하기 위해 결합할 수 있다.



데이터 구조는 "모델" 이고, 계층(layer)을 구성하는 데 이용한다. 가장 간단한 유형의 모델은 Sequential 모델이다. 

계층을 선형적으로 쌓은 것 이다. 

```python
from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential()

#.add() 를 이용하면 계층을 손쉽게 쌓을 수 있다. 

model.add(Dense(units=64, input_dim=100))
model.add(Activation('relu'))
model.add(Dense(units=10))
model.add(Activation('softmax'))


#이후 compile을 통해서 학습과정을 구성할 수 있다. 
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
```







