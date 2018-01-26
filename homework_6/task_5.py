a = open("text_doc.txt", encoding='utf8')
b = a.split(' ')
b.sort()
print((b.rstrip()) + '\n')
