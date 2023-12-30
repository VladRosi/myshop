
words = ["abc", "aabc", "bc"]
l = len(words)
flat_words = [char for word in words for char in word]
from collections import Counter
counter = Counter(flat_words)
for num in counter.values():
  if num % l != 0:
    return False

return True
print(counter.values())

