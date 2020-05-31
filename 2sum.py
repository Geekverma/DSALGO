def pair(arr,k):
	# if len(arr)<2:   # edge case
	# 	return 
	seen = ()
	output = ()
	for num in arr:
		target = k-num
		if target not in seen:
			seen.add(num)
		else:
			output.add(((min(num,target),max(num,target)))
	
    # return  '\n'.join(map(str,list(output)))
	return len(output)


a=pair([1,3,2,2],4)
print(a)