```
def pascals_triangle(n):
    table = [[0] * n for i in range(n)]
    
    # build pascal triangle with formula: 
    # table[row,col] = table[row-1, col-1] + table[row-1, col]
    for row in range(n):
        for col in range(n):
            if col == 0:
                table[row][col] = 1
            else:
                if row >= 1:
                    table[row][col] = table[row-1][col] + table[row-1][col-1]
                    
    pascals_triangle = []
    for row in range(n):
        pascals_triangle = pascals_triangle + table[row][:(row+1)]
        
    return pascals_triangle
```