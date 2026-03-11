from lorem_text import lorem

chars = lorem.words(20000)

with open("lorem.txt", "w") as f:
    f.write(chars)

print(f"Generated lorem text with {len(chars)} characters and saved to 'lorem.txt'")