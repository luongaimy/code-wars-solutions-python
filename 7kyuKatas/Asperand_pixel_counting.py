
def count_pixels(k):
    if k==1:
        return 11
    border = k * 4 
    bridge = 6
    inner = (k-1)*4 
    return border + bridge + inner
