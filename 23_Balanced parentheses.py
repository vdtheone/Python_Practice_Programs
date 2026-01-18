# Balanced parentheses

"""Problem Statement:
Given a string containing only the characters '(', ')', '{', '}', '[', and ']', determine whether the string is balanced.

A string is balanced if:

Every opening bracket has a matching closing bracket

Brackets are closed in the correct order"""

input_str_1 = "{[()]}"
output = True


input_str_2 = "{[(])}"
output = False

input_str_3 = "{[(})]}"
input_str_4 = "{[("

def balanced_parentheses(input_str):
    correct_para = {"}":"{", "]":"[", ")":"("}
    stack : list = []
    for i in input_str:
        if i in correct_para.values():
            stack.append(i)
        else:
            if not stack:
                return False
            
            if stack.pop()!= correct_para[i]:
                return False

    return len(stack)==0    

print("result = ", balanced_parentheses(input_str_1))
print("result = ", balanced_parentheses(input_str_2))
print("result = ", balanced_parentheses(input_str_3))
print("result = ", balanced_parentheses(input_str_4))




