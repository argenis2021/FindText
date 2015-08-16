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

for word in list_words:
    #inicio contador
    contador=0
    for line in list_lines:
        if line.find(word) >= 0:
            contador += 1
    print word + " " + str(contador) + " veces"        