def bell(n):
    arr=[[0 for i in range(n+1)]for j in range(n+1)]
    arr[0][0]=1
    for i in range(1,n+1):
        arr[i][0]=arr[i-1][i-1]
        for j in range(1,i+1):
            arr[i][j]=arr[i-1][j-1]+arr[i][j-1]
    return arr[n][0]
n=int(input())
print(bell(n))
