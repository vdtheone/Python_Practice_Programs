# Rearrange array (positives and negatives)

def rearrange_array(arr):
    # Separate positive and negative numbers
    positives = [x for x in arr if x >= 0]
    negatives = [x for x in arr if x < 0]

    # Interleave positives and negatives
    result = []
    i, j = 0, 0
    while i < len(positives) and j < len(negatives):
        result.append(positives[i])
        result.append(negatives[j])
        i += 1
        j += 1

    # Append remaining positives or negatives
    result.extend(positives[i:])
    result.extend(negatives[j:])

    return result

# Example usage
arr = [1, -2, 3, -4, 5, -6]
rearranged = rearrange_array(arr)
print(rearranged)  # Output: [1, -2, 3, -4, 5, -6]
