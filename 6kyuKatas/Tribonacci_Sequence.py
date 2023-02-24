
def tribonacci(signature, n):
      # Initialize the first three values of the sequence
    a=signature[0]
    b=signature[1]
    c=signature[2]

    if n <=2: 
        return signature[:n]
    else:
        for i in range(3, n):
            d = a + b + c  # Add the last three values to get the next value
            a, b, c = b, c, d  # Shift the values to the left
            signature.append(d)

        return signature
