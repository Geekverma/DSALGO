''' Create a function to sum digits of number 

ex: n = 4321, 4+3+2+1=10
'''


def sum_of_digits(num):
    #base condition
    if num == 0:
        return 0
    else:
        return num%10 + sum_of_digits(num//10)


value = sum_of_digits(8537)
print(value)