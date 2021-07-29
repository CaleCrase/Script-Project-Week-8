"""
Program: Week8 Project2
Author: Cale Crase
Newton's method 2
"""

def newton(x, estimate):
    tolerance = 0.000001
    difference = abs(x - estimate ** 2)
    y = 1.0
    if difference <= tolerance:
        return estimate
    else:
        estimate = newton(x, (estimate + x/estimate)/2)
    return estimate

def main():
    while True:
        x = (input("Enter a number: "))
        if not x.isnumeric():
            break
        print(newton(float(x), 1.0))
main()

