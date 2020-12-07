def sum(data, tong):
    list_result = []
    L = []
    for i in data:
        L.append(['%s+' % i, '%s-' % i, '%s' % i])
    L = L[:-1]
    # print(L)
    for i in range(3 ** 8):
        A = [0, 0, 0, 0, 0, 0, 0, 0]
        for a in range(8):
            A[7 - a] = i % 3
            print(i%3)
            if i == 1:
                break
            i = i // 3
            a += 1
        L_new = L[0][A[0]] + L[1][A[1]] + L[2][A[2]] + L[3][A[3]] + L[4][A[4]] + L[5][A[5]] + L[6][A[6]] + L[7][A[7]] + T[-1]
        total = eval(L_new)
        if total == tong:
            list_result.append(L_new)
    return list_result
if __name__ == '__main__':
    T = '123456789'
    list_result = b1(T, 100)
    print('list_result', list_result)