```
def square_digits(num):
    string = str(num)

    list_of_squares = [str(int(digit)**2) for digit in string]
    
    square_digits = int("".join(list_of_squares))
    
    return square_digits
```