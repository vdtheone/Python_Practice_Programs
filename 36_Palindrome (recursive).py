# Palindrome (recursive)

num = input("Enter number = ")

def palindrome_recursive(s, left=0, right=None):
    if right is None:
        right = len(s) - 1

    # Base case
    if left >= right:
        return True

    # If mismatch
    if s[left] != s[right]:
        return False

    # Recursive call
    return palindrome_recursive(s, left + 1, right - 1)

print("Result =", palindrome_recursive(num))


def palindrome_number(num, rev=0, temp=None):
    if temp is None:
        temp = num

    if temp == 0:
        return num == rev

    return palindrome_number(num, rev * 10 + temp % 10, temp // 10)

num = int(input("Enter number = "))
print("Result =", palindrome_number(num))
