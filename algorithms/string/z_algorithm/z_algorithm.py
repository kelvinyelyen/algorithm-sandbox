def get_z_array(string, z):
    """
    Fills Z array for given string.
    """
    n = len(string)
    l, r, k = 0, 0, 0
    for i in range(1, n):
        # If i > r nothing matches so we will calculate.
        # Z[i] using naive way.
        if i > r:
            l, r = i, i
            while r < n and string[r - l] == string[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            # k odpowies to number of characters in [0, r-l]
            k = i - l
            # if z[k] is less than remaining interval
            # then z[i] will be equal to z[k].
            # For example, str = "ababab", i = 3, r = 5, l = 2
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                # else start from right and check manually
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1

def z_algorithm(text, pattern):
    """
    Z Algorithm for pattern searching.
    """
    concat = pattern + "$" + text
    l = len(concat)
    z = [0] * l
    get_z_array(concat, z)
    
    result_indices = []
    
    # now looping through Z array for matching condition
    for i in range(l):
        # if Z[i] (matched region) is equal to pattern
        # length we got the pattern
        if z[i] == len(pattern):
            # Index in text is i - (pattern_len + 1)
            result_indices.append(i - len(pattern) - 1)
            
    return result_indices

if __name__ == "__main__":
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    
    matches = z_algorithm(text, pattern)
    print(f"Pattern found at indices: {matches}")
    
    text2 = "ABABDABACDABABCABAB"
    pattern2 = "ABABCABAB"
    print(f"\nText: {text2}")
    print(f"Pattern: {pattern2}")
    matches2 = z_algorithm(text2, pattern2)
    print(f"Pattern found at indices: {matches2}")
