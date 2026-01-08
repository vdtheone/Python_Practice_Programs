import re


input_str = "a1b2c3"
output = "abbccc"

result = ""
for i in input_str:
    if i.isdigit():
        num = int(i)
        result+=char*num
    else:
        char = i
        
print("result - ",result)

result = "".join(ch * int(n) for ch, n in re.findall(r'([a-zA-Z])(\d)', input_str))
print(re.findall(r'([a-zA-Z])(\d)', input_str))