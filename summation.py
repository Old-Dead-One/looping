n = 10
n1 = 5


def summation_while(n):
    """Summation of the first n numbers using a while loop."""
    total = 0

    while n > 0:
        total += n
        n -= 1 
    return total

print(summation_while(n))

def summation_for(n1):
    """Summation of the first n numbers using a for loop."""
    total = 0

    for i in range(1, n1+1):
        total += i
    return total

print(summation_for(n1))
