# Task 1: Calculate Factorial Using a Function


def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

print(f"factorial of 5 is : {factorial(5)}")


