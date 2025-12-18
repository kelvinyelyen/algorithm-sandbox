import math
from collections import Counter

def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1): # Last element is label
        distance += (row1[i] - row2[i])**2
    return math.sqrt(distance)

def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    
    distances.sort(key=lambda tup: tup[1])
    
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

if __name__ == "__main__":
    # [x, y, Class]
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
    
    test_point = [4.0, 3.0] # Should be class 0
    k = 3
    
    print(f"Dataset: {dataset}")
    print(f"Test Point: {test_point}")
    predicted = predict_classification(dataset, test_point, k)
    print(f"Predicted Class: {predicted}")
