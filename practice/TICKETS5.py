# cook your code here
# ABABAB
for _ in range(int(raw_input())):
    arr= raw_input()
    l= len(arr)
    if l==2 and arr[0]==arr[1]:
        print 'NO'
        continue
    ans='NO'
    i=0
    while i<l:
        if i+2<l and arr[i]==arr[i+2] and arr[i]!=arr[i+1]:
            i+=1
            continue
        else:
            break
    if i==l-2:
        ans='YES'
    print ans
