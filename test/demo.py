from __future__ import print_function

move=[]

move.append(10)
print(move)

move.append(6)
print(move)

move.append(5)
print(move)
print("Enter value : ")
move1=int(raw_input())
limit=len(move)


# for i in range(0,limit):
#     if(move1!=move[i]) :
#         move.append(move1)
#         limit=len(move)
#         break
#
#     else:
#         print("Enter new value : ")
for i in range(0,limit) :
    if move1 in move[i] :
        print("Enter new value : ")
        move1=int(raw_input())

    else :
        move.append(move1)

print(move)
