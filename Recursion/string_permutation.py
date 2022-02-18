''' string permutation
'abc'-> 'abc','acb','bac','bca','cab','cba'
'''

def string_permutation(string):
    out = []
    #base case
    if len(string) == 1:
        out = [string]
    else:
        ''' take a part of sting like 'a' from 'abc' and find the combination from the rest 'bc' 
        and join the combinations ['bc','cb'] to initial string
        '''
        for i, let in enumerate(string):
            for perm in string_permutation(string[:i] + string[i+1:]):
                print(i,string[:i], string[i+1:],out)
                print('current let is',let)
                print('current perm is',perm)
                out+=[let+perm]

    return out


value = string_permutation('ab')
print(value)
