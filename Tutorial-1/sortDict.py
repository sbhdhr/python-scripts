
def getP(val):
    return val['p']

P = [3,2,1]
B = ['a','b','c']

C = []

for i in range(len(P)):
    C.append({'p':P[i],'b':B[i]})

C.sort(key = getP)

print(C)