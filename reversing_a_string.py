# Write three functions that take a string s and return a reversed copy of it.

# reverse_while: Implements the reversing using a while loop.
# reverse_for: Implements the reversing using a for loop (iterating over the string using indices (using range)).
# reverse_foreach: Implements the reversing using a foreach loop (iterating over the actual characters in the string, not using range)

def reverse_while(s: str) -> str:
    result = ""
    i = len(s) - 1

    while i >= 0:
        result += s[i]
        i -= 1
    return result

def reverse_for(s: str) -> str:
    result = ""

    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result


# I dont really understand this one, I needed help from the solution
def reverse_foreach(s: str) -> str:
    result = ""

    for char in s:
        result = char + result
    return result

s = "The quick Brown fox jumps over the lazy dog."

print("Reverse While")
print(reverse_while(s))
print()

print("Reverse For")
print(reverse_for(s))
print()

print("Reverse Foreach")
print(reverse_foreach(s))
