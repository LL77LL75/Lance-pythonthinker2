SCORe = 0
answer1 = input("how many legs does an octopus have? ")
# a = 1
# while 1>0:
#     a = a+1
#     print(a)
while (int(answer1) != 8) or not(answer1 == "skip"):
    answer1 = input("how many legs does an octopus have? ")
else:
    SCORe+=1
    answer2 = input("how many months are there in a year? ")
    while (str(answer2) != 12) or not(answer2 == "skip"):
        answer2 = int(input("how many months are there in a year? "))
    else:
        SCORe+=1
        answer3 = input("how letters are there in the alpabet? ")
        while (int(answer3) != 26) or not(answer3 == "skip"):
            answer3 = input("how letters are there in the alpabet? ")
SCORe+=1
print("u have at least 1 iq")
print("your score is " + str(SCORe))