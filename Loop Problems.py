# 1) Pascals Triangle

n=int(input())
dp=[[0 for _ in range(n)]for _ in range(n)]
for i in range(1,n+1):
    if(i==1):
        dp[i-1][0]=1
        continue
    if(i==2):
        dp[i-1][0]=1
        dp[i-1][1]=1
        continue
    for j in range(i):
        if(j==0):
            dp[i-1][0]=dp[i-2][0]
        elif(j==i-1):
            dp[i-1][j]=dp[i-2][i-2]
        else:
            dp[i-1][j]=dp[i-2][j-1]+dp[i-2][j]
for i in dp:
    print(i)
            



for i in range(5):
    c=9-(2*i+1)
    for j in range(1,10):
        if(j<=c):
            print(" ",end="")
        else:
            print("*",end="")
    print()
for i in range(3,-1,-1):
    c=9-(2*i+1)
    for j in range(1,10):
        if(j<=c):
            print(" ",end="")
        else:
            print("*",end="")
    print()



print()
n=5
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if (j == (n - i + 1) or j == (n + i - 1)):
            print("* ",end="")
        elif (i == n):
            print("* ", end="")
        else :
            print(" "+" ", end="")
    print()


n=5

for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(i,n+1):
        if(j==i or j==n or i==1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
    
    
    
        
    
        
