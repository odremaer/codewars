def first_non_repeating_letter(string):
    i = -1
    for let in string.lower():
        i = i + 1
        if string.lower().count(let) == 1:
            return string[i]
        elif i == (len(string) - 1):
            return ''
    if string == '':
        return string




print(first_non_repeating_letter('abba'))