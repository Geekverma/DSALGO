def string_permutation(s):
    'create a list of string permutation'
    l=[]
    #base case
    if len(s) <=1 :
        l = [s]

    else:
        # l = [s[i]+string_permutation(s[:i] + s[i+1:]) for i in range(len(s))]
        for i in range(len(s)):
            for perm in string_permutation(s[:i]+s[i+1:]):
                l+=[s[i]+perm]
            # print(l)

    return l
    


def test_string_permute():
    ''' test for string permutation'''
    assert string_permutation('ab') == ['ab','ba']
    assert string_permutation('abc') == ['abc','acb','bac','bca','cab','cba']
    # assert string_permutation('a_b') == ['a_b','ab_','_ab','_ba','b_a','b_a']