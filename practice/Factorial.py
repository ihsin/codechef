# Solution to https://www.codechef.com/problems/FCTRL2
t= input()
t= int(t)


for x in range(t,0,-1):
    num= input()
    num= int(num)
    fact=1
    for i in range(num,1,-1):
        fact*=i
    print(fact)

