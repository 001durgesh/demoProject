
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

print("Enter the number")
number = int(input())
print(isPrime(number))


