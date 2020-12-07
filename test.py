def sum(data, tong):
    result = []
    Lct = []
    for i in data:
        Lct.append(['%s+' % i, '%s-' % i, '%s' % i])
    Lct = Lct[:-1]
    for i in range(3 ** 8):
        Ops = [0, 0, 0, 0, 0, 0, 0, 0]
        for a in range(8):
            Ops[7 - a] = i % 3
            if i == 1:
                break
            i = i // 3
            a += 1
        Lct_data = Lct[0][Ops[0]] + Lct[1][Ops[1]] + Lct[2][Ops[2]] + Lct[3][Ops[3]] + Lct[4][Ops[4]] + Lct[5][Ops[5]] + \
                   Lct[6][Ops[6]] + Lct[7][Ops[7]] + data[-1]
        total = eval(Lct_data)
        if total == tong:
            result.append(Lct_data)
    return result


if __name__ == '__main__':
    data = '123456789'
    result = sum(data, 100)
    for i in result:
        print("result: ", i, "=", 100)
