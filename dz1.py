def is_permutation(a:str, b:str):
    s1 = set(a)
    p1 = {}
    for letter in s1:
        p1[letter] = a.count(letter)
    s2 = set(b)
    p2 = {}
    for letter in s2:
        p2[letter] = b.count(letter)

    return(p1 == p2)
        
           
                    
