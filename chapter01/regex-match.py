import re

text = "AI is the future for IT operatation."
pattern = r"future"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
    
else:
    print("No Match")
    