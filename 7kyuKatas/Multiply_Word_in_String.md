```
def modify_multiply(st, loc, num):
    word = st.split()
    
    selected_word = word[loc]
    
    word_rep = '-'.join([selected_word] * num)
    
    return word_rep
```
