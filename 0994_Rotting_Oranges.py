from collections import deque

class Solution:
    counter =0
    def orangesRotting(self, grid):
        
        rows, cols = len(grid), len(grid[0])
        if rows == 0:
            return -1
        
        counter=0
        movement = [(1,0), (-1,0), (0,1) , (0,-1)]
        
        fresh_oranges = 0
        rotten = deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2: #if it's a rotten
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh_oranges +=1
        while rotten and fresh_oranges > 0: #until no rotten and no more fresh oranges
            counter+=1
            
            for _ in range(len(rotten)):
                
                x, y = rotten.popleft()
                
                for dx, dy in movement:
                    i = x+dx
                    j = y+dy
                    
                    
                    if i < 0 or i == rows or j <0 or j==cols or grid[i][j] == 0 or grid[i][j] == 2: #if it's empty or rotten already , skip
                        continue
                        
                    fresh_oranges -=1
                    grid[i][j]=2
                    
                    rotten.append((i, j))
            
        if fresh_oranges == 0:
            return counter
        return -1