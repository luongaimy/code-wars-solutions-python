```
def est_subsets(arr):
    length = len(arr)
    
    count = 0
    unique_list = []
    
    for element in arr:
        if element not in unique_list:
            count += 1
            unique_list.append(element)  
    
    num_subsets = 2**count - 1 
    
    return num_subsets
```