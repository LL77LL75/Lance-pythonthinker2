SCORe = 0
answer1 = int(input("how many legs does an octopus have? "))
# a = 1
# while 1>0:
#     a = a+1
#     print(a)
while (answer1 != 8) or not(str(answer1) == "skip"):
    answer1 = int(input("how many legs does an octopus have? "))
else:
    SCORe+=1
    answer2 = int(input("how many months are there in a year? "))
    while (answer2 != 12) or not(str(answer2) == "skip"):
        answer2 = int(input("how many months are there in a year? "))
    else:
        SCORe+=1
        answer3 = int(input("how letters are there in the alpabet? "))
        while (answer3 != 26) or not(str(answer2) == "skip"):
            answer3 = int(input("how letters are there in the alpabet? "))
SCORe+=1
print("u have at least 1 iq")
print("your score is " + str(SCORe))