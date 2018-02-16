def prettyprintmatrix(matrix):
    for row in matrix:
        for col in row:
            print col,
        print 
the_matrix = [[0,0,1],[1,1,1],[1,0,0]] 

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
rotateMatrix90(the_matrix)