class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(capacity, items):
    """
    capacity: max weight knapsack can carry
    items: list of Item objects
    """
    # Sort items by value/weight ratio in descending order
    items.sort(key=lambda x: (x.value / x.weight), reverse=True)

    total_value = 0.0
    current_weight = 0

    for item in items:
        if current_weight + item.weight <= capacity:
            current_weight += item.weight
            total_value += item.value
            print(f"Took whole item: Value {item.value}, Weight {item.weight}")
        else:
            remain = capacity - current_weight
            fraction = remain / item.weight
            total_value += item.value * fraction
            current_weight += remain
            print(f"Took fraction {fraction:.2f} of item: Value {item.value}, Weight {item.weight}")
            break
            
    return total_value

if __name__ == "__main__":
    capacity = 50
    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]
    
    max_val = fractional_knapsack(capacity, items)
    print(f"Maximum value in Knapsack: {max_val}")
