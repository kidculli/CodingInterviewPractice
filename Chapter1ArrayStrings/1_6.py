import numpy as np
import pdb 
def prettyprintmatrix(matrix):
    for row in matrix:
        for col in row:
            print col,
        print 
the_matrix = [[21,0,22,73,213],[1,1,1,45,96],[24,0,23,87,99],[24,0,23,87,99],[24,0,23,87,99]] 
#the_matrix = [[1,2,3],[4,5,6],[7,8,9]]
'''
rotates a matrix 90 degrees 
O(n) 
'''
def rotateMatrix90(matrix):
    prettyprintmatrix(matrix)
    print '---------------------------'
    rotated = []
    for index,row in enumerate(matrix):
        rotated.append(list())
    rotated_rows = len(rotated) - 1
    for row_index,row in enumerate(matrix):
        rotated_rows_it = rotated_rows
        for col_index,col in enumerate(row):
            rotated[rotated_rows_it].append(matrix[row_index][col_index])
            rotated_rows_it -=1
            if rotated_rows < 0:
                break
    prettyprintmatrix(rotated)


"""
@param matrix - 2d matrix of ints 
@n - length of each side 
"""
def rotateMatrixInPlace(matrix, n):
    arr = np.array(matrix)
    current = arr[0][0]
    print arr
    temp = arr[0][n-1]
    cycles = n/2
    for cycle in range(0,cycles):
        # begging column index for this cycle 
        begin = 0 + cycle
        # ending column index for this cycle
        end = n-1-cycle

        for i in range(begin, end):
            # top left 
            current = arr[begin,i]
            # top right 
            temp = arr[i,end]
            arr[i,end] = current
            #swap 
            current = temp

            #bottom right 
            temp = arr[end][end - i]
            arr[end][end - i] = current
            #swap 2 
            current = temp
            
            #bottom left 
            temp = arr[end - i][begin]
            arr[end - i][begin] = current 
            #swap 3 

            #top left 
            arr[begin][i] = temp 
            #swap 4 
        print "----------------------------------"
        print arr
        

if __name__ == "__main__":
    #rotateMatrix90(the_matrix)
    rotateMatrixInPlace(the_matrix,len(the_matrix[0]))