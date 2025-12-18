# Naive Bayes Classifier

## What is it?
**Naive Bayes** classifiers are a family of simple "probabilistic classifiers" based on applying Bayes' theorem with strong (naive) independence assumptions between the features.

## How it works
1.  Calculate Prior Probability for each class.
2.  Calculate Likelihood for each feature given a class (often assuming Gaussian distribution).
3.  Calculate Posterior Probability: `P(Class|Data) = (P(Data|Class) * P(Class)) / P(Data)`.
4.  Select class with highest probability.

## Complexity
- **Time**: **O(N * M)** for training.
- **Space**: **O(C * M)** where C is classes, M is features.

## Example Usage
```bash
python3 naive_bayes.py
```
