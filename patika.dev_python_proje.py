def flatten(liste):
    if isinstance(liste, list):
        flat_liste = []
        for i in liste:
            flat_liste.extend(flatten(i))
        return flat_liste
    else:
        return [liste]



liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
liste.reverse()

res = flatten(liste)


print("Flat edilmiş liste : " + str(res))