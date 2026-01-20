# Group anagrams

"""Given a list of strings, group the words that are anagrams of each other."""

input_list_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = [
  ["eat", "tea", "ate"],
  ["tan", "nat"],
  ["bat"]
]

input_list_2 = ["listen", "silent", "enlist", "hello", "ohlle"]
output = [
  ["listen", "silent", "enlist"],
  ["hello", "ohlle"]
]

def group_anagram(input_list):
    result_dict = {}

    for i in input_list:
        sorted_str = "".join(sorted(i))
        if sorted_str in result_dict:
            result_dict[sorted_str].append(i)
        else:
            result_dict[sorted_str] = [i]

    return [i for i in result_dict.values()]

print("result - ", group_anagram(input_list_1))
print("result - ", group_anagram(input_list_2))


from collections import defaultdict

# def group_anagram(words):
#     groups = defaultdict(list)

#     for word in words:
#         key = tuple(sorted(word))
#         groups[key].append(word)
#     print('groups: ', groups)

#     return list(groups.values())

def group_anagram(words):
    groups = defaultdict(list)

    for word in words:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(word)

    return list(groups.values())


print("result - ", group_anagram(input_list_2))
