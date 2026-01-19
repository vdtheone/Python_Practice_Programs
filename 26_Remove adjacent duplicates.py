# Remove adjacent duplicates

input_str = "abbaca"
output = "ca"


def remove_adjecent_duplicate(input_str):
    stack = []
    for ch in input_str:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)
        

print("result - ", remove_adjecent_duplicate(input_str))