s = input("Enter a string: ")
upper = sum(1 for ch in s if ch.isupper())
lower = sum(1 for ch in s if ch.islower())

print(f"Uppercase: {upper}, Lowercase: {lower}")