def pig_it(text):
    b = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in b])


print(pig_it('abhram link'))
