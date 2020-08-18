def move_zeros(array):
    array.sort(key=lambda x: x == 0 and x is not False)
    return array


def move_zerosv2(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))


print(move_zeros([0,1,None,2,False,1,0]))