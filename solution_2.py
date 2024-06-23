with open('input.rtf', 'r', encoding='utf-8') as o:
    with open('output.rtf', 'w', encoding='utf-8') as f:
        for x in o:
            if x[0] == 'a' or x[0] == 'A':
                f.write(x)
#или
with open('input.rtf', 'r', encoding='utf-8') as o:
    with open('output.rtf', 'w', encoding='utf-8') as f:
        for x in o:
            if x[0].lower == 'a':
                f.write(x)
