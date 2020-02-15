grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
def dfs(grid,i, j):
#     print(i)
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0':
        return
    print('\n'.join(map(''.join, grid)))
    print('---------')
    grid[i][j]='0'
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)    
    dfs(grid, i, j+1)    
    dfs(grid, i, j-1)    
    

counter=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        print('i is :{}'.format(i))
        print('j is :{}'.format(j))


        if grid[i][j]=='1':
            dfs(grid,i,j)
            counter+=1

print(counter)