import numpy as np

def efr(data):
    yList = []
    step = 0
    xList = sorted(set(data))
    dataLen = len(data)
    for elem in xList:
        count = data.count(elem)
        step += count
        yList.append(step / dataLen)
    return xList, yList

def sup(data1, data2):
    xList1, yList1 = efr(data1)
    xList2, yList2 = efr(data2)
    difXList = sorted(set(xList1).union(set(xList2)))
    xList1.append(0)
    xList2.append(0)
    i1, i2 = 0, 0
    difYList = []
    for elem in difXList:
        if elem == xList1[i1] == xList2[i2]:
            difYList.append(round(abs(yList1[i1] - yList2[i2]), 6))
            i1 += 1
            i2 += 1
        elif elem == xList1[i1]:
            if xList2[0] > xList1[i1]:
                difYList.append(yList1[i1])
            else:
                difYList.append(round(abs(yList1[i1] - yList2[i2 - 1]), 6))
            i1 += 1
        elif elem == xList2[i2]:
            if xList1[0] > xList2[i2]:
                difYList.append(yList2[i2])
            else:
                difYList.append(round(abs(yList1[i1 - 1] - yList2[i2]), 6))
            i2 += 1
    return max(difYList)

def gen_sup(n):
    dataList = []
    for i in range(5):
        data = np.zeros(n)
        for iteration in range(n):
            xi = np.random.rand()
            r = xm / xi ** (1 / a)
            data[iteration] = r
        dataList.append(data.tolist())
    supList = []
    dataListLen = len(dataList)
    for i in range(dataListLen):
        for j in range(i + 1, dataListLen):
            supList.append(sup(dataList[i], dataList[j]))
    return supList

[a, xm] = [5, 1]
print("Supremum of the ECDF difference of sample n = 5: ", gen_sup(5), sep="\n")
print("Supremum of the ECDF difference of sample n = 10: ", gen_sup(10), sep="\n")
print("Supremum of the ECDF difference of sample n = 100: ", gen_sup(100), sep="\n")
print("Supremum of the ECDF difference of sample n = 1000: ", gen_sup(1000), sep="\n")
print("Supremum of the ECDF difference of sample n = 10^5: ", gen_sup(10**5), sep="\n")
