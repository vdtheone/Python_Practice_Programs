input_str = "a1b2c3"
output = "abbccc"

result = ""
for i in input_str:
    try:
        num = int(i)
        char = char*num
        result+=char
    except:
        char = i
        
print("result - ",result)