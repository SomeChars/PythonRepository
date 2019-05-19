import os
import numpy as np
from keras.models import Model
from keras.layers import Dense, Input
#from keras.utils import np_utils
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
np.random.seed(42)
I = np.random.random((500,2))*4.0 - 2.0
O = [1 if (x/2)**(2/3) + (y/2)**(2/3) <= 1 else 0 for [x,y] in I]
l0 = Input(shape=(2,))
l1 = Dense(6, activation='sigmoid', use_bias=True)(l0)
l2 = Dense(6, activation='sigmoid', use_bias=True)(l1)
l4 = Dense(6, activation='sigmoid', use_bias=True)(l2)
l3 = Dense(1, activation='sigmoid', use_bias=False)(l4)

model = Model(input = l0, output = l3)
model.compile(
    loss='mean_squared_error',
    optimizer='adam',
    metrics=['accuracy']
)
model.fit(
        I, O,
        epochs=10000,
        verbose=False
    )

c = np.r_[-2.5:2.5:0.05]
IO = np.transpose([np.tile(c, len(c)), np.repeat(c, len(c))])

R = model.predict(IO)

for (x, y), z in zip(IO, R):
    plt.scatter(x, y, c='red' if z[0] >= 0.5 else 'green')

plt.show()
