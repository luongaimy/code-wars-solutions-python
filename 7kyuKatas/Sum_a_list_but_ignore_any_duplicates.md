```
def sum_no_duplicates(l):
    # write your solution here
    remove_list = [] 
    
    for number in l:
        if l.count(number) >= 2:
            remove_list.append(number)
    
    Sum = sum(l) - sum(remove_list) 

    return Sum
```