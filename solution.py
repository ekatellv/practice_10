with open('input.rtf', 'r', encoding='utf-8') as o:
    with open('output.rtf', 'w', encoding='utf-8') as f:
        for i in o:
            f.write(i.upper())
