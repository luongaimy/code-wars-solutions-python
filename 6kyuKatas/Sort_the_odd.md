```
def sort_array(source_array):
    # Return a sorted array.
    length_list = len(source_array)
    
    for i in range(0,length_list):
        for j in range(i+1,length_list):
            if source_array[i]%2==1 and source_array[j]%2==1:
                if source_array[j] < source_array[i]:
                    temp = source_array[i]
                    source_array[i] = source_array[j]
                    source_array[j] = temp
                    
    return source_array
```