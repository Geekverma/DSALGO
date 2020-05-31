# def find(arr1,arr2):
#     arr1.sort()
#     arr2.sort()

#     for num1,num2 in zip(arr1,arr2):
#         if num1!=num2:
#             print(num1)
#             return num1
#         else:
#             pass

#     print(arr1[-1])
#     return arr1[-1]
# d={num1:m.count(num2) for (num1,m.count(num2)) in zip(l,m)}
l=[1,2,3,4,5,6,7]
m=[3,7,2,5,4,6]
d={}
m=sorted(m)
for (num1,num2) in zip(l,m):
    d[num1]=m.count(num1)
    if m.count(num1)==0:
        print(f"missing element:{num1}")
    else:
        pass
print(d)