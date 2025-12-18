# Logistic Regression

## What is it?
**Logistic Regression** is a statistical model that in its basic form uses a logistic function to model a binary dependent variable.

## How it works
-   It uses the **Sigmoid function** `1 / (1 + e^-z)` to map predictions to probabilities between 0 and 1.
-   Weights are updated using Gradient Descent to minimize the Log Loss (Cross-Entropy Loss).

## Complexity
- **Time**: **O(N * M * Epochs)**.
- **Space**: **O(M)** for weights.

## Example Usage
```bash
python3 logistic_regression.py
```
