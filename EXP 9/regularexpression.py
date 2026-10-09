import re
text = "My phone number is 9420776791"
pattern = r"\d+"
result = re.findall(pattern, text)
print(result)


    
