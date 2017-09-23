def nextMove(n,row_bot,col_bot,mat):
    row_princess=0
    for i in mat:
        if("p" in i):
            col_princess=i.index('p')
            break
        row_princess+=1
#print(row_princess,col_princess)
    if(row_bot>row_princess):
        return "UP"
    elif(row_bot<row_princess):
        return "DOWN"
    elif(col_bot>col_princess):
        return "LEFT"
    elif(col_bot<col_princess):
        return "RIGHT"
    
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
