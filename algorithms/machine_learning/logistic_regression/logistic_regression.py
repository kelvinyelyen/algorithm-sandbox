import math

def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))

def predict(row, coefficients):
    yhat = coefficients[0]
    for i in range(len(row) - 1):
        yhat += coefficients[i + 1] * row[i]
    return sigmoid(yhat)

def train_weights(train, l_rate, n_epoch):
    coef = [0.0 for i in range(len(train[0]))]
    
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train:
            yhat = predict(row, coef)
            error = row[-1] - yhat
            sum_error += error**2
            coef[0] = coef[0] + l_rate * error * yhat * (1.0 - yhat)
            for i in range(len(row) - 1):
                coef[i + 1] = coef[i + 1] + l_rate * error * yhat * (1.0 - yhat) * row[i]
                
    return coef

if __name__ == "__main__":
    dataset = [
        [2.78, 2.55, 0],
        [1.46, 2.36, 0],
        [3.39, 4.40, 0],
        [1.38, 1.85, 0],
        [3.06, 3.00, 0],
        [7.62, 2.75, 1],
        [5.33, 2.08, 1],
        [6.92, 1.77, 1],
        [8.67, -0.24, 1],
        [7.67, 3.50, 1]
    ]
    
    l_rate = 0.3
    n_epoch = 100
    coef = train_weights(dataset, l_rate, n_epoch)
    print(f"Trained Coefficients: {coef}")
    
    # Predict for training data to verify
    for row in dataset:
        prob = predict(row, coef)
        print(f"Expected={row[-1]}, Predicted={prob:.3f} [{'1' if prob>0.5 else '0'}]")
