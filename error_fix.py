with open("requirements.txt", "rb") as f:
    content = f.read().decode("utf-16")  # Change to utf-16 if needed

with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write(content)
