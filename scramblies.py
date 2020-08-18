#GOVNO BLYAT NE SDELAL
def scramble(s1, s2):
    k = -1
    for i in s2:      
        #для запоминания индекса(для реплейса)
        k = -1
        for let in s1:
            k += 1
            if i == let:
                s1 = s1.replace(s1[k], '')
            else:


    return


print(scramble('rkqodl', 'world'))

