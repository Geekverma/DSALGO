''' generate fibnocci sequence using recursion, DP(memoization) and iteratively
input integer n
output: nth number of sequence
ex:0112358...
axioms: input is integer only
assumption: consider 0 as first seq and 1 as second sequence.
'''
from datetime import datetime
import time
#recurion

def fibnoacci_seq(n:int) ->int:
    #Base case
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibnoacci_seq(n-1)+fibnoacci_seq(n-2)

print(f'starting at..{(datetime.now()).strftime("%X")}')
value = fibnoacci_seq(40)
print(value)
print(f'end at..{(datetime.now()).strftime("%X")}')




#Dynamic programming 

# cache = {}

# def fibnoacci_seq(n:int) ->int:
#     #Base case
#     if n <= 1:
#         return 0
#     elif n == 2:
#         return 1
#     elif not n in cache:
#         cache[n] = fibnoacci_seq(n-1)+fibnoacci_seq(n-2)

#     return cache[n]

# print(f'starting at..{(datetime.now()).strftime("%X")}')
# value = fibnoacci_seq(45)
# print(value)
# print(f'end at..{(datetime.now()).strftime("%X")}')

