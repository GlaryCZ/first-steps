import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


class LinearRegression:
    def __init__(self, lr=0.001, n_filters=1_000) -> None:
        self.lr = lr
        self.n_filters = n_filters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.iters):
            y_predicted = np.dot(X, self.weights) + self.bias

            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1/n_samples) * np.sum(y_predicted-y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db 

    def predict(self, X):
        y_predicted = np.dot(X, self.weights) + self.bias

loss = nn.MSELoss()
input = torch.randn(3, 5, requires_grad=True)

target = torch.randn(3, 5)

output = loss(input, target)
output.backward()
print(output)




























'''
# f = w * X
# f = 2 * X

X = np.array([1, 2, 3, 4], dtype=np.float32)
Y = np.array([2, 4, 6, 8], dtype=np.float32)

W = 0

# model prediction
def forward(x):
    return W * x

# loss
def loss(y, y_predicted):
    return ((y_predicted-y)**2).mean()

# gradient
# MSE = 1/N * (w*x - y)**2
def gradient(x, y, y_predicted):
    return np.dot(2*x, y_predicted-y).mean()

print(f'Prediction before training: f(5) = {forward(5):.3f}')

# training
'''