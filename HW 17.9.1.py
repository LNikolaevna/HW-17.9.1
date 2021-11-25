def not_mistakes_in_data(st):
    out = True
    if type(st) == list:
        for x in st:
            try:
                float(x)
            except:
                print(f'{x} - не соотвествует формату числа')
                out = False
    elif type(st) == str:
        try:
            float(st)
        except:
            print(f'{st} - не соотвествует формату числа')
            out = False
    return out


def sort(lst):
    return sorted([float(x) for x in lst])


def search(lst, x):
    niz = 0
    verch = len(lst) - 1
    if lst[niz] > x:
        return "Нет элемента меньше заданного"
    while niz < verch:
        ser = (niz + verch) // 2
        item = lst[ser]
        if item == x:
            if ser == 0:
                return "Нет элемента меньше заданного"
            else:
                return ser - 1
        if item > x:
            verch = ser
        else:
            niz = ser + 1
    if lst[ser] < x:
        return ser
    else:
        return ser - 1


if __name__ == '__main__':

    Spisok = input('Введите последовательность чисел через пробел\n')
    Chislo = input('Введите число\n')

    l_Spisok = Spisok.split(' ')

    if not_mistakes_in_data(l_Spisok) and not_mistakes_in_data(Chislo):
        pozicia = search(sort(l_Spisok), float(Chislo))
        if pozicia == 'Нет элемента меньше заданного':
            znachenie = 'Отстутсвует'
        else:
            znachenie = sort(l_Spisok)[pozicia]
        print(f'Номер позиции элемента в отсортированном списке: {pozicia}\nЗначение элемента: {znachenie}')
