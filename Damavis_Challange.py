#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -----------------------------------------------------------
# Damavis Challenge
#
# 09-03-21 Marc Maldonado Lorca, Terrassa, Spain
# 
# maldonadolorcamarc@gmail.com
# -----------------------------------------------------------


# In[2]:


# Main function recursive 
def numberOfAvailableDifferentPaths(board, snake, depth):  
    depthCounter = 0 # To save de depth in the tree
    pathDecisions = '' # Store paths with 'U D L R' string
   
    numberOfAvailableDifferentPathsRecursive(board, snake[:], depth, depthCounter, pathDecisions)
    
    return pathNumber

# To check if there are colisions or we are out of the board
def validMovement(board,snake,newPosition):

    #Check boundaries
    if 0 <= newPosition[0] <= board[0]-1 and 0 <= newPosition[1] <= board[1]-1:
        pass
    else:
        return False

    #Check collisions
    if newPosition in snake[:-1]:
        return False
    else:
        return True

# Recursive function
def numberOfAvailableDifferentPathsRecursive(board, snake, depth, depthCounter, pathDecisions):
    
    if depthCounter == depth: # If que found solution
        global pathNumber # Variable to return stored as a global in order to not modify it through recursive calls 
        pathNumber += 1
        print(pathDecisions)
        return 0
    
    if depthCounter < depth: # If we can still exploring through the tree
        depthCounter += 1
        

    newPosition = snake[0] # Auxiliar to compute next move
    

     # Go Down
    if validMovement(board,snake, [newPosition[0],newPosition[1]+1]): #Check if valid
        
        #Update snake
        newSnake = snake[:] #Copy snake, if qe do not do it the recursive call won't stack the values
        
        #New snake
        newSnake.pop()
        newSnake.insert(0,[newPosition[0],newPosition[1]+1])

        #Recursive Call
        numberOfAvailableDifferentPathsRecursive(board, newSnake, depth, depthCounter, pathDecisions+'D')
        
    # Go Up
    if validMovement(board,snake, [newPosition[0],newPosition[1]-1]):
        
        #Update snake
        newSnake = snake[:] #Copy snake, if qe do not do it the recursive call won't stack the values
        
        #New snake
        newSnake.pop()
        newSnake.insert(0,[newPosition[0],newPosition[1]-1])

        #Recursive Call
        numberOfAvailableDifferentPathsRecursive(board, newSnake, depth, depthCounter, pathDecisions+'U')
    
    # Go Right
    if validMovement(board,snake, [newPosition[0]+1,newPosition[1]]): #Check if valid
        
        #Update snake
        newSnake = snake[:] #Copy snake, if qe do not do it the recursive call won't stack the values
        
        #New snake
        newSnake.pop()
        newSnake.insert(0,[newPosition[0]+1,newPosition[1]])

        #Recursive Call
        numberOfAvailableDifferentPathsRecursive(board, newSnake, depth, depthCounter, pathDecisions+'R')

    # Go Left
    if validMovement(board,snake, [newPosition[0]-1,newPosition[1]]):
        #Update snake
        newSnake = snake[:] #Copy snake, if qe do not do it the recursive call won't stack the values
        
        #New snake
        newSnake.pop()
        newSnake.insert(0,[newPosition[0]-1,newPosition[1]])

        #Recursive Call
        numberOfAvailableDifferentPathsRecursive(board, newSnake, depth, depthCounter, pathDecisions+'L')

    return 0
    


# In[3]:



if __name__ == "__main__":
    print("----- TEST 1 ------")
    pathNumber = 0
    board = [4,3]
    snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
    depth = 3
    assert numberOfAvailableDifferentPaths(board, snake, depth) == 7, "Should be 7" 
    print('Number of paths: ' + str(pathNumber))
    print('\n')
    
    
    print("----- TEST 2 ------")
    pathNumber = 0
    board = [2, 3]
    snake = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
    depth = 10
    assert numberOfAvailableDifferentPaths(board, snake, depth) == 1, "Should be 1" 
    print('Number of paths: ' + str(pathNumber))
    print('\n')
    
    print("----- TEST 2 ------")
    pathNumber = 0
    board = [10, 10]
    snake = [[5,5], [5,4], [4,4], [4,5]]
    depth = 4
    assert numberOfAvailableDifferentPaths(board, snake, depth) == 81, "Should be 81" 
    print('Number of paths: ' + str(pathNumber))
    print('\n')
    
    print("Everything passed")


# In[ ]:




