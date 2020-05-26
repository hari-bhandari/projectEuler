import math
def highlyDivisibleTrangle(length):
    found=False
    number=10000
    while found==False:
        trangleNumber=1/2*number*(number+1)
        factorsList=factorize(trangleNumber)
        number+=1
        if len(factorsList)>length:
            found=True
            return trangleNumber



def factorize(n):
    factorsList = []
    for i in range(1,int(n/2)+1):
        if n%i==0:
            factorsList.append(i)

    factorsList.append(n)
    return factorsList


# print(factorize(28))
print(highlyDivisibleTrangle(500))