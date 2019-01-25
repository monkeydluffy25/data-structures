def ugly(n):
    arr=[0]*n
    arr[0]=1
    i2,i3,i5,next2,next3,next5=0,0,0,2,3,5
    for i in range(1,n):
        arr[i]=min(next2,next3,next5)
        if(arr[i]==next2):
            i2=i2+1
            next2=arr[i2]*2
        if(arr[i]==next3):
            i3=i3+1
            next3=arr[i3]*3
        if(arr[i]==next5):
            i5=i5+1
            next5=arr[i5]*5
    return arr[-1]
t=int(input())
print(ugly(t))
