list_words = []
list_lines = []

f1 = open('list2')
for line in f1.readlines():
    # remove the trailing \n
    list_words.append(line[:-1])

f2 = open('text2')
for line in f2.readlines():
    # remove the trailing \n
    list_lines.append(line[:-1])

for line in list_lines:
    for word in list_words:
        if word in line:
            print "Se encontro el monto " + word + " en la siguiente linea del archivo:"
            print line
            print "*"*70
            break