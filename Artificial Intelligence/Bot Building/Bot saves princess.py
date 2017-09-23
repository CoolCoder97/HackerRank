def displayPathtoPrincess(n,mat):
    need=n//2
    if(mat[0][0]=="p"):
        for i in range(need):
            print("UP")
        for i in range(need):
            print("LEFT")
    elif(mat[0][n-1]=="p"):
        for i in range(need):
            print("UP")
        for i in range(need):
            print("RIGHT")
    elif(mat[n-1][0]=="p"):
        for i in range(need):
            print("DOWN")
        for i in range(need):
            print("LEFT")
    else:
        for i in range(need):
            print("DOWN")
        for i in range(need):
            print("RIGHT")
            
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
