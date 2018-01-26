my_file = open("text_doc.txt", encoding='utf8')
my_string = my_file.read()
print(my_string)
my_file = open("text_doc1.txt", 'a')
print(my_string +'!\n', file=my_file)

with my_file as q:
    q.write(str(input('Введите имя: ')))
