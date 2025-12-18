# Simplified Decision Tree (CART) - Gini Index

def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    for index in range(len(dataset[0]) - 1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index':b_index, 'value':b_value, 'groups':b_groups}

def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

def gini_index(groups, classes):
    # count all samples at split point
    n_instances = float(sum([len(group) for group in groups]))
    gini = 0.0
    for group in groups:
        size = float(len(group))
        if size == 0:
            continue
        score = 0.0
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        gini += (1.0 - score) * (size / n_instances)
    return gini

# ... Rest of recursive splitting would go here. 
# For size reasons, we demonstrate the split finding.

if __name__ == "__main__":
    dataset = [[2.77, 2.55, 0],
               [1.46, 2.36, 0],
               [3.39, 4.40, 0],
               [1.38, 1.85, 0],
               [3.06, 3.00, 0],
               [7.62, 2.75, 1],
               [5.33, 2.08, 1],
               [6.92, 1.77, 1],
               [8.67, -0.24, 1],
               [7.67, 3.50, 1]]
               
    split = get_split(dataset)
    print(f"Best Split: [Column {split['index']}] < {split['value']:.3f} (Gini={split['index']:.3f})")
