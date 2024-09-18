# This is the starter template for the week 1 participation assignment

# Input n: integer
# constraints: n > 0
# Output: nth Fibonacci number
# Examples:
# |  Input  |  Output  |
# |---------|----------|
# |    1    |     0    |
# |---------|----------|
# |    5    |     3    |
# |---------|----------|
# |   20    |   4181   |
# |---------|----------|
# Recursive implementation of the Fibonacci sequence
def fibonacciRecursive(n):
    # Base case for n=1 or n=2
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Recursive call for n > 2
        return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)    

# Input n: integer
# constraints: n > 0, no recursion in implementation
# Output: nth Fibonacci number
# Examples:
# |  Input  |  Output  |
# |---------|----------|
# |    1    |     0    |
# |---------|----------|
# |    5    |     3    |
# |---------|----------|
# |   20    |   4181   |
# |---------|----------|
# Iterative implementation of the Fibonacci sequence
def fibonacciIterative(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b

# Main section to handle user input and display output
if __name__ == "__main__":
    n = int(input("Enter a positive integer for Fibonacci calculation: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print(f"Recursive: Fibonacci({n}) = {fibonacciRecursive(n)}")
        print(f"Iterative: Fibonacci({n}) = {fibonacciIterative(n)}")
