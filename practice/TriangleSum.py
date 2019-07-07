# Solution for https://www.codechef.com/problems/SUMTRIAN
t= raw_input()
t= int(t)

for i in range(t):
	row= raw_input()
	row= int(row)
	mat= []
	for i in range(row):
		arr=[]
		arr=raw_input().split()
		mat.append(arr)
	for i in range(row-1,0,-1):
		for j in range(i):
			mat[i-1][j]= int(mat[i-1][j]) + max(int(mat[i][j+1]),int(mat[i][j]))
	print(mat[0][0])
