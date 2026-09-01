import re

text = "The bif fat wedding"
pattern = r"fat"


search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Patter not found")
    