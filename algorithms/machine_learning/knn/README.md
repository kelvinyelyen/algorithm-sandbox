# K-Nearest Neighbors (KNN)

## What is it?
**KNN** is a non-parametric, lazy learning algorithm used for classification and regression. It classifies a data point based on how its neighbors are classified.

## How it works
1.  Select the number K of the neighbors.
2.  Calculate the Euclidean distance of K number of neighbors.
3.  Take the K nearest neighbors as per the calculated Euclidean distance.
4.  Among these k neighbors, count the number of the data points in each category.
5.  Assign the new data point to that category for which the number of neighbors is maximum.

## Complexity
- **Time**: **O(N * M)** for prediction (where N is samples, M is dimensions).
- **Space**: **O(N * M)** to store data.

## Example Usage
```bash
python3 knn.py
```
