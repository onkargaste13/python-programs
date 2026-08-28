text = "My name is Onkar Gaste and I am learning Python"

stop_words = ["is", "and", "I", "am"]

words = text.split()

filtered_words = []

for word in words:
       if word not in stop_words:  filtered_words.append(word)

print(filtered_words)