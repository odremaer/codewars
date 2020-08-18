import string
def generate_hashtag(s):
    lst = s.split()
    r = '#' + ''.join([x.title() for x in lst])
    return r if len(r) < 140 and r != '#' else False


print(generate_hashtag('chto   ne tak'))