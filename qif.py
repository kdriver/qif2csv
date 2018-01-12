
f = open('new.qif')

contents = []
for my_line in f:
    if my_line[0] != '!':
        contents.append(my_line.strip('\n'))


record = ""
for r in contents:
    if r == "^":
        print(record)
        record = "" 
    else:
        if r != "":
            sep = ','
            if record == "":
                sep=''
            text = sep + r[1:]
            record += text 



