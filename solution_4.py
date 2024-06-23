with open('input.rtf', 'r', encoding='utf-8') as o:
    with open('output.rtf', 'w') as f:
        for x in o:
            if len(x) > 20:
                f.write(x)
