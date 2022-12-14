#1. The Big Result
# Write an add_mult function that requires three parameters / arguments
# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.
# PS Assume that numeric parameters will always be passed to the function, no need to check types
# Various solutions are possible (you are allowed to use other data structures inside function such as list).
# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30
# PSS function should return the result, not print it.

def add_mult(a, b , c):
    if a <= b and b <= c:
        result = (a + b) * c
        return result
    if a <= c and c < b:
        result = (a + c) * b
        return result
    if a > b and b >= c:
        result = (b + c) * a
        return result

result_to_print = add_mult(6, 1, 1)
print(result_to_print)

