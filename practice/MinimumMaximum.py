# cook your code here
t= raw_input()
t= int(t)

for _ in range(t):
    N= raw_input()
    N= int(N)
    arr= map(int, raw_input().split())
    minimum= min(arr)
    print (N-1)*minimum
