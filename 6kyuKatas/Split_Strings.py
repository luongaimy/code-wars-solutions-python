
def solution(s):
    if len(s) % 2 == 1:
        s += '_'

    pairs_list = []
    for i in range(0, len(s), 2):
        pairs_list.append(s[i:i+2])
        
    return pairs_list
