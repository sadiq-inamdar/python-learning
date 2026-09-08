import re

text = "apple,banaba,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)