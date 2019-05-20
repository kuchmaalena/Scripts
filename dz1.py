def is_permutation(a:str, b:str):
    s1 = set(a)
    s2 = set(b)
    if s1.union(s2) == s1:
        return(True)
    else:
        return(False)
        
           
                    
