import numpy as np

def relu(x):
    return np.maximum(0, x)

def relu2deriv(output):
    return output > 0

def act(x):
    return x+1

input = np.array([100])
weight0 = 2*np.random.random((1,1)) - 1
weight1 = 2*np.random.random((1,1)) - 1
weight2_0 = 2*np.random.random((1,1)) - 1
weight2_1 = 2*np.random.random((1,1)) - 1
output = np.array([10])

alpha = 0.1
for i in range(20):
    x = 0
    while True:
        layer_0 = input
        layer_1 = layer_0.dot(weight0)
        layer_2 = layer_1.dot(weight1)
        input = layer_2.dot(weight2_0)
        x += 1
        if x == 10:
            layer_3 = layer_2.dot(weight2_1)
            print(layer_3)
            break

print("1")