def longest_common_substring(X, Y):
    m = len(X)
    n = len(Y)
    
    result = 0
    end_index = 0
    
    # Store LCSuff[i][j] --> Length of Longest Common Suffix
    # of X[0..i-1] and Y[0..j-1]
    LCSuff = [[0 for k in range(n + 1)] for l in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                if LCSuff[i][j] > result:
                    result = LCSuff[i][j]
                    end_index = i - 1
            else:
                LCSuff[i][j] = 0
                
    # If we want the string itself
    if result == 0:
        return ""
    
    return X[end_index - result + 1 : end_index + 1]

if __name__ == "__main__":
    X = "OldSite:GeeksforGeeks.org"
    Y = "NewSite:GeeksQuiz.com"
    print(f"Common Substring: {longest_common_substring(X, Y)}")
    
    A = "ABAB"
    B = "BABA"
    print(f"Common Substring: {longest_common_substring(A, B)}")
