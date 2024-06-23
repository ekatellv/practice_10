with open('input.rtf', 'r', encoding='unt-8') as o:
    with open('output.rtf', 'w') as f:
        n = o.readline().strip()
        if n.isdigit():
            count = 0
            for line in o:
                count += 1
            if count == int(n):
                f.write('yes')
            else:
                f.write('no')
        else:
            f.write('error')
          
