input_str = "abbccc"
output = "a1b2c3"

def test(input_str):
    result = ""
    count = 1
    for i in range(0, len(input_str)-1):
        if input_str[i]==input_str[i+1]:
            count+=1
        else:
            result+=input_str[i]+str(count)
            count = 1
    result+=input_str[-1]+str(count)
    print(result)

test(input_str=input_str)

s = "abbccc"

result = ""
count = 1

for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

print(result)
