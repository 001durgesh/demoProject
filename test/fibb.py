from __future__ import print_function

def fibbinaciSeries(limit):
    i=1
    j=0
    print(j, i, end=' ')

    for count in range(0,limit-2):
        i=i+j
        j=i-j
        print(i, end=' ')



print("Enter number till you want Fibbanaci series :")
inputNumber = input()

fibbinaciSeries(inputNumber)
