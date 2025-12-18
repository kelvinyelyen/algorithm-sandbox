def mean(values):
    return sum(values) / float(len(values))

def variance(values, mean):
    return sum([(x - mean)**2 for x in values])

def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    x_mean, y_mean = mean(x), mean(y)
    b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return [b0, b1]

def simple_linear_regression(train, test):
    predictions = list()
    b0, b1 = coefficients(train)
    for row in test:
        yhat = b0 + b1 * row[0]
        predictions.append(yhat)
    return predictions

if __name__ == "__main__":
    # Dataset: [Input, Output]
    dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
    test = [[1.5], [3.5]] # predicting for inputs 1.5 and 3.5
    
    print(f"Training Data: {dataset}")
    b0, b1 = coefficients(dataset)
    print(f"Coefficients: B0={b0:.3f}, B1={b1:.3f}")
    
    predictions = simple_linear_regression(dataset, test)
    print(f"Predictions for {test}: {predictions}")
