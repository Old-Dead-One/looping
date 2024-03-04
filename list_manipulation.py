""" Create three functions that take two lists of numbers of equal size and return 
a new list with the results of multiplying each matching position from the input lists: """


def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    """Multiply each matching position from the input lists using a while loop."""
    result = []
    i = 0

    while i < len(a):
        result.append(a[i] * b[i])
        i += 1
    return result

def list_multiply_for(a: list[int], b: list[int]) -> list[int]:
    """Multiply each matching position from the input lists using a for loop."""
    result = []

    for i in range(len(a)):
        result.append(a[i] * b[i])
    return result

