#!/usr/bin/env python

import numpy as np
import model
import feature

races = feature.read_races()
x, y = feature.preprocessing(races)

nnet = model.nnet()
nnet.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'],
)
nnet.summary()

nnet.fit(
    x,
    y,
    batch_size=128,
    epochs=20,
    validation_split=0.1
)


pred = nnet.predict(x)
n_right = 0
for i in range(len(x)):
    if y[i] == np.argmax(pred[i]):
        n_right += 1

print('')
print('正解率：%4.3f%% [%d件]' % (n_right/len(x), len(x)))
