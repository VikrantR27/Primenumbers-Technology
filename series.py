import math
def is_series(lst):
    flag=[]
    for n in lst :
        if(n==0):
            flag.append(1)
        else :    
            lg=math.log2(abs(n))
            if n>0 and (lg%4==0 or lg%4==1) :
                flag.append(1)
            elif n<0 and (lg%4==2 or lg%4==3) :
                flag.append(1)
            else:
                flag.append(0)
    sum=0
    for n in flag:
        sum=sum+n
    
    if sum==len(flag) :
        print("All numbers in list are part of the series")
    else :
        print("Not all numbers are part of the series")

            

# is_series([0,1,2,-4,-8,32,-64])