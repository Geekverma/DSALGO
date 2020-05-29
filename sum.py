def anagram(s1,s2):
	s1=s1.replace(" ","").lower()
	s2=s2.replace(" ","").lower()
	if sorted(s1)==sorted(s2):
		print(True)
	else :
		print(False)

anagram("dog","gid")

def anagram(s1,s2):
	s1=s1.replace(" ","").lower()
	s2=s2.replace(" ","").lower()

	if len(s1) != len(s2):
		print(False)
		return False
	count={}
	for letter in s1:
		if letter in count:
			count[letter] += 1
		else:
	    		count[letter] = 1
	for letter in s2:
		if letter in count:
			count[letter] -= 1
		else:
    		 count[letter] = 1

	for k in count:
    	 if count[k] != 0:
    	 	print(False)
    	 	return False

	print(True)
	return True

anagram("The Morse Code","Here comes dots")

# # l=[1,3,2,4,2,4,6,5,6]
# # l=l.sort()
# # print(l)
# # for i in set(l):
# 	# print(i,end=" ")
# l=zip([1,2,3,4,5],[6,7,8,9,10])
# for n,m in l:
# 	print(n,m,end=" ")
# print(l)