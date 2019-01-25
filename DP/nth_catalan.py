def binomial(n,k):
    res=1
    if(k>n-k):
        k=n-k
    for i in range(k):
        res*=n-i
        res/=i+1
    return res
def cat(n):
    catalan=[0]*(n+1)
    if(n==0 or n==1):
        return 1
    catalan[0],catalan[1]=1,1
    for i in range(2,n+1):
        catalan[i]=0
        for j in range(i):
            catalan[i]=catalan[i]+catalan[j]*catalan[i-j-1]
    return catalan[n]
n=int(input())
c=binomial(2*n,n)
print(int(c/(n+1)))
print(cat(n))
