


def permutation(rep, prefixe, liste):


    if prefixe and prefixe[-1][1] == 'E':
        rep.append(prefixe)
   
    else:
        for i in range(len(liste)):
            if (prefixe and liste[i][0] == prefixe[-1][1]) or (not prefixe and liste[i][0] == 'A'):
                
                permutation(rep, prefixe + [liste[i]], liste[:i] + liste[i+1:])

lst = []    
rep = []
permutation(rep, lst, [('A', 'B'), ('C','E'), ('B', 'E'), ('C', 'D'), ('B', 'C'), ('B', 'A'), ('A', 'E'), ('D', 'E')])

print(rep)

