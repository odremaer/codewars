def who_is_next(names, r):
    if r == 1:
        return names[0]
    else:
        for i, j in enumerate(range(r)):
            print(i+1,names)
            popped_person = names.pop(0)
            for j in range(2):
                names.append(popped_person)
        return popped_person


print(who_is_next(["1", "2", "3", "4"], 75))