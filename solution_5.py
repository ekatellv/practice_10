with open('input.rtf', 'r', encoding='utf-8') as o:
    with open('output.rtf', 'w') as f:
        try:
            n_1 = int(o.readline())
            n_2 = int(o.readline())
            n_3 = int(o.readline())
            f.write((n_1 / n_2) + n_3)
        except ValueError:
            print('Неверное значение')
        except ZeroDivisionError:
            print('Деление на ноль')
