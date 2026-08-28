text = "My name is Onkar Gaste. I am learning Python. I am from Rajapur and i am studying b tech degree at DYPCET in kolhapur"

sentences = text.split(".")

for sentence in sentences:
    if sentence.strip():
        print(sentence.strip())