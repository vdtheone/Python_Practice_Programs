# Flatten nested dictionary

"""
Flatten Nested Dictionary

Problem Statement:

Given a dictionary that may contain nested dictionaries, write a program to flatten it.
The flattened dictionary should use dot (.) notation to represent nested keys.

Input 1
data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3
        }
    }
}

Output 1
{
    "a": 1,
    "b.c": 2,
    "b.d.e": 3
}

Input 2
data = {
    "x": {
        "y": 10
    },
    "z": 5
}

Output 2
{
    "x.y": 10,
    "z": 5
}
"""

data_1 = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3
        }
    }
}

data_2 = {
    "x": {
        "y": 10
    },
    "z": 5
}

def flatten_nested_dict(data, parent_key="", sep="."):
    flat_dict = {}
    for key, val in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        
        if isinstance(val, dict):
            flat_dict.update(flatten_nested_dict(val, new_key, sep))
        else:
            flat_dict[new_key] = val
    return flat_dict
        
print("Result = ", flatten_nested_dict(data_1))
print("Result = ", flatten_nested_dict(data_2))
