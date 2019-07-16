# cook your code here
for _ in range(int(raw_input())):
    A,B,N = map(int,raw_input().split())
    if N%2==1:    #odd
        A= A<<((N+1)/2)
        B= B<<((N-1)/2)
    else:
        A= A<<(N/2)
        B= B<<(N/2)
    print(int(max(A,B)/min(A,B)))
