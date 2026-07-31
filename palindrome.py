s = input("Enter a string: ")
reversed_s = ""

for char in s:
    reversed_s = char + reversed_s

if s == reversed_s:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")