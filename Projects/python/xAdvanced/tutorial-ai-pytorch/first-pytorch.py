import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# 0) setup variablles
X_numpy, y_numpy = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=1)
X = torch.from_numpy(X_numpy.astype(np.float32))
y = torch.from_numpy(y_numpy.astype(np.float32))

print(X)
print(y.view(y.shape[0], 1))

n_samples, n_features = X.shape

# 1) model
input_size = n_features
output_size = 1

model = nn.Linear(input_size, output_size)

# 2) loss and optimizer
learning_rate = 0.1
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

# 3) training loop
num_epochs = 100
for epoch in range(num_epochs):
    # forward pass and loss
    y_predicted = model(X)
    loss = criterion(y_predicted, y)
    # backword pass
    loss.backward()

    # update
    optimizer.step()
    optimizer.zero_grad()
    if (epoch+1) % 10 == 0:
        print(f"epoch: {epoch+1}, loss: {loss.item():.4}")

# plot
predicted = model(X).detach().numpy()
plt.plot(X_numpy, y_numpy, 'ro')
plt.plot(X_numpy, predicted, 'b')
plt.show()













'''
w = torch.tensor(1.0, requires_grad=True)
x = torch.tensor(1.0)
y = torch.tensor(2.0)

# forward pass and compute loss
s1 = x * w
loss = (s1 - y)**2
print(loss)

# backword pass
loss.backward()
print(w.grad)

### update weights
### next forward and backword
'''