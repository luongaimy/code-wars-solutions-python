def get_count(sentence):
    count = 0
    string = "aeiou"
    l = []
    for v in sentence:
        for a in string:
            if v==a:
                l.append(v)
                
    return len(l)