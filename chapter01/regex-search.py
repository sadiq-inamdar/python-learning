import re

text = "The furure is AI"
pattern = r"future"

search = re.search(pattern, text)
if search:
    print("Pattern found:", serach.group())

else:
    print("Pattern not found")
    