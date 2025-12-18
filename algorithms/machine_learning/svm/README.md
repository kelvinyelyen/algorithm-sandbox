# Support Vector Machine (SVM)

## What is it?
**SVM** is a supervised learning model used for classification and regression analysis.

## How it works
1.  Finds a **hyperplane** in an N-dimensional space that distinctly classifies the data points.
2.  Maximizes the **margin** (distance) between the data points of both classes and the hyperplane.
3.  Uses **Kernel Trick** to transform data into higher dimensions if it's not linearly separable.

## Complexity
- **Time**: **O(N^2)** to **O(N^3)** generally.
- **Space**: **O(N^2)** for kernel matrix.

## Example Usage
```bash
python3 svm.py
```
