def spiralTraverse(array):
    # Write your code here.
    print("Vertical length",len(array))
    print("Horizontal length",len(array[0]))

    if(len(array) == 1 and len(array[0]) == 1):
        return array[0]

    start_row = 0
    end_row = len(array) - 1
    start_col = 0 
    end_col = len(array[0]) - 1

    output_array = []
    
    while(start_row <= end_row and start_col <= end_col):

        # Looping through N, E, S, W perimeters. 4 loops.
        for i in range(start_col, end_col + 1):
            output_array.append(array[start_row][i])
        start_row += 1

        # this is for arrays with one row:
        if(start_row > end_row):
            break
    
        # East
        for i in range(start_row, end_row + 1):
            output_array.append(array[i][end_col])
        end_col -= 1

        # arrays with one column
        if(start_col > end_col):
            break
                
        # South 
        for i in reversed(range(start_col, end_col + 1)):
            output_array.append(array[end_row][i])
        end_row -= 1
        
        # West
        for i in reversed(range(start_row, end_row + 1)):
            output_array.append((array[i][start_col]))
        start_col += 1
       
        
    return output_array
 
    
