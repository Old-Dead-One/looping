"""Write three functions that take two strings, target and c (which will be a single character). The functions will count how many times c appears in target, returning the result.

char_count_while: Implements the character counting using a while loop.
char_count_for: Implements the character counting using a for loop (iterating over the string using indices (using range)).
char_count_foreach: Implements the character counting using a foreach loop (iterating over each character instead of using range)."""


def char_count_while(target: str, c: str) -> int:
    count = 0
    i = 0

    while i < len(target):
        if target[i] == c:
            count += 1
        i += 1
    return count

def char_count_for(target: str, c: str) -> int:
    count = 0

    for i in range(len(target)):
        if target[i] == c:
            count += 1
    return count

def char_count_foreach(target: str, c: str) -> int:
    count = 0

    for char in target:
        if char == c:
            count += 1
    return count


s = "The quick Brown fox jumps over the lazy dog."
c = "l"

print("Count While")
print(char_count_while(s, c))
print()

print("Count For")
print(char_count_for(s, c))
print()

print("Count Foreach")
print(char_count_foreach(s, c))
print()
