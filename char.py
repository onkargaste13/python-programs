s = input("Enter a string: ")
v = c = d = sp = sc = 0

for ch in s:
    if ch.lower() in "aeiou": v += 1
    elif ch.isalpha(): c += 1
    elif ch.isdigit(): d += 1
    elif ch.isspace(): sp += 1
    else: sc += 1

print(f"Vowels: {v}, Consonants: {c}, Digits: {d}, Spaces: {sp}, Special: {sc}")