#итераторы

#итерируемый объект - список
#mylist = [1,2,3]
#for i in mylist:
#   print(i)
#генераторное выражение
#mylist2 = [x*x for x in range(3)]
#for i in mylist2:
#   print(i)

#генераторы - итерируемые объекты, но прочитать их можно один раз.(не хранят значение в памяти,
# а генерируют их на лету)
#mygenerator = (x*x for x in range(3))
#for i in mygenerator:
#    print(i)
#Yield это ключевое слово, которое используется примерно как return — отличие в том,
# что функция вернёт генератор.
def createGenerator():
    mylist3 = range(3)
    for i in mylist3:
        yield i*i

mygenerator = createGenerator() #создаем генератор
print(mygenerator)
for i in mygenerator:
    print(i)