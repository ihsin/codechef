
# 5 1 3 4
t=raw_input()
t=int(t)

for _ in range(t):
        n=raw_input()
        n=int(n)
        arr=[]
        arr= raw_input().split()
        arr= map(int, arr)
        if n==2:
            print(int(arr[0])+int(arr[1]))
            continue;
        if n>2 and n<=100:
            arr.sort()
            print(int(arr[0])+int(arr[1]))
            continue
        max=0
        for i in arr:
                if int(i)>max:
                        max=int(i)
        ans=[0]*(max+1)
        sum=0
        for i in arr:
                ans[int(i)]=1
        k=0
        for i in range(max):
                if ans[i]==1:
                        sum +=i
                        k +=1
                        if k==2:
                                break
        print(sum)

