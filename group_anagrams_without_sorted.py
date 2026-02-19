# Group anagrams without using built-in sorted() function.

def custom_sorted(word):
    arr = list(word)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return "".join(arr)


def group_anagrams(words):
    result_dict = {}
    
    for i in words:
        sorted_str = "".join(custom_sorted(i))
        if sorted_str in result_dict:
            result_dict[sorted_str].append(i)
        else:
            result_dict[sorted_str] = [i]
            
    return [i for i in result_dict.values()]


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
words = ["listen", "silent", "enlist", "hello", "ohlle"]
print(group_anagrams(words))