import re

text = "aaadaa"
pattern = "aa"

# Using finditer to find all overlapping or non-overlapping matches
# Note: Standard search finds non-overlapping matches
for match in re.finditer(pattern, text):
    print(f"Match '{match.group()}' at indices: {match.start()}, {match.end()}")   