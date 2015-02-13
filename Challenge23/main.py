p = [[(" "*(4-len(str(j*i))) if i != 1 else "") +str(i*j) for i in range(1,13)] for j in range(1,13)]
	for i in p:
		print("".join(i).strip(" ")+'\n')