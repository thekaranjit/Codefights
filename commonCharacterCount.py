def commonCharacterCount(s1, s2):
    b = list(s1)
    c = list(s2)

    counter = 0

    for i in  b:
        for j in c:
            if i == j:
                counter += 1
                break
    return counter

    
