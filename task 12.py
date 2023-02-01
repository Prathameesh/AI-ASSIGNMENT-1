#12. print each elemt of list along with its index number(both forward and backward)
L1=['P','Y','T','H','O','N']
length=len(L1)
for e in range(length):
	print("Forward indexing: ",e,"Backward indexing",(e-length),"Element value is",L1[e])	
