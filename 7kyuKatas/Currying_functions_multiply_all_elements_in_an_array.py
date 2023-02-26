def multiply_all(arr):
    def number(n):
        list_arr = []
        for a in arr: 
            b = a*n
            list_arr.append(b)
        return list_arr
    return number
