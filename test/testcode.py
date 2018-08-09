from __future__ import print_function

data = [1,5,9]
sub = []
count = 0
result=0
if len(data) >= 3:
    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):

            if abs(data[i] - data[j]) in sub:
                if abs(data[i] - data[j])%2==0:
                    if sum(data)%2!=0:
                        count+=1
                        break
                elif sum(data)%2==0:
                    count+=1
                    break

            else:
                sub.append(abs(data[i] - data[j]))

        if (count >= 1 and sum(data) % 2 == 0) or count>=2:
            break

if (count >= 1 and sum(data) % 2 == 0) or count>=2:
    print("Pattern formed... ")
else:
    print("Not formed")
