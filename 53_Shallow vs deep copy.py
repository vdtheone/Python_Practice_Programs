# Shallow vs deep copy

import copy

original = [1, 2, [3, 4]]

shallow = copy.copy(original)
shallow[2].append(5)

print(original)
print(shallow)

deep = copy.deepcopy(original)
deep[2].append(6)
print(original)
print(deep)