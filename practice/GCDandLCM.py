# cook your code here
t= raw_input()
t= int(t)

def gcd(a,b):
    if a>b:
        a,b=b,a
    if b%a==0:
        return a
    return gcd(b%a,a)
# 120 140
for _ in range(t):
        arr= map(int, raw_input().split())
        LCM=1
        GCD=1
        # minimum=arr[0] if arr[1]>arr[0] else arr[1]
        # maximum=arr[1] if arr[1]>arr[0] else arr[0]
        # for i in range(minimum,1,-1):
        #         if minimum%i==0 and maximum%i==0:
        #                 GCD=i
        #                 break
        GCD= gcd(arr[0],arr[1])
        LCM= (arr[0]*arr[1])/GCD
        print(GCD),
        print(LCM)


