''' Recursion is a technique to call one or more times to itself
factorial program to demostrate how fatorial of a number is identify
, with a base condition set to 1!=1
'''

''' without memorization'''
# def fatorial(num):
#     if num == 0:
#         ''' base condition '''
#         return 1
#     else:
#         return num*fatorial(num-1)


# value = fatorial(51)
# print(value)




''' Memorization is a technique to store the result in chache and for letter use to reduce the cost of calling the memory for the same result'''

cache = {}

def fact(num):
    #Base case
    if num == 0:
        return 1

    elif not num in cache:
        cache[num] = num*fact(num-1)

    
    return cache[num]
        

value = fact(5)
print(value)
print(cache)