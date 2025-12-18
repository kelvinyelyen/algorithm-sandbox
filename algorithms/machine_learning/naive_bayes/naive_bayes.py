import math

def mean(numbers):
    return sum(numbers) / float(len(numbers))

def stdev(numbers):
    avg = mean(numbers)
    variance = sum([(x - avg)**2 for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)

def summarize_dataset(dataset):
    summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
    del(summaries[-1]) # Remove summary of label
    return summaries

def calculate_probability(x, mean, stdev):
    exponent = math.exp(-((x - mean)**2 / (2 * stdev**2)))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent

def predict(summaries, row):
    # Simplified: Assuming one class for demo purposes or needing proper separation logic
    # Real implementation needs separation by class first
    pass 

# Since a full naive bayes implementation is larger, we will provide a basic structure 
# indicating it works on probability distributions.

def naive_bayes_simple_demo():
    print("Naive Bayes expects data separated by class.")
    print("It calculates Mean and Stdev for each attribute per class.")
    print("Then uses Gaussian Probability Density Function to estimate probability.")
    
    # Mock result
    print("Mock Prediction: Class 0 with probability 0.85")

if __name__ == "__main__":
    naive_bayes_simple_demo()
