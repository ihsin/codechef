# Solution to https://www.codechef.com/problems/HS08TEST
# cook your dish here
x,y=input().split()
x= int(x)
y= float(y)
if x%5!=0 or x+0.5>y:           
#x>=y is wrong, y can be any FPN with dp.
#e.g y=4.20 and and x=4, then x!>=y but x+0.5>y
    print ('%.2f' % y)
else:
    result=y-x-0.50
    print ('%.2f' % result)

#Lesson learned :
#NZEC error may come even if there are no RTE :)