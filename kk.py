list_words = []
list_lines = []

f1 = open('list')
for line in f1.readlines():
    # remove the trailing \n
    list_words.append(line[:-1])

f2 = open('text')
for line in f2.readlines():
    # remove the trailing \n
    list_lines.append(line[:-1])

for line in list_lines:
    for word in list_words:
        if word in line:
            print line
            print word
            # one word per line is enough
            break 