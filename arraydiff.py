def array_diff(a, b):
    c = []
    for i in b:
        for j in a:
            if i == j:
                a.remove(j)
            else:
                pass
    return a

print(array_diff([1,2,2],[2]))