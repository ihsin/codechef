
t= raw_input()
t= int(t)

for _ in range(t):
	arr= []
	arr= map(float, raw_input().split())
	price= arr[0]*arr[1]
	if arr[0]>1000:
		price=price- 0.1*price
	print('%.6f'%price)
