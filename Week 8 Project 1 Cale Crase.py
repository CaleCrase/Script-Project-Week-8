"""
Program: Week8 Project1
Author: Cale Crase
Newton's square root method
"""
def newton(x):
    tolerance = 0.000001
    estimate = 1.0
    while True:
        estimate = (estimate + x/estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
        return estimate

def main():
    while True:
        x = (input("Enter a number: "))
        if not x.isnumeric():
            break
        print(newton(float(x)))
main()
