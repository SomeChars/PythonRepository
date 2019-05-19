import numpy as np
from keras.models import Model
from keras.layers import Dense, Input
import matplotlib.pyplot as plt

np.random.seed(42)
Rand = np.random.random((150, 2)) * 4.0 - 2.0

Pin = np.array([[0.99*np.cos(t*np.pi/24),0.99*np.sin(t*np.pi/24)] for t in range(42)])
Pon = np.array([[np.cos(t*np.pi/24),np.sin(t*np.pi/24)] for t in range(42)])
Pout = np.array([[1.01*np.cos(t*np.pi/24),1.01*np.sin(t*np.pi/24)] for t in range(42)])

X = np.concatenate((Rand,Pin,Pon,Pout),axis=0)



Y = [
    1 if x ** 2 + y ** 2 <= 1 else 0
    for [x, y] in X
]
l0 = Input(shape=(2,))
l1 = Dense(6, activation='sigmoid', use_bias=True)(l0)
l2 = Dense(1, activation='sigmoid', use_bias=False)(l1)

model = Model(input=l0, output=l2)

model.compile(
    loss='mean_squared_error',
    optimizer='adam',
    metrics=['accuracy']
)
model.fit(
        X, Y,
        epochs=20000,
        verbose=False
    )
plt.axis('equal')

c = np.r_[-2:2:0.05]

# https://stackoverflow.com/a/11144716/539470 =)
XY = np.transpose([np.tile(c, len(c)), np.repeat(c, len(c))])

Z = model.predict(XY)

for (x, y), z in zip(XY, Z):
    plt.scatter(x, y, c='red' if z[0] >= 0.5 else 'green')

plt.show()