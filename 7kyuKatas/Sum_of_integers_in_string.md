```
def sum_of_integers_in_string(s):
    temp = "0"
    sum = 0
    # read each character in input string
    for ch in s:
    # if current character is a digit
        if (ch.isdigit()):
            temp += ch
        # if current character is an alphabet
        else:
            # increment Sum by number found
            # earlier(if any)
            sum += int(temp)
            # reset temporary string to empty
            temp = "0"
    # atoi(temp.c_str1()) takes care
    # of trailing numbers
    return sum + int(temp)
```