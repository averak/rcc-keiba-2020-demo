#!/usr/bin/env python

import numpy as np
from sklearn.model_selection import train_test_split
import model
import feature

# 教師データを用意 =================
races = feature.read_races()
x, y = feature.preprocessing(races)

# 学習用と検証用に分割
x_train, x_test = train_test_split(x, test_size=0.2, random_state=1)
y_train, y_test = train_test_split(y, test_size=0.2, random_state=1)


# 学習 =============================
nnet = model.nnet(x_train.shape[1:])
nnet.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'],
)
nnet.summary()

nnet.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=20,
    validation_data=(x_test, y_test),
)


# 評価 =============================
pred = nnet.predict(x_test)
cnt_accuracy = 0
for i in range(len(x_test)):
    if y_test[i] == np.argmax(pred[i]):
        cnt_accuracy += 1

print('')
print('正解率：%5.3f%% [全%d件]' % (100 * cnt_accuracy / len(x_test), len(x_test)))
