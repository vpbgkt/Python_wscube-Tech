for i in range(0, 5):
    for j in range(0, i):
        print('*', end=' ')
        for k in range(5-i, 0, -1):
            print('0', end='')
    print('')
