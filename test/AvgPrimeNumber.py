
def isPrime(number) :
    flag = 1
    if number <= 1:
        flag = 0
    elif number == 2:
        pass

    if number > 2 :
        i=2
        while (i <= number/2) :
            if number%i==0 :
                flag=0
                break
            i+=1

    if flag==1 :
        return True
    else:
        return False

print("How many prime to be Averaged : ")
total = int(input())

primeList= []
i =1
avg = 0.0

while len(primeList) < total :

    if isPrime(i) is True :
        primeList.append(i)
        avg = avg + i

    i+=1

print("Prime numbers are : ", primeList)

print("Average of prime numbers is : ", (avg/total))





