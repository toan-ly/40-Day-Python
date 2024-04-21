import pandas as pd
import wandb
import numpy as np

dataset = pd.read_csv('advertising.csv')
dataset.head()

def min_max_scale(X):
    return (X - np.min(X)) / (np.max(X) - np.min(X))
    
def predict(x, w, b):
    return x @ w + b

def gradient(y_hat, y, x):
    dw = 2 * x * (y_hat - y)
    db = 2 * (y_hat - y)
    return (dw, db)

def update_weight(w, b, lr, dw, db):
    w -= lr * dw
    b -= lr * db
    return (w, b)

b = 1
w = np.zeros(3)
lr = 0.01
epochs = 1000

# init project wandb
wandb.init(
   # Set the project where this run will be logged 
   project='demo-linear-regression',
   config={
       'learning_rate': lr,
       'epochs': epochs,
   },
)

wandb.run.log({'Dataset': wandb.Table(dataframe=dataset)})

X_train = dataset[['TV', 'Radio', 'Newspaper']]
X_train = min_max_scale(X_train)
y_train = dataset['Sales']

n = len(X_train)
losses = []

for epoch in range(epochs):
    for i in range(n):
        x = X_train.iloc[i].values
        y = y_train[i]
        
        y_hat = predict(x, w, b)
        
        loss = (y_hat - y)**2 / 2.0
       
        wandb.log({'loss': loss})

        (dw, db) = gradient(y_hat, y, x)
        (w, b) = update_weight(w, b, lr, dw, db)
        
wandb.finish()