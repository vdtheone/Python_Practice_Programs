# Find all pairs with sum = K

data = [2,4,5,7,8,3,9]
k = 12

def find_all_pairs(data):
    seen = set()
    pairs = []
    for i in data:
        dif = k - i
        if dif in seen:
            pairs.append((dif, i))
        seen.add(i)
    return pairs
print(find_all_pairs(data))