def genPrimes():
    primeList = []
    num = 2
    while True:
        flag = True
        for p in primeList:
            if (num % p == 0 and flag):
                flag = False
        if (flag):
            primeList.append(num)
            yield int(num)
        num += 1
