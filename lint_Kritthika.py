"""This is a Python program that generates a fib sequence"""
def fib(n):
    """Calculate the n-th fib number"""
    if n ==0  or n ==1:
        return  n
    return fib(n-1)  +  fib(n-2)
def print_fib_sequence():
    """Print the first 10 fib numbers"""
    for i in range(1, 11):
        print('i: ' + str(i) + ' fib: ' + str(fib(i)))
print('fib from 1 to 10: ')
print_fib_sequence()
