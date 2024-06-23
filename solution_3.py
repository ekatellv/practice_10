ith open('input.rtf', 'r', encoding='utf-8') as o:
    with open('output.rtf', 'w') as f:
        for x in o:
            word = x[0]
            f.write(word)
