# Random Forest

## What is it?
**Random Forest** is an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time.

## How it works
1.  **Bagging (Bootstrap Aggregation)**: Create N different subsets of training data (with replacement).
2.  Train N Decision Trees on these subsets.
3.  **Feature Randomness**: At each split, consider only a random subset of features.
4.  **Voting**: For classification, take the majority vote of all trees. For regression, take the average.

## Complexity
- **Time**: **O(N * M * D * T)** where T is number of trees.
- **Space**: **O(T * nodes)**.

## Example Usage
```bash
python3 random_forest.py
```
