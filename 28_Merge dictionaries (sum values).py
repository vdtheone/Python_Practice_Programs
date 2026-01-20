# Merge dictionaries (sum values)
"""
Given two dictionaries with common keys, merge them into a single dictionary.
If a key exists in both dictionaries, sum their values.
"""

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}


output = {"a": 10, "b": 25, "c": 45, "d": 25}

dict1 = {"x": 1, "y": 2}
dict2 = {"y": 3, "z": 4}

output = {"x": 1, "y": 5, "z": 4}


def merge_dict(dict_1:dict, dict_2):
    new_dict={}
    new_dict.update(dict_1)
    new_dict.update(dict_2)
    for i in dict_1:
        if i in dict_2:
            new_dict[i] = dict_1[i] + dict_2[i]
        
    return new_dict

print("result - ", merge_dict(dict1, dict2))    


# Optimized Approach #1 (Single Loop)
def merge_dict(d1, d2):
    result = {}

    for key in d1.keys() | d2.keys():
        result[key] = d1.get(key, 0) + d2.get(key, 0)

    return result

print("result - ", merge_dict(dict1, dict2))    



# Optimized Approach #2 (collections.Counter) BEST
from collections import Counter

def merge_dict(d1, d2):
    print('Counter(d1): ', Counter(d1))
    return dict(Counter(d1) + Counter(d2))

print("result - ", merge_dict(dict1, dict2))    
