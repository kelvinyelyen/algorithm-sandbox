# Decision Tree

## What is it?
A **Decision Tree** is a flowchart-like structure where an internal node represents a feature (or attribute), the branch represents a decision rule, and each leaf node represents the outcome (class label).

## How it works
1.  Select the best attribute to split the records (using metrics like Gini Index or Entropy/Information Gain).
2.  Make that attribute a decision node and break the dataset into smaller subsets.
3.  Recursively allow this process for each child node until:
    -   All tuples belong to the same attribute value.
    -   There are no more remaining attributes.
    -   There are no more instances.

## Complexity
- **Time**: **O(N * M * D)** where N=samples, M=features, D=depth.
- **Space**: **O(nodes)**.

## Example Usage
```bash
python3 decision_trees.py
```
