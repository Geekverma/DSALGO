from typing import List


def merge(l1: List, l2: List, m:int, n:int) -> List:
    i,j,k=0,0,0
    temp = []
    #fill temp by comapring each index of l1 and l2 element.
    while i<m and j<n:
        if l1[i] <= l2[j]:
            # print(i,j,temp[0],l1[i])
            temp.append(l1[i])
            k+=1
            i+=1
        else:
            temp.append(l2[j])
            k+=1
            j+=1

    
    for item in range(j,n):
        temp.append(l2[item])
        # i+=1
        
    l1 = temp
    return l1


print(merge([1,3,0,0,0],[2,4,5],2,3))