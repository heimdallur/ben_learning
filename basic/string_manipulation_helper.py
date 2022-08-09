# Test 3

# This is how I did it

import json


def counter(words: str) -> object:
    char_counts: object = {}
    for c in words.replace(' ', '').lower():
        if c in char_counts:
            char_counts[c] = char_counts[c] + 1
        else:
            char_counts[c] = 1
    return char_counts


a: str = 'Hello my name is Ben and I like ben10 figures even snails'

res: object = json.dumps(counter(a), indent=4)

print(res)