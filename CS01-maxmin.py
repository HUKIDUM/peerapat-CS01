num = int(input("Enter Your loop : "))
numM = []
for i in range(num):
    data = int(input("Enter Your Number : "))
    numM += [data]
print(numM)
numM.sort(reverse=False)
print(numM[0])
numMM = len(numM)
print(numM[numMM-1])