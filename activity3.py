def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
print("the factorial of zero is", factorial(0))
print("the factorial of one is", factorial(1))
print("the factorial of two is", factorial(4))
print("the factorial of five is", factorial(5))
print("the factorial of ten is", factorial(10))