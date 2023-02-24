
def digitize(n):
    reversed_numbers = []
    
    if n == 0:
        return [0]
    else:
        for digit in str(n):
            reversed_numbers.insert(0, int(digit))
            
    return reversed_numbers
        
